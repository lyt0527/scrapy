# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:33:45 2019

@author: liuyuntao
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url ='https://www.toutiao.com/'
opt = webdriver.ChromeOptions()

opt.set_headless()

driver =webdriver.Chrome()

driver.get(url)

driver.implicitly_wait(10)
#brower.maximize_window() # 最大化窗口
#brower.implicitly_wait(10)
#brower.find_element_by_link_text('热点').click()
#brower.implicitly_wait(10)
#添加代理IP
#opt = webdriver.ChromeOptions()
#opt.add_argument("--proxy-server=http://61.185.96.132:8118")
#设置无头
#opt.set_headless()

#查看IP
#driver.get("http://httpbin.org/ip")

title_list,url_list,sources_list,comments_list=[],[],[],[]
# 获取页面新闻标题，详情页面链接，来源，评论，并添加到列表中
titles= driver.find_elements_by_xpath('//div[@class="title-box"]/a')
for title in titles:
    title_list.append(title.text)
    
urls = driver.find_elements_by_xpath('//div[@class="title-box"]/a')
for url in urls:
    url = url.get_attribute('href')
    url_list.append(url)
    
sources = driver.find_elements_by_xpath('//a[@class="lbtn source"]')
for source in sources:
    sources_list.append(source.text)
    
comments =driver.find_elements_by_xpath('//a[@class="lbtn comment"]')
for comment in comments:
    comments_list.append(comment.text)
print(titles)