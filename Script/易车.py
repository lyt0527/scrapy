# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:51:30 2019

@author: liuyuntao
"""
import requests
from lxml import etree
import csv
import re
import time
import pymysql

headers={
   "User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    'Cookie': 'XCWEBLOG_testcookie=yes; b_8695=1; b_2922=2; b_4450=1; b_3087=1; b_4430=1; UserGuid=a868c1dc-6420-4e06-b047-7ca04ec22bf3; b_6049=2; CIGDCID=cce748b37be24ea7908b20ff51e3ad0f-yiche; locatecity=450200; bitauto_ipregion=222.84.126.74%3a%e5%b9%bf%e8%a5%bf%e5%a3%ae%e6%97%8f%e8%87%aa%e6%b2%bb%e5%8c%ba%e6%9f%b3%e5%b7%9e%e5%b8%82%3b602%2c%e6%9f%b3%e5%b7%9e%e5%b8%82%2cliuzhou; Hm_lvt_1d0536730fc65a83bdfdd84c77395d80=1575000946; Hm_lvt_f69697b4b54908f4b7129fa24bbfdbbe=1575000947; player_pos=1046.5|50; Hm_lpvt_1d0536730fc65a83bdfdd84c77395d80=1575001378; Hm_lpvt_f69697b4b54908f4b7129fa24bbfdbbe=1575001379',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}
def main():
    with open(r"./易车.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
        for i in data:
            print(i)
            base_url = i[0][:9] + '.m.' + i[0][10:]
            response = etree.HTML(requests.get(base_url, headers=headers).text)
            read_num = response.xpath('//i[@class="ico-play"]/text()')
            if read_num == []:
                read_num = ''
            else:
                read_num = read_num[0]
            comment_num = response.xpath('//em[@id="videoSupport"]/text()')
            if comment_num == []:
                comment_num = ''
            else:
                comment_num = comment_num[0]
            up_num = response.xpath('//li[@class="dz-ico"]//p/em/text()')
            if up_num == []:
                up_num = ''
            else:
                up_num = up_num[0]
            url = i[0]
            MonitorName = i[1]
            zhuanfa = ''
            print(url, read_num, comment_num, up_num)
            writer.writerow([url, MonitorName, read_num, up_num, comment_num, zhuanfa])

if __name__ == '__main__':
    db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
    cur = db.cursor()
    sql = "select * from data1 WHERE Url LIKE '%http://vc.yiche.com%';"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    main()