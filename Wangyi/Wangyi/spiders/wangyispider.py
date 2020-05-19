# -*- coding: utf-8 -*-
import csv
import time
from Wangyi.items import WangyiItem
import scrapy


class WangyispiderSpider(scrapy.Spider):
    name = 'wangyispider'
    # allowed_domains = ['http://dy.163.com']
    # start_urls = ['http://http://dy.163.com/']

    s = time.time()
    with open("网易.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\wangyi.csv'))
        for i in data:
            print(i[0])
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = WangyiItem()
        comment_num = response.xpath('//span[@class="num"]/a/text()').extract()
        if comment_num == []:
            item['comment_num'] = ''
        else:
            item['comment_num'] = comment_num[0]
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['read_num'] = ''
        item['up_num'] = ''
        item["zhuanfa"] = ''
        yield item

    def close(spider, reason):
        print(time.time() - WangyispiderSpider.s)