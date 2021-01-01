import paramiko
def ssh_connect(ip,user,password,command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=password)
    session = client.get_transport().open_session()
    if session.active:
        session.exec_command(command)
        print(session.recv(1024))
    return
ssh_connect('127.0.0.1','asim','asim123','id')

