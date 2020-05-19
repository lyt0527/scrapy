# -*- coding: utf-8 -*-
import csv
import scrapy
import re
from baidu.items import BaiduItem
import time
# def get_urls():
#     urls = []
#     data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\贴吧.csv'))
#     for i in list(data)[:3]:
#         urls.append(i[0])
#     print(urls, "================")
#     return urls

class TiebaspiderSpider(scrapy.Spider):
    name = 'tiebaspider'
    # allowed_domains = ['tieba.baidu.com']
    # start_urls = ['http://tieba.baidu.com/']
    # start_urls = get_urls()

    # def parse(self, response):
        # number = response.xpath('//div[@class="p_thread thread_theme_5"]//li[@class="l_reply_num"]/span[1]/text()').extract()
        # print(number, "000000000000000000")

    #c重写start_requests
    s = time.time()
    with open("data.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\tieba.csv'))
        j = 1
        for i in data:
            print(j, i)
            j += 1
            yield  scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse)

    def parse(self, response):
        try:
            print("进入try..........................")
            item = BaiduItem()
            item['comment_num'] = re.findall(r'<span class="red" style="margin-right:3px">(.+?)</span>', response.text)
            item['read_num'] = ''
            item['up_num'] = ''
            item['zhuanfa'] = ''
            item['url'] = response.meta.get('url')
            item["MonitorName"] = response.meta.get('MonitorName')
            if item['comment_num'] == []:
                item['comment_num'] = ''
                print("---------------------------------")
            else:
                item['comment_num'] = item['comment_num'][0]
                print(item["url"], item["MonitorName"], item['comment_num'], "====================")
        except:
            print("进入except.......................")
        yield item

    def close(spider, reason):
        print(time.time() - TiebaspiderSpider.s)