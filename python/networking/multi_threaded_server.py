import socket
import threading
import logging
from queue import Queue
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
HOST = '0.0.0.0'
PORT = 5555
MAX_CLIENTS = 50
BUFFER_SIZE = 1024  # Max message length
clients = {}
client_threads = {}
client_lock = threading.Lock()
msg_queue = Queue()


def authenticate(client_socket):
    client_socket.send(
        "Welcome to the chat! Please enter your username: ".encode())
    username = client_socket.recv(BUFFER_SIZE).decode().strip()
    while username in clients.values():
        client_socket.send(
            "Username is already taken. Please choose a different one: ".encode())
        username = client_socket.recv(BUFFER_SIZE).decode().strip()
    client_socket.send(
        f"Hello {username}, you are now connected to the chat server.\n".encode())
    logging.info(f"Client {username} authenticated.")
    return username


def handle_client(client_socket, client_address):
    try:
        username = authenticate(client_socket)
        with client_lock:
            clients[client_socket] = username  # Store the client's username
            client_threads[client_socket] = threading.current_thread()
        broadcast(f"{username} has joined the chat.\n", client_socket)
        while True:
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8').strip()
            if not message:
                break
            if message.startswith("/"):
                process_command(message, client_socket)
            else:
                broadcast(f"{username}: {message}\n", client_socket)
        disconnect_client(client_socket, username)
    except Exception as e:
        logging.error(f"Error with client {client_address}: {e}")
    finally:
        client_socket.close()


def broadcast(message, sender_socket):
    with client_lock:
        for client_socket in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode('utf-8'))
                except Exception as e:
                    logging.error(f"Error sending message to {
                                  client_socket}: {e}")
                    remove_client(client_socket)


def send_private_message(username, message, sender_socket):
    recipient_username = message.split(" ", 1)[0]
    private_message = message.split(" ", 1)[1] if len(
        message.split(" ", 1)) > 1 else ""
    with client_lock:
        for client_socket, user in clients.items():
            if user == recipient_username:
                try:
                    client_socket.send(f"(Private from {clients[sender_socket]}): {
                                       private_message}".encode())
                    sender_socket.send(f"Private message sent to {
                                       recipient_username}: {private_message}".encode())
                except Exception as e:
                    logging.error(f"Error sending private message to {
                                  recipient_username}: {e}")
                    sender_socket.send(f"Failed to send private message to {
                                       recipient_username}".encode())
                break
        else:
            sender_socket.send(
                f"User {recipient_username} not found.".encode())


def process_command(command, client_socket):
    if command.startswith("/nick"):
        new_username = command.split(" ", 1)[1]
        old_username = clients.get(client_socket)
        with client_lock:
            clients[client_socket] = new_username
        client_socket.send(f"Your username has been changed to {
                           new_username}.\n".encode())
        broadcast(f"{old_username} is now known as {
                  new_username}\n", client_socket)
    elif command.startswith("/quit"):
        disconnect_client(client_socket, clients.get(client_socket))
    elif command.startswith("/private"):
        send_private_message(command.split(" ", 1)[1], command, client_socket)
    else:
        client_socket.send(
            "Unknown command. Type /help for available commands.\n".encode())


def disconnect_client(client_socket, username=None):
    with client_lock:
        if username:
            broadcast(f"{username} has left the chat.\n", client_socket)
        if client_socket in clients:
            del clients[client_socket]
        if client_socket in client_threads:
            del client_threads[client_socket]


def shutdown_server(server_socket):
    logging.info("Shutting down the server.")
    with client_lock:
        for client_socket in list(clients.keys()):
            disconnect_client(client_socket, clients.get(client_socket))
    server_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CLIENTS)
    logging.info(f"Server started on {HOST}:{PORT}")
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            logging.info(f"New connection from {client_address}")
            client_thread = threading.Thread(
                target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        logging.info("Server shutdown initiated.")
        shutdown_server(server_socket)


if __name__ == "__main__":
    start_server()
