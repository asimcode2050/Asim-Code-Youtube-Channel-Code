import os, re, requests
def downloadImages(url):
    resp = requests.get(url)
    text = resp.text
    reg_ex = r'<img.*?src="(.*?)"[^\>]+>'
    img_links =re.findall(reg_ex,text)

    for link in img_links:
        os.system("wget {}".format(link))

    return "Done"

print("Image Downloader")
link = input("Please enter the url:")
downloadImages(link)
