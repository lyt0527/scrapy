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

header = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'


def main():
    with open(r"./百度知道.csv", "a", newline="") as f:
        writer = csv.writer(f)
    #     writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
        j = 0
        for i in list(data)[1400:]:
            j += 1
            headers = {
                "User-Agent": header,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "BAIDUID=AD4B7BDD088E096F130D5102AA7D1D43:FG=1; BIDUPSID=AD4B7BDD088E096F130D5102AA7D1D43; PSTM=1575341501; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=6; BDUSS=WlJUGwtTFdhUWVrQXdxWFYtRFRDUkdCZHJpdUdobWVieHRUWE5WNnNOQnRxUTVlSVFBQUFBJCQAAAAAAAAAAAEAAACpuM40t8nP6ExUOTYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG0c511tHOddL; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1422_21124_30210_29700_26350; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1575334202,1575420425,1575424102,1575427226; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1575427226",
                "Referer": i[0]
            }
            res = requests.get(i[0], headers=headers)
            time.sleep(1)
            if res.status_code == 200:
                comment_num = re.findall(r'<span class="question-all-answers-title" .*?>(\d+).*?', res.text)
                comment_num = '' if comment_num == [] else comment_num[0]

                url = 'https://zhidao.baidu.com/api/qbpv?q={}'.format(re.split(r'\/|\.', i[0])[-2])
                response = requests.get(url, headers=headers)
                read_num = response.text
                print(i[0], read_num, comment_num, j)
                writer.writerow([i[0], i[1], read_num, '', comment_num, ''])
            else:
                print("====")
                writer.writerow([i[0], i[1], '', '', '', ''])



if __name__ == '__main__':
    data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\zhidao.csv'))
    main()
