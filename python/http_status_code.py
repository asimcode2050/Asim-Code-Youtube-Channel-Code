'''
YouTube Channel : Asim Code
How to Fetch HTTP status code in Python
https://youtu.be/iMuuYvsdz-E
'''
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import emoji
url = input('Please enter the URL: ')

try:
    response = urlopen(url)
    print('Status Code : '+str(response.code) + ' ' +emoji.emojize(':thumbs_up:'))
    print('Message : '+ 'Request successful - ' + response.reason)
except HTTPError as err:
    print('Status Code : ' + str(err.code) + ' ' + emoji.emojize(':thumbs_down:') )
    print('Message: Request failed -  ' + err.reason)
except URLError as e:
    print(emoji.emojize(':thumbs_down:'))
