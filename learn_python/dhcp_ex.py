import socket
import random
import time
class DHCPServer:
    def __init__(self, ip_range_start, ip_range_end):
        self.ip_range_start = ip_range_start
        self.ip_range_end = ip_range_end
        self.allocated_ips = []  # List of integers representing allocated IPs
    def assign_ip(self):
        available_ips = [ip for ip in range(self.ip_range_start, self.ip_range_end + 1)
                         if ip not in self.allocated_ips]

        if not available_ips:
            return None

        assigned_ip = random.choice(available_ips)
        self.allocated_ips.append(assigned_ip)  # Marks this IP as assigned.

        return assigned_ip

    def lease_time(self):
        return random.randint(30, 120)


class DHCPClient:
    def __init__(self, server: DHCPServer):
        self.server = server  # Reference to the DHCPServer object (instance)
        self.ip_address = None
        self.lease_time = 0

    def request_ip(self):
        print("Client: Sending DHCPDISCOVER message to server...")
        time.sleep(1)

        self.ip_address = self.server.assign_ip()

        if self.ip_address is None:
            print("Client: No IP addresses available.")
            return False 

        print(f"Client: Assigned IP address {self.ip_address} by DHCP Server.")

        self.lease_time = self.server.lease_time()
        print(f"Client: IP address {self.ip_address} leased for {
              self.lease_time} seconds.")

        return True

    def release_ip(self):

        print(f"Client: Releasing IP address {self.ip_address}.")
        self.ip_address = None  # Sets the IP address to None (no IP assigned).

def simulate_dhcp_process():
    dhcp_server = DHCPServer(ip_range_start=1921681100,
                             ip_range_end=1921681110)

    client1 = DHCPClient(dhcp_server)
    if client1.request_ip():
        time.sleep(client1.lease_time)
        client1.release_ip()

    client2 = DHCPClient(dhcp_server)
    if client2.request_ip():
        time.sleep(client2.lease_time)
        client2.release_ip()


simulate_dhcp_process()
