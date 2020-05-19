# -*- coding: utf-8 -*-
import csv
import json
import time
from kandian.items import KandianItem
import scrapy


class KandianspiderSpider(scrapy.Spider):
    name = 'kandianspider'
    # allowed_domains = ['https://k.sina.com.cn/']
    # start_urls = ['http://https://k.sina.com.cn//']

    s = time.time()
    with open("kandian.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\kandian1.csv'))
        for i in data:
            split_url = i[0].split('_')
            url = 'https://comment.sina.com.cn/page/info?version=1&format=json&channel=mp&newsid=' + split_url[1] + '-' + split_url[2].split('.')[0]
            print(i[0], url)
            yield scrapy.Request(url=url, meta={'url': i[0], 'MonitorName':i[1]}, callback=self.parse)

    def parse(self, response):
        try:
            item = KandianItem()
            result = json.loads(response.text)
            item['comment_num'] = result['result']['count']['total']
            item['url'] = response.meta.get('url')
            item['MonitorName'] = response.meta.get('MonitorName')
            item['read_num'] = ''
            item['zhuanfa'] = ''
            item['up_num'] = ''
            yield item

        except:
            url = response.meta.get('url')
            print(url, "===============")

    def close(spider, reason):
        print(time.time() - KandianspiderSpider.s)

