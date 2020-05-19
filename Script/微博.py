# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:01:27 2019

@author: liuyuntao
"""

from lxml import etree
from selenium import webdriver
import time

url = "https://weibo.com/baojun630sgmw"

opt = webdriver.ChromeOptions()

opt.add_argument('--proxy-server=http://114.249.119.19:9000')

driver = webdriver.Chrome()
cookies = driver.get_cookies()
print(cookies)
driver.get(url)
time.sleep(15)


for i in range(10000, 30001,10000):   
    js = "var q=document.documentElement.scrollTop=%s;" % i
    driver.execute_script(js)
    time.sleep(3)
    response = etree.HTML(driver.page_source)
    base = response.xpath('//div[@class="WB_feed WB_feed_v3 WB_feed_v4"]')
    #print(base)
    for each in base:
    #    微博发表时间
        publish_time = each.xpath('.//div[@class="WB_detail"]//div[@class="WB_from S_txt2"]/a[1]/text()')
    #    微博内容
        content = each.xpath('.//div[@class="WB_detail"]//div[@class="WB_text W_f14"]/text()')
        #微博转发
        transpond = each.xpath('.//div[@class="WB_feed_handle"]//li[2]//em[2]/text()')
        #微博评论数
        comment_num = each.xpath('.//div[@class="WB_feed_handle"]//li[3]//em[2]/text()')
        #微博点赞数
        up_num = each.xpath('.//div[@class="WB_feed_handle"]//li[4]//em[2]/text()')
print(publish_time, transpond, comment_num, up_num)
driver.close()