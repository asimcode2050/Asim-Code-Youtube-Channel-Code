import socket
def dns_lookup(domain_name):
    try:
        print(f"Looking up the IP address for: {domain_name}")
        ip_address = socket.gethostbyname(domain_name)
        print(f"The IP address for {domain_name} is: {ip_address}")
        return ip_address
    except socket.gaierror:
        print(f"Error: Could not resolve the domain {
              domain_name}. Please check the domain or your network.")
        return None

if __name__ == "__main__":
    domain_name = "example.com"
    dns_lookup(domain_name)
