# -*- coding: utf-8 -*-
import csv
import time

from Xinlang.items import XinlangItem
import scrapy


class XinlangspiderSpider(scrapy.Spider):
    name = 'xinlangspider'
    # allowed_domains = ['https://auto.sina.cn/']
    # start_urls = ['http://https://auto.sina.cn//']
    s = time.time()

    # with open("手机新浪.csv", "a+", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\shoujixinlang1.csv'))
        for i in data:
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse)

    def parse(self, response):
        item = XinlangItem()
        num = response.xpath('//section[@class="foot_comment one"]//span/text()').extract()
        if num == []:
            item['comment_num'] = 0
        else:
            item['comment_num'] = num[0]
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['read_num'] = ''
        item['up_num'] = ''
        item['zhuanfa'] = ''
        print(item['comment_num'])
        yield item

    def close(spider, reason):
        print(time.time() - XinlangspiderSpider.s)
