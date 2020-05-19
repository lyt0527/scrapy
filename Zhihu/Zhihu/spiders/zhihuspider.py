# -*- coding: utf-8 -*-
import csv
import time
import re
import scrapy
import pymysql
from Zhihu.items import ZhihuItem



class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuspider'
    # allowed_domains = ['https://www.zhihu.com/']
    # start_urls = ['http://https://www.zhihu.com//']

    s = time.time()
    # with open("知乎.csv", "a+", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
        cur = db.cursor()
        sql = 'select * from zhihu1;'
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        for i in data:
            print(i[0])
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse)


    def parse(self, response):
        item = ZhihuItem()
        # item['up_num'] = re.findall(r'"voteupCount":(\d+)', response.text)[0]
        # item['zhuanfa'] = re.findall(r'"voting":(\d+)', response.text)[0]
        # item['comment_num'] = re.findall(r'"commentCount":(\d+)', response.text)[0]
        # item['url'] = response.meta.get('url')
        # item['MonitorName'] = response.meta.get('MonitorName')
        # item['read_num'] = ''
        # print(item['up_num'], item['comment_num'], item['zhuanfa'], item['url'])
        # yield item

        item['comment_num'] = re.findall(r'"commentCount":(\d+)', response.text)[0]
        item['read_num'] = re.findall(r'"visitCount":(\d+)', response.text)[0]
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['zhuanfa'] = ''
        item['up_num'] = ''
        print(item['read_num'], item['comment_num'], item['url'])
        yield item

    def close(spider, reason):
        print(time.time() - ZhihuspiderSpider.s)