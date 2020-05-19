import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

headers={
    "User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

url = "https://club.autohome.com.cn/bbs/thread/c5d62dc681343d6c/84760998-1.html"

#res = requests.get(url, headers=headers)
#print(res.status_code)
#if res.status_code == 200:
#    response = etree.HTML(res.text)
#    print(res.text)
#    read_number = response.xpath('//div[@class="consnav"]/span[1]/font[1]/text()')[0]
#    comment_number = response.xpath('//div[@class="consnav"]/span/font[@id="x-replys"]/text()')[0]
#    print(read_number, comment_number)


driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

response = etree.HTML(driver.page_source)
read_number = response.xpath('//div[@class="consnav"]/span[1]/font[1]/text()')[0]
comment_number = response.xpath('//div[@class="consnav"]/span/font[@id="x-replys"]/text()')[0]
print(read_number, comment_number)