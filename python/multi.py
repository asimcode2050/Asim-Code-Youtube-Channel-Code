import socket, time
import threading

sock = socket.socket()
sock.bind(("10.0.2.15",6398))
sock.listen(5)

def info(client):
    message = client.recv(1024).decode()
    if(message !=""):
        print(message)
    return

while True:
    (client, (ip,port)) = sock.accept()
    print("Client connected...")
    threading.Thread(target=info,args=(client,)).start()