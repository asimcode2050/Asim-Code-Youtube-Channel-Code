import socket
from geolite2 import geolite2
import json
hostname = "google.com"
ip_address = socket.gethostbyname(hostname)
print("Id : {0}".format(ip_address))
reader = geolite2.reader()
response = reader.get(ip_address)
print(json.dumps(response['continent']['names']['en'],indent =4))
print(json.dumps(response['country']['names']['en'],indent =4))
print(json.dumps(response['location']['latitude'],indent =4))
print(json.dumps(response['location']['longitude'],indent =4))
print(json.dumps(response['location']['time_zone'],indent =4))
