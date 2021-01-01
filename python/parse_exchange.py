from selenium import webdriver
from bs4 import BeautifulSoup
driver_path = '/home/asim/Downloads/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(driver_path)
url = 'https://calculator.net/currency-calculator.html'
driver.get(url)
html_soup = BeautifulSoup(driver.page_source,'html.parser')
table = html_soup.find_all('table', class_='cinfoT')
driver.quit()
print(table[0].tbody)