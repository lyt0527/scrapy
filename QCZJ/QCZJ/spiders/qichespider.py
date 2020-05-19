# -*- coding: utf-8 -*-
import csv
import re
import time
import scrapy
from QCZJ.items import QczjItem

class QichespiderSpider(scrapy.Spider):
    name = 'qichespider'
    # allowed_domains = ['club.autohome.com.cn']
    # start_urls = ['http://club.autohome.com.cn/']
    s = time.time()
    with open("汽车之家.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\qichezhijia.csv'))
        for i in data:
            url = "https://club.m." + i[0][13:]
            yield scrapy.Request(url=url, meta={'url':url, 'MonitorName':i[1]}, callback=self.parse)

    def parse(self, response):
        try:
            print("进入try..........................")
            item = QczjItem()
            item['read_num'] = re.findall(r'<span id="views">(.+?)</span>', response.text)[0]
            item['comment_num'] = re.findall(r'<span id="replys">(.+?)</span>', response.text)[0]
            item['up_num'] = ''
            item['zhuanfa'] = ''
            item['url'] = response.meta.get('url')
            item['MonitorName'] = response.meta.get('MonitorName')
            print(item['url'], item['MonitorName'], item['read_num'], item['up_num'], item['comment_num'], item['zhuanfa'])

        except:
            print("进入except.......................")

        yield item

    def close(spider, reason):
        print(time.time() - QichespiderSpider.s)
