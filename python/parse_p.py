import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

counter = 0
ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
link = input('Please Enter the URL:')
html_content = urllib.request.urlopen(link,context=ctx).read()
soup = BeautifulSoup(html_content,'html.parser')
p_tags = soup('p')
for tag in p_tags:
    counter += 1

print(counter)