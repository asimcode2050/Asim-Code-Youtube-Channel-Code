""" Python SSH connection with pxssh and running a command on a remote SSH server """
""" https://youtu.be/XS2A9caAIhc """
from pexpect import pxssh
import getpass
try:
    conn = pxssh.pxssh()
    hostname = input('hostname: ')
    username =input('username: ')
    password = getpass.getpass('password: ')
    conn.login(hostname,username,password)
    conn.sendline('ls -l')
    conn.prompt()
    print(conn.before)
except pxssh.ExceptionPxssh as ex:
    print("Cannot login")
    print(str(ex))
