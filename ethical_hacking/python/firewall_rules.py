import subprocess

def list_firewall_rules():
    command = "netsh advfirewall firewall show rule name=all"
    result = subprocess.run(command, capture_output=True, shell=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    list_firewall_rules()


