# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:35:19 2019

@author: liuyuntao
"""

import requests
from lxml import etree
import csv

url = "https://bbs.baojunev.com/"
headers={
    "User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

response = etree.HTML(requests.get(url, headers=headers).text)

base = response.xpath('//div[@class="container"]//div[@class="col-lg-3 col-md-6 col-sm-6"]')


def main():
    for each in base:
        link = each.xpath('.//h4/a/@href')[0]
        time = each.xpath('.//div/span/text()')[0].strip()
        author = each.xpath('.//div/a/span/text()')[0].strip()
        read_num = each.xpath('.//div[@class="i-count fright"]/span[1]//text()')[0].strip()
        comment_num = each.xpath('.//div[@class="i-count fright"]/span[2]//text()')[0].strip()
        praise_num = each.xpath('.//div[@class="i-count fright"]/span[3]//text()')[0].strip()
        
        url1 = url + link      
        url1 = url1.replace("a=index", "a=comment_list")
        res = etree.HTML(requests.get(url1, headers=headers).text)
        r_list = res.xpath('//div[@class="comment-item"]')
        for r in r_list:
        	comment_nickname = r.xpath('./div/a/span[@class="use-n"]/text()')[0].strip()
        	comment_time = r.xpath('./div/a/span[@class="use-t"]/text()')[0].strip()
        	comment_author = r.xpath('./div[@class="item-p"]/text()')[0].strip()
        	with open("论坛.csv", "a", newline="", encoding="utf-8") as f:
        		writer = csv.writer(f)
        		writer.writerow([url1, time, author, read_num, comment_num, praise_num, comment_nickname, comment_time, comment_author])
    

    
if __name__ == "__main__":
    main()
    print("写入完成")
			













