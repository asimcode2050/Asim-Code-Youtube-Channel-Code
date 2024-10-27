import ssl
import socket
from datetime import datetime

def check_ssl_expiration(domain):
    port = 443
    context = ssl.create_default_context()
    try:
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiration_date = cert['notAfter']
                expiration_date = datetime.strptime(expiration_date, '%b %d %H:%M:%S %Y GMT')
                days_until_expiration = (expiration_date - datetime.now()).days
                print(f"SSL certificate for {domain} expires on {expiration_date}"
                    f"({days_until_expiration} days remaining)")
    except Exception as e:
        print(f"Failed to retrieve SSL certificate for {domain}: {e}")

if __name__ == "__main__":
    target_domain  = input("Enter the domain to check :")
    check_ssl_expiration(target_domain)





