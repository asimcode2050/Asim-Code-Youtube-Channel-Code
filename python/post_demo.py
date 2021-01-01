import requests
from requests import post

proxy_list = {
    'http':'http://192.168.1.100:3000',
    'https':'http://192.168.1.101:1080',
}
foo = requests.post('http://httpbin.org/post',proxies=proxy_list)
print(foo)