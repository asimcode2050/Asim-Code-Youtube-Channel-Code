import subprocess

def block_ip(ip):
    command = f"netsh advfirewall firewall add rule name=\"Block {ip}\" dir=in action=block remoteip={ip}"
    subprocess.run(command, shell=True)
    print(f"Blocked IP: {ip}")

if __name__== "__main__":
    suspicious_ip = "192.168.1.100"
    block_ip(suspicious_ip)

