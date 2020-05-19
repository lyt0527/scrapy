# -*- coding: utf-8 -*-
import csv
import re
import time
import scrapy
from Toutiao.items import ToutiaoItem


class ToutiaospiderSpider(scrapy.Spider):
    name = 'toutiaospider'
    # allowed_domains = ['www.toutiao.com']
    # start_urls = ['http://www.toutiao.com/']

    s = time.time()
    with open("今日头条.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\toutiao.csv'))
        for i in data:
            # print(i[0])
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse, dont_filter=True)

    def parse(self, response):

        item = ToutiaoItem()
        item['url'] = response.meta.get('url')
        comment_num = re.findall(r'comments_count: (\d+)', response.text)
        if comment_num == []:
            item['comment_num'] = 0
        else:
            item['comment_num'] = comment_num[0]
        item['read_num'] = ''
        item['up_num'] = ''
        item['zhuanfa'] = ''
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        print(item['comment_num'], "==================")
        yield item


    def close(spider, reason):
        print(time.time() - ToutiaospiderSpider.s)
