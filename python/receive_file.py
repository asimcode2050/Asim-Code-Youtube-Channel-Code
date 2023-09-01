import socket

def recv_file():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    sock.connect((host, port))
    sock.send(b"Hello Server!")

    with open("ReceviedFile","wb") as file:
        print("File opened")
        print("Receiving data...")
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)

    print("Successfully received the file")
    sock.close()
    print("Connection Closed")

recv_file()

