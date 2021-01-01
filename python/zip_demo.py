import requests
from requests.auth import HTTPDigestAuth
response = requests.get('http://httpbin.org/digest-auth/auth/user/pass',auth=HTTPDigestAuth('user','pass'))
print(str(response.status_code))