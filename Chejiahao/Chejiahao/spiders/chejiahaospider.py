# -*- coding: utf-8 -*-
import csv
import re
import time

from Chejiahao.items import ChejiahaoItem
import scrapy


class ChejiahaospiderSpider(scrapy.Spider):
    name = 'chejiahaospider'
    # allowed_domains = ['https://chejiahao.autohome.com.cn']
    # start_urls = ['http://https://chejiahao.autohome.com.cn/']

    s = time.time()
    with open("chejiahao.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\chejiahao.csv'))
        for i in data:
            if i[0][18:19] == 'm':
                i[0] = 'https://chejiahao.' + i[0][20:]
            print(i[0])
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = ChejiahaoItem()
        item['comment_num'] = re.findall(r'<small id="ReplyCount">(.*?)</small>', response.text)[0]
        item['read_num'] = re.findall(r'<span>(.*?)&', response.text)[0]
        item['up_num'] = re.findall(r'<small data-starcount="0">(.*?)</small>', response.text)[0]
        item['zhuanfa'] = ''
        item['MonitorName'] = response.meta.get('MonitorName')
        item['url'] = response.meta.get('url')
        print(item['comment_num'], item['read_num'], item['up_num'])

        yield item

    def close(spider, reason):
        print(time.time() - ChejiahaospiderSpider.s)




