from scapy.all import ARP, Ether, srp

def network_scan(target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=2,verbose=False)[0]
    live_hosts= []
    for sent, received in result:
        live_hosts.append(received.psrc)

    return live_hosts

if __name__== "__main__":
    target_ip = "192.168.1.1/24"
    hosts = network_scan(target_ip)
    print("Live hosts in the network:")
    for host in hosts:
        print(host)
