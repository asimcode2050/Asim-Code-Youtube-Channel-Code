'''
In this video we will learn how to extract text inside html tag
using Python and Beautiful Soup.
https://youtu.be/36iuqQJ8X4g
'''

from bs4 import BeautifulSoup
html_data = '''\
    <div>
        <div>Python Program</div>
        <span>
            <div><span>Extract Text Example</span></div>
        </span>
        </div>'''
soup = BeautifulSoup(html_data,'html.parser')
our_text = soup.select_one('div span div span')
print(our_text.text)
