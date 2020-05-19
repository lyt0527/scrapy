# -*- coding: utf-8 -*-
import scrapy


class UcspiderSpider(scrapy.Spider):
    name = 'ucspider'
    allowed_domains = ['http://a.mp.uc.cn/']
    start_urls = ['http://http://a.mp.uc.cn//']

    def parse(self, response):
        pass
