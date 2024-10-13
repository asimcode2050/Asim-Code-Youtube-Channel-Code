import socket 
import struct

sus_patterns = ['danger.com','unauthorized_access']

def sniff_packet():
    sock = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0003))

    while True:
        raw_data, addr = sock.recvfrom(65535)
        eth_header = raw_data[:14]
        eth_data = struct.unpack('!6s6sH',eth_header)

        payload = raw_data[14:]

        for pattern in sus_patterns:
            if pattern.encode() in payload:
                print(f'Suspicious activity detected: {pattern} in {addr}')

if __name__=='__main__':
    print('Starting packet sniffer, intrusion detection!')
    sniff_packet()

                                      




