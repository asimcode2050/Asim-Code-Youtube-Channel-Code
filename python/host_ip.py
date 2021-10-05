'''
Youtube Channel : Asim Code
How to Get the Ip address and Hostname of Website In Python
https://youtu.be/ZG-VihtIpME
'''
import socket

def show_host_ip():
    hostname = input("Please enter website URL :")
    try:
        print(f'Hostname: {hostname}')
        print(f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invalid Hostanme , error : {error}')

show_host_ip()
