# https://www.youtube.com/watch?v=pnVgH2lmPQM&ab_channel=AsimCode
import socket
from datetime import datetime

server_address = ('localhost',6789)
data_size = 4096
print('Client starting at ',datetime.now())
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b'Hi!',server_address)
data, server = client_socket.recvfrom(data_size)
print('### At',datetime.now(),server, 'replied',data)
client_socket.close()

