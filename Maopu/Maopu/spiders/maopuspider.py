# -*- coding: utf-8 -*-
import csv
import scrapy


class MaopuspiderSpider(scrapy.Spider):
    name = 'maopuspider'
    # allowed_domains = ['http://auto.mop.com/']
    # start_urls = ['http://http://auto.mop.com//']

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\maopu.csv'))
        for i in list(data)[:5]:
            yield scrapy.Request(url=i[0], meta={'url':i[0]}, callback=self.parse)

    def parse(self, response):
        comment_num = response.xpath('//div[@class="comment-area-title"]/span/i/text()').extract()
        url = response.meta.get('url')
        print(url, comment_num)
