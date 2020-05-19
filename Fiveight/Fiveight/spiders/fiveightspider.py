# -*- coding: utf-8 -*-
import csv
import time
from Fiveight.items import FiveightItem
import scrapy


class FiveightspiderSpider(scrapy.Spider):
    name = 'fiveightspider'
    # allowed_domains = ['https://mtongzhen.58.com/']
    # start_urls = ['http://https://mtongzhen.58.com//']

    s = time.time()
    with open("58.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\fiveeight.csv'))
        for i in data:
            print(i[0])
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse)

    def parse(self, response):
        item = FiveightItem()
        zhuanfa = response.xpath('//div[@class="comment-infos_9df22a"]/div[3]/div/text()').extract()
        if zhuanfa == []:
            item['zhuanfa'] = 0
        else:
            item['zhuanfa'] = zhuanfa[0]
        up_num = response.xpath('//div[@class="comment-infos_9df22a"]/div[5]/text()').extract()
        if up_num == []:
            item['up_num'] = 0
        else:
            item['up_num'] = up_num[0]
        comment_num = response.xpath('//div[@class="comment-infos_9df22a"]/div[4]/text()').extract()
        if comment_num == []:
            item['comment_num'] = 0
        else:
            item['comment_num'] = comment_num[0]
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['read_num'] = ''
        yield item

    def close(spider, reason):
        print(time.time() - FiveightspiderSpider.s)
