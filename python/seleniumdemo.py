import time
from selenium import webdriver
driver = webdriver.Chrome('/home/asim/Downloads/chromedriver_linux64/chromedriver')
driver.get('https://google.com')
print(driver.title)
time.sleep(10)
driver.quit
