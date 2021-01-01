import requests
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('user','pass'))
print('Response Code '+ str(response.status_code))
if response.status_code == 200:
    print('Login successful: '+response.text)