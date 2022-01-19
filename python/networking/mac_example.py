"""
MAC addressing in Python
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/MLc2ldyTK14
"""
from getmac import get_mac_address as gmac
from netaddr import *
print(gmac())
mac = EUI(gmac())
print(mac.info)
oui = mac.oui
print(oui.registration().org)
print(oui.registration().address)
