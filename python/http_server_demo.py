import socket
serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('localhost',8080))
serverSocket.listen(5)

while True:
    print('Server waiting for connections')
    (cSocket, address) = serverSocket.accept()
    print('HTTP server request received:')
    print(cSocket.recv(1024))
    cSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hello World From HTTP Server</h1></body></html>\r\n",'utf-8'))
    cSocket.close()