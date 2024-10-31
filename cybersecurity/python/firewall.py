from scapy.all import *
import os

# Specify the IP address to block
BLOCKED_IP = " 192.168.1.6"

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        # Get the source IP
        src_ip = packet[IP].src
        if src_ip == BLOCKED_IP:
            print(f"Blocked packet from {src_ip}")
            return  # Drop the packet
        else:
            print(f"Allowed packet from {src_ip}")

# Set up packet sniffing
def start_firewall():
    print("Starting firewall... Press Ctrl+C to stop.")
    try:
        sniff(prn=packet_callback, store=0)  # Capture packets without storing them
    except KeyboardInterrupt:
        print("Firewall stopped.")
        os._exit(0)

if __name__ == "__main__":
    start_firewall()
