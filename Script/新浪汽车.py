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
import json
import pymysql

headers={
   'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Cookie': 'SINAGLOBAL=222.84.126.67_1575018437.197652; UOR=news.sina.com.cn,news.sina.com.cn,; Apache=222.84.126.73_1575265093.139069; ULV=1575265103320:2:2:2:222.84.126.73_1575265093.139069:1575265091199; SCF=AhCXv06Ub8hblVML9MJqbSdg3j6eXWWPnX53toTZHi_SRbI1lsqPbWLi3l1xJFlH2z7RqM_y5XbBZWGCimSncm0.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWJgo18YGLl.VUAv..RSpUQ5NHD95Q01KB0e02XeKz7Ws4Dqcjci--Xi-zRi-2Ei--Xi-zRiKy2i--Xi-zRiKyFi--NiKLWiKnXi--ciK.Ri-8si--Xi-i2i-27; ALF=1606801136; UM_distinctid=16ec51e91684cf-0857dd58119869-3a3a5d0c-15f900-16ec51e9169219; U_TRS1=00000051.c25b61c5.5de4a379.2e85a1f8; U_TRS2=00000051.c26861c5.5de4a379.9bbcd1a0; lxlrttp=1572512346; SessionID=8k48r47o27mlslc2n534gikoo1; SINABLOGNUINFO=1000000000.3b9aca00.v5sinalogtest; __gads=Test; SUB=_2A25w4N3PDeRhGeVH71ES8SrNyTyIHXVTlEgHrDV_PUJbm9BeLXLtkW9NT0ZAXSJap5_WpOjUsbOOeZRTxRzWYXnr',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-encoding': 'gzip, deflate, br',
    'Accept-language': 'zh-CN,zh;q=0.9',
    'Aache-control': 'max-age=0',
}
def main():
    with open(r"./新浪汽车.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
        for i in data:
            response = requests.get(i[0], headers=headers)
            news_id = re.findall(r"newsid: '(.*?)'", response.text)
            if news_id != []:
                url = 'http://comment.sina.com.cn/page/info?channel=qc&newsid={}'.format(news_id[0])
                res = requests.get(url, headers=headers)
                comment_num = json.loads(res.text)['result']
                if 'count' in comment_num:
                    print(111)
                    comment_num = comment_num['count']['total']
                    read_num = ''
                    up_num = ''
                    zhuanfa = ''
                    print(i[0], comment_num)
                    writer.writerow([i[0], i[1], read_num, up_num, comment_num, zhuanfa])
                else:
                    writer.writerow([i[0], i[1], '', '', '', ''])
            else:
                writer.writerow([i[0], i[1], '', '', '', ''])

if __name__ == '__main__':
    db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
    cur = db.cursor()
    sql = "SELECT * FROM data1 WHERE Url LIKE '%http://auto.sina.com.cn%';"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    main()