"""
IPAddress from netaddr in Python
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/gMtBiNjgeKE
"""
from netaddr import IPAddress
ip = IPAddress('192.168.56.1')
print(ip.version)
print(ip.bin)
print(ip.bits())
print(ip.words)
print(ip.is_unicast())
print(ip.is_link_local())
