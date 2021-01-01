import socket
sock = socket.socket()
host = socket.gethostname()
port = 1218
sock.connect((host,port))
sock.send(b"Hello from client")
with open("readfile.txt","wb") as file:
    print("File open")
    print("receiving data...")
    while True:
        data = sock.recv(1024)
        print(f"data={data}")
        if not data:
            break
        file.write(data)
print("Got the file")
sock.close()
print("Connection is closed")
