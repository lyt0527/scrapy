from selenium import webdriver
import requests


driver = webdriver.Chrome()
url = 'http://auto.mop.com/a/190905105018279.html'
driver.get(url)
print(driver.page_source)