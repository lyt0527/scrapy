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
    with open(r"./爱奇艺.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
        for i in data:
            res = requests.get(i[0], headers=headers)
            if res.status_code == 200:
                tvid = re.findall('param\[\'tvid\'] = "(.*?)";', res.text)[0]
                vid = re.findall('param\[\'vid\'] = "(.*?)";', res.text)[0]
                url1 = 'https://iface2.iqiyi.com/like/count?businessType=14&entityId={}&qyid={}'.format(tvid, vid)
                url2 = 'https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&business_type=17&content_id={}'.format(tvid)
                response = requests.get(url1, headers=headers)
                response1 = requests.get(url2, headers=headers)
                up_num = json.loads(response.text)['data']
                comment_num = json.loads(response1.text)['data']['totalCount']
                zhuanfa = ''
                read_num = ''
                print(i[0], up_num, comment_num)

                writer.writerow([i[0], i[1], read_num, up_num, comment_num, zhuanfa])
            else:
                writer.writerow([i[0], i[1], '', '', '', ''])


if __name__ == '__main__':
    db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
    cur = db.cursor()
    sql = "SELECT * FROM data1 WHERE Url LIKE '%www.iqiyi.com%';"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    main()