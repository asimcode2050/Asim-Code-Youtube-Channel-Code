import mechanicalsoup
import http.cookiejar

def get_cookies(url):
    browser = mechanicalsoup.StatefulBrowser()
    cookieJar = http.cookiejar.CookieJar()
    browser.set_cookiejar(cookieJar)
    browser.open(url)
    for cookie in cookieJar:
        print(cookie.__dict__)
if __name__== '__main__':
    site = 'https://google.com'
    get_cookies(site)
