def sendfile(filename: str ="myfile.txt", testing:bool =False) -> None:
    import socket
    port = 12345 
    sock = socket.socket()
    host = socket.gethostname()
    sock.bind((host,port))
    sock.listen(5)
    print("Server started and listening....")

    while True:
        conn, addr = sock.accept()
        print(f"Got connection from {addr}")
        data = conn.recv(1024)
        print(f"Server recieved: {data : }")
        with open(filename, "rb") as file:
            data = file.read(1024)
            while data:
                conn.send(data)
                print(f"sent {data!r}")
                data = file.read(1024)
        print("Done sending")
        conn.close()
    sock.shutdown(1)
    sock.close()

sendfile()




