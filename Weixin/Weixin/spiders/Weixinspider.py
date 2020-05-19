# -*- coding: utf-8 -*-
import csv
import scrapy

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}


class WeixinspiderSpider(scrapy.Spider):
    name = 'Weixinspider'
    # allowed_domains = ['https://weixin.sogou.com']
    # start_urls = ['http://https://weixin.sogou.com/']

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\weixin.csv'))

        for i in data:
            yield scrapy.Request(url=i[0], callback=self.parse, dont_filter=True)

    def parse(self, response):
        pass
