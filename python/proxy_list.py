'''
HTTPS proxies List in Python
YouTube Channel: Asim Code
Please Subscribe to Asim Code.
https://youtu.be/HYl0EWEKEW0
'''
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.sslproxies.org/')
soup = BeautifulSoup(resp.text,"lxml")
proxy_list = []
table = soup.find('tbody')
table_rows = table.find_all('tr')
for row in table_rows:
        ip = row.find_all('td')[0]
        port = row.find_all('td')[1]
        proxy_list.append(f'{ip.text}:{port.text}')

print(proxy_list)

