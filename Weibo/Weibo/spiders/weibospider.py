# -*- coding: utf-8 -*-
import csv
import re
import time
import pymysql
import scrapy
from Weibo.items import WeiboItem

class WeibospiderSpider(scrapy.Spider):
    name = 'weibospider'
    # allowed_domains = ['weibo.com']
    # start_urls = ['http://weibo.com/']

    s = time.time()
    with open("weibo.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):

        # db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
        # cur = db.cursor()
        # sql = 'select * from weibo WHERE url NOT LIKE "%http://weibo.com/tt%";'
        # cur.execute(sql)
        # data = cur.fetchall()
        # db.close()
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\weibo1.csv'))

        # 除tt
        for i in data:
            url = "https://weibo.com/tv/v/" + i[0].split('/')[-1]
            print(url)
            yield scrapy.Request(url=url, meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse, dont_filter=True)

        # for i in data:
        #     # url = 'https://weibo.com/ttarticle/p/show?id=2309404436912000598034'
        #     yield scrapy.Request(url=i[0], meta={'url': i[0], 'MonitorName': i[1]}, callback=self.parse, dont_filter=True)



    def parse(self, response):
        item = WeiboItem()
        item['zhuanfa'] = response.xpath('//div[@class="WB_handle"]//li[1]//em[2]/text()').extract()[0]
        item['comment_num'] = response.xpath('//div[@class="WB_handle"]//li[2]//em[2]/text()').extract()[0]
        item['up_num'] = response.xpath('//div[@class="WB_handle"]//li[3]//em[2]/text()').extract()[0]
        if item['zhuanfa'] == '转发':
            item['zhuanfa'] = 0
        else:
            item['zhuanfa'] = item['zhuanfa']

        if item['comment_num'] == '评论':
            item['comment_num'] = 0
        else:
            item['comment_num'] = item['comment_num']

        if item['up_num'] == '赞':
            item['up_num'] = 0
        else:
            item['up_num'] = item['up_num']

        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['read_num'] = ''
        print(item['zhuanfa'], item['comment_num'], item['up_num'], item['url'], item['MonitorName'], item['read_num'])
        yield item


        # comment_num = re.findall(r'<span .*?>评论 (.*?)</span>', response.text)
        # if comment_num == []:
        #     item['comment_num'] = 0
        # else:
        #     item['comment_num'] = comment_num[0]
        #
        # up_num = response.xpath('//span[@class="line S_line1"]//em/text()')
        # if up_num == []:
        #     item['up_num'] = 0
        # else:
        #     item['up_num'] = up_num[0]
        #
        # zhuanfa = re.findall(r'<span .*?>转发 (.*?)</span', response.text)
        # if zhuanfa == []:
        #     item['zhuanfa'] = 0
        # else:
        #     item['zhuanfa'] = zhuanfa[0]
        #
        # read_num = re.findall(r'<span class="num">阅读数：(.*?)</span', response.text)
        # if read_num == []:
        #     item['read_num'] = 0
        # else:
        #     item['read_num'] = read_num[0]
        # item['url'] = response.meta.get('url')
        # item['MonitorName'] = response.meta.get('MonitorName')
        # print(item['read_num'], item['zhuanfa'], item['comment_num'], item['up_num'])
        # yield item

    def close(spider, reason):
        print(time.time() - WeibospiderSpider.s)


