"""
Python Telnet
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/7VOL4a_7NfI
"""
import getpass
import telnetlib

HOST_NAME = "localhost"
user = input("Please enter your remote account: ")
password = getpass.getpass()
tel_net = telnetlib.Telnet(HOST_NAME)
tel_net.read_until(b"login: ")
tel_net.write(user.encode('ascii') + b"\n")
if password:
    tel_net.read_until(b"Password: ")
    tel_net.write(password.encode('ascii') + b"\n")

tel_net.write(b"ls\n")
tel_net.write(b"exit\n")
print(tel_net.read_all().decode('ascii'))
