import sys
import json
from urllib.request import urlopen
def get_lat_long():
    resp = urlopen('http://ipinfo.io').read()
    json_data = json.loads(resp)
    lat, longitude =json_data.get('loc').split(',')
    return(lat,longitude)
print(get_lat_long())