# -*- coding: utf-8 -*-
import csv
import json
import re
import time

from Kuai.items import KuaiItem
import requests

import scrapy

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

class KuaispiderSpider(scrapy.Spider):
    name = 'kuaispider'
    # allowed_domains = ['https://www.360kuai.com/']
    # start_urls = ['http://https://www.360kuai.com//']

    s = time.time()
    with open("Kuai.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\kuai.csv'))
        for i in data:
            res = requests.get(i[0], headers=headers)
            num = re.findall(r'"rptid":"(.*?)"', res.text)
            if num != []:
                print(i[0], num)
                url = 'https://u.api.look.360.cn/comment/lists?page_key=' + num[0]
                yield scrapy.Request(url=url, meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse)

    def parse(self, response):
        item = KuaiItem()

        item['comment_num'] = json.loads(response.text)['data']['total']
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['read_num'] = ''
        item['up_num'] = ''
        item['zhuanfa'] = ''
        print(item['url'], item['MonitorName'], item['read_num'], item['up_num'], item['comment_num'], item['zhuanfa'])

        yield item

    def close(spider, reason):

        print(time.time() - KuaispiderSpider.s)