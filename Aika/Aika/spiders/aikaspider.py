# -*- coding: utf-8 -*-
import csv
import re
import time
from Aika.items import AikaItem
import scrapy
import pymysql


class AikaspiderSpider(scrapy.Spider):
    name = 'aikaspider'
    # allowed_domains = ['https://aikahao.xcar.com.cn/']
    # start_urls = ['http://https://aikahao.xcar.com.cn//']

    s = time.time()
    with open("爱咖.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
        cur = db.cursor()
        sql = "SELECT * FROM data1 WHERE Url LIKE '%aikahao.xcar.com.cn/%';"
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = AikaItem()
        item['read_num'] = re.findall(r'<span class="browse_number">(\d+)', response.text)[0]
        item['url'] = response.meta.get('url')
        item['comment_num'] = ''
        item['MonitorName'] = response.meta.get('MonitorName')
        item['zhuanfa'] = ''
        item['up_num'] = ''
        print(item['url'], item['read_num'])
        yield item

    def close(spider, reason):
        print(time.time() - AikaspiderSpider.s)
