# -*- coding: utf-8 -*-
import csv
import re
import time

from Qichetoutiao.items import QichetoutiaoItem
import scrapy


class QichespiderSpider(scrapy.Spider):
    name = 'qichespider'
    # allowed_domains = ['https://www.qctt.cn/']
    # start_urls = ['http://https://www.qctt.cn//']

    s = time.time()
    with open("汽车头条.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\qichetoutiao.csv'))
        for i in data:
            if i[0][20:21] == 'n':
                yield scrapy.Request(url=i[0], meta={'url': i[0], 'MonitorName': i[1]}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = QichetoutiaoItem()
        read_num = re.findall(r'<span style="color:#17abc1">(.*?)</span>', response.text)
        if read_num == []:
            item['read_num'] = 0
        else:
            item['read_num'] = read_num[0]
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['up_num'] = ''
        item['comment_num'] = ''
        item['zhuanfa'] = ''
        print(item['read_num'], item['url'])
        yield item

    def close(spider, reason):
        print(time.time() - QichespiderSpider.s)