import socket
import threading
import sys
SERVER_HOST = 'localhost'  # Change to the IP address of the server if necessary
SERVER_PORT = 5555
BUFFER_SIZE = 1024
client_socket = None
username = None


def receive_messages():
    global username
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if message:
                print(message)
            else:
                print("Disconnected from the server.")
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


def send_message():
    global username
    while True:
        message = input()
        if message.lower() == '/quit':
            client_socket.send(message.encode('utf-8'))
            print("You have left the chat.")
            break
        elif message.startswith("/nick"):
            new_username = message.split(" ", 1)[1] if len(
                message.split(" ", 1)) > 1 else ""
            if new_username:
                client_socket.send(f"/nick {new_username}".encode('utf-8'))
                username = new_username
            else:
                print("Please specify a new username: /nick <new_username>")
        elif message.startswith("/private"):
            parts = message.split(" ", 2)
            if len(parts) > 2:
                recipient = parts[1]
                private_message = parts[2]
                client_socket.send(
                    f"/private {recipient} {private_message}".encode('utf-8'))
            else:
                print("Usage: /private <username> <message>")
        else:  # Regular message
            client_socket.send(message.encode('utf-8'))


def connect_to_server():
    global client_socket, username
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Connected to the server at {SERVER_HOST}:{SERVER_PORT}")
        username = input("Please enter your username: ")
        client_socket.send(username.encode('utf-8'))
        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.daemon = True  # Allow the thread to exit when the program ends
        receive_thread.start()
        send_message()
    except Exception as e:
        print(f"Error connecting to server: {e}")
        sys.exit()


if __name__ == "__main__":
    connect_to_server()
