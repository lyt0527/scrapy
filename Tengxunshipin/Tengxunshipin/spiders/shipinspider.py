# -*- coding: utf-8 -*-
import csv
import re
import time

import requests
import pymysql
import scrapy
from Tengxunshipin.items import TengxunshipinItem

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

class ShipinspiderSpider(scrapy.Spider):
    name = 'shipinspider'
    # allowed_domains = ['https://v.qq.com/']
    # start_urls = ['http://https://v.qq.com//']

    s = time.time()
    with open("腾讯视频.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
    def start_requests(self):
        db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
        cur = db.cursor()
        sql = 'SELECT * FROM data1 WHERE Url LIKE "%//v.qq.com%";'
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        for i in data:
            print(i[0])
            yield scrapy.Request(url=i[0], meta={'url':i[0], 'MonitorName':i[1]}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = TengxunshipinItem()
        item['url'] = response.meta.get('url')
        # 切割
        target_url = 'https://ncgi.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid={}'.format(re.split('\/|\.', item['url'])[-2])
        req = requests.get(target_url, headers=headers)
        #获取target_id
        target_id = re.findall(r'"comment_id":"(.*?)"', req.text)[0]
        comment_url = 'https://video.coral.qq.com/article/{}/commentnum?callback=_article{}ommentnum'.format(target_id,target_id)
        res = requests.get(comment_url, headers=headers)
        item['comment_num'] = re.findall(r'"commentnum":"(.*?)"', res.text)[0]
        item['read_num'] = response.xpath('//span[@class="icon_text"]/em/text()').extract()[0]
        up_num = response.xpath('//div[@class="video_info"]//a[@class="btn_book"]/span[2]/text()').extract()
        if up_num == []:
            item['up_num'] = 0
        else:
            item['up_num'] = up_num[0]
        item['MonitorName'] = response.meta.get('MonitorName')
        item['zhuanfa'] = ''
        print(item['url'], item['comment_num'], item['read_num'], item['up_num'])

        yield item


    def close(spider, reason):
        print(time.time() - ShipinspiderSpider.s)