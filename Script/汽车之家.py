# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:11:51 2019

@author: liuyuntao
"""
import time
from lxml import etree
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument('--proxy-server=http://123.139.56.238:9999')
#opt.add_argument('--headless')

driver = webdriver.Chrome(options=opt)


base_url = "https://club.autohome.com.cn/bbs/forum-c-4890-"


for i in range(3):
    url = base_url + str(i+1) + ".html"
    print(url)
    driver.get(url)
    time.sleep(15)
    response = etree.HTML(driver.page_source)
    base = response.xpath('//li[@class="text-type"]')
    for each in base:
        title = each.xpath('.//p[@class="post-title"]/a/text()')[0]
        author = each.xpath('./div[@class="post-basic-info"]/a/text()')[0]
        post_time = each.xpath('./div[@class="post-basic-info"]/i[1]/text()')[0]
        browse = each.xpath('./div[@class="post-basic-info"]/i[3]/text()')[0]
        reply = each.xpath('./div[@class="post-basic-info"]/i[2]/text()')[0]
        print(title, author, post_time, browse, reply)
driver.close()