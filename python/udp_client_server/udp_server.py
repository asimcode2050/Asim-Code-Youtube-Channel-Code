# https://www.youtube.com/watch?v=pnVgH2lmPQM&ab_channel=AsimCode
import socket
from datetime import datetime

server_address = ('localhost',6789)
data_size = 4096
print('Server starting at :',datetime.now())
print('Waiting for a client to connect.')
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(server_address)
data , client = server_socket.recvfrom(data_size)
print('*** AT ', datetime.now(),client,'data',data)
server_socket.sendto(b'Hello from server',client)
server_socket.close()
