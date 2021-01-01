import socket
ONE_CONNECTION_ONLY =(True)
filename = "file.txt"
port =1218
sock = socket.socket()
host = socket.gethostname()
sock.bind((host,port))
sock.listen(10)
print("File Server started....")
while True:
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    data = conn.recv(1024)
    print(f"Server received {data}")
    with open (filename,"rb") as file:
        data = file.read(1024)
        while data:
            conn.send(data)
            print(f"Sent {data!r}")
            data = file.read(1024)
    print("File sent complete.")
    conn.close()
    if(ONE_CONNECTION_ONLY):
        break
sock.shutdown(1)
sock.close()