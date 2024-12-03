'''
pip install requests beautifulsoup4

'''
import requests
from bs4 import BeautifulSoup
url = 'https://wikipedia.org'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headings = soup.find_all('h1')
    for heading in headings:
        print(heading.text)
else:
    print('Failed to retrieve the page')
