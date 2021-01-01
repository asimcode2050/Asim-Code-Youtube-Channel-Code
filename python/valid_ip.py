import socket
def check_ipv4(address):
    try:
        if socket.inet_aton(str(address)):
            return True
    except:
        return False
print(check_ipv4('10.0.2.15'))