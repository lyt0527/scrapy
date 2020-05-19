# -*- coding: utf-8 -*-
import csv
import re
import time
import requests
from lxml import etree
import scrapy
import json
from Souhu.items import SouhuItem

class SouhuspiderSpider(scrapy.Spider):
    name = 'souhuspider'
    # allowed_domains = ['www.sohu.com']
    # start_urls = ['http://www.sohu.com/']

    s = time.time()
    with open("搜狐.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):

        # db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
        # cur = db.cursor()
        # sql = 'SELECT * FROM sohu;'
        # cur.execute(sql)
        # urls = cur.fetchall()
        # cur.close()
        # print(urls)
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\sohu.csv'))
        j = 0
        for i in data:
            j += 1
            # print(i[0])
            #动态加载地址
            url = 'http://db.auto.sohu.com/api/comment/list?newsId=' + i[0].split('/')[4].split('_')[0] + '&pageSize=20&pageNo=1&businessType=article'
            print(j, "=============")
            yield scrapy.Request(url=url, meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = SouhuItem()

        item['url'] = response.meta.get('url')
        item['comment_num'] = json.loads(response.text)["data"]["outerCmtSum"]
        req = etree.HTML(requests.get(item['url']).text)
        num = req.xpath('//div[@class="l read-num"]/text()')
        print(num, '-------------')
        if num == []:
            print('进来.................', item['url'], response)
            item['read_num'] = ''
        else:
            item['read_num'] = re.findall('\d+', num[0])[0]
        item['up_num'] = ''
        item['zhuanfa'] = ''
        item['MonitorName'] = response.meta.get('MonitorName')
        print('评论数：', item['comment_num'], '阅读数：', item['read_num'])
        yield item

    def close(spider, reason):
        print(time.time() - SouhuspiderSpider.s)

