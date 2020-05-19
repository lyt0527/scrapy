# -*- coding: utf-8 -*-
import json
import re

import scrapy
import csv
import requests
from Tengxun.items import TengxunItem

headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "pgv_info=ssid=s2620233524; pgv_pvid=3303719844; ts_uid=3522976910; pgv_pvi=1040208896; pgv_si=s270492672; _qpsvr_localtk=0.6418003882126724; ptisp=ctc; RK=53pEHrr4G7; ptcz=3fc4038e1b68a27d42fab6771d7833416757670ba89bf7f369a9b262aff326f0; qq_openid=C202D65E40CC9A487C2B8B6B85D74018; qq_access_token=02ABB0C35C67D27F839F4BBAE9EE5224; qq_client_id=101487368; pac_uid=3_C202D65E40CC9A487C2B8B6B85D74018; ts_refer=graph.qq.com/oauth2.0/show; uid=189841333; ts_last=new.qq.com/rain/a/20190903A08OEQ; ad_play_index=75",
    "if-none-match": "W/'1be1-nhtRk9um0PcFFEIATYTPo8lAYko'",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

class TengxunspiderSpider(scrapy.Spider):
    name = 'Tengxunspider'
    # allowed_domains = ['https://new.qq.com/']
    # start_urls = ['http://https://new.qq.com//']

    with open("Tengxun.csv", "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])

    def start_requests(self):
        data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\tengxun.csv'))
        for i in data:
            print(i)
            res = requests.get(i[0], headers=headers)
            comment_id = re.findall(r'"comment_id": "(.*?)"', res.text)
            if comment_id != []:
                # print(comment_id)
                url = 'https://coral.qq.com/article/' + comment_id[0] + '/commentnum'
                # print(url)
                yield scrapy.Request(url=url, meta={'url': i[0], 'MonitorName': i[1]}, callback=self.parse, dont_filter=True)


    def parse(self, response):
        item = TengxunItem()

        item['comment_num'] = json.loads(response.text)['data']['commentnum']
        item['url'] = response.meta.get('url')
        item['MonitorName'] = response.meta.get('MonitorName')
        item['read_num'] = ''
        item['up_num'] = ''
        item['zhuanfa'] = ''
        print(item['url'], item['MonitorName'], item['read_num'], item['up_num'], item['comment_num'], item['zhuanfa'])

        yield item
