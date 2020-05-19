# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:06:37 2019

@author: liuyuntao
"""

from selenium import webdriver
from lxml import etree
import time

url = "https://cj.sina.com.cn/"

#opt = webdriver.ChromeOptions()
#opt.add_argument("--headless")
#opt.add_argument('--proxy-server=http://123.139.56.238:9999')

driver = webdriver.Chrome()
driver.get(url)

time.sleep(15)

response = etree.HTML(driver.page_source)
base = response.xpath('//li[@class="m-article-item"]')
for each in base:
    #标题
    title = each.xpath('.//h2/a/text()')[0]
    #来源
    from_address = each.xpath('.//div[@class="m-article-des clearfix"]/a/text()')[0]
    #时间
    times = each.xpath('.//div[@class="m-article-des clearfix"]/span[2]/text()')[0]

    print(title, from_address, times) 
driver.close()