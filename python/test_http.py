import socket

serverHost = 'localhost'
serverPort  = 8080
print('Connecting to HTTP Server:')
httpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
httpClient.connect((serverHost,serverPort))
httpClient.send(bytes("GET / HTTP/1.1\r\nHost:localhost\r\n\r\n".encode('utf-8')))
resp = httpClient.recv(4096)
print("Response from HTTP Server:")
print(resp.decode())
