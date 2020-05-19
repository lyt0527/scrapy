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
   "User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
}

def main():
    with open(r"./58部落.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
        for i in data:
            res = requests.get(i[0], headers=headers)
            if res.status_code == 200:
                print(i[0])
                comment = re.findall(r'"replynum":"(.*?)"', res.text)
                comment_num = '' if comment == [] else comment[0]

                read = re.findall(r'"viewnum":"(.*?)"', res.text)
                read_num = '' if read == [] else read[0]

                up = re.findall(r'"thumbnum":(\d+)', res.text)
                up_num = '' if up == [] else up[0]

                zhuanfa = ''
                print(i[0], comment_num, read_num, up_num)
                writer.writerow([i[0], i[1], read_num, up_num, comment_num, zhuanfa])
            else:
                writer.writerow([i[0], i[1], '', '', '', ''])

if __name__ == '__main__':
    db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
    cur = db.cursor()
    sql = "SELECT * FROM data1 WHERE Url LIKE '%tribe.58.com%';"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    main()