import xmltodict
import requests

site_map = xmltodict.parse(requests.get('https://netroxtech.com/sitemap-pt-post-2019-11.xml').text)
urls = [url["loc"] for url in site_map["urlset"]["url"]]
print("\n".join(urls[0:3]))
