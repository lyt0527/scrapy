# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:35:19 2019

@author: liuyuntao
"""

from selenium import webdriver
from lxml import etree
import time
import csv

opt = webdriver.ChromeOptions()
opt.set_headless()

driver = webdriver.Chrome(options=opt)
url = "https://bbs.baojunev.com/"
driver.get(url)


def main(): 
    i = 0
    while True:
        response = etree.HTML(driver.page_source)
        base = response.xpath('//div[@class="container"]//div[@class="col-lg-3 col-md-6 col-sm-6"]')
        for each in base[i:i+20]:
            # 标题
            title = each.xpath('.//h4/a/text()')[0].strip()
            # 发表时间
            Time = each.xpath('.//div/span/text()')[0].strip()
            # 作者
            author = each.xpath('.//div/a/span/text()')[0].strip()
            # 阅读量
            read_num = each.xpath('.//div[@class="i-count fright"]/span[1]//text()')[0].strip()
            # 评论数量
            comment_num = each.xpath('.//div[@class="i-count fright"]/span[2]//text()')[0].strip()
            # 点赞数
            praise_num = each.xpath('.//div[@class="i-count fright"]/span[3]//text()')[0].strip()
            
#            print(title, Time, author, read_num, comment_num, praise_num)
            # 写入本地
            with open("主页.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([title, Time, author, read_num, comment_num, praise_num])
            print("写入完成")
            
        i += 20
        # 判断是否存在这个字段
        if response.xpath('//div[@class="container"]//div[@id="btn-more"]/text()')[0].strip() == '加载更多':
            driver.find_element_by_id("btn-more").click()
            time.sleep(1)         
        else:
            break
            
                

    
if __name__ == "__main__":
    main()
			













