import socket  # Import the socket module
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("Server is waiting for messages...")
while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received message: {data.decode()} from {client_address}")
