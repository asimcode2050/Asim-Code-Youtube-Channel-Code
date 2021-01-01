import socket
import os
localhost = "10.0.2.15"
if os.name == "nt":
    socket_protocol = soket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP
packet_reader = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket_protocol) 
packet_reader.bind((localhost,0))
packet_reader.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)
if os.name == "nt":
    packet_reader.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
print(packet_reader.recvfrom(65535))
if os.name == "nt":
    packet_reader.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

