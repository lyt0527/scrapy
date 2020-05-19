import csv
import json

import requests
from lxml import etree

# url = 'https://comment.sina.com.cn/page/info?version=1&format=json&channel=mp&newsid=7013977281-p1a210ccc100100khem&thread=1'
# url = 'https://comment.sina.com.cn/page/info?version=1&format=json&channel=mp&newsid=7166099740-1ab22011c00100otcu&thread=1'
# url = 'https://k.sina.com.cn/article_7166099740_1ab22011c00100otcu.html'

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}


data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\kandian1.csv'))
for i in list(data)[:5]:
    # print(i[0])
    split_url = i[0].split('_')
    url = 'https://comment.sina.com.cn/page/info?version=1&format=json&channel=mp&newsid=' + split_url[1] + '-' + split_url[2].split('.')[0]
    print(url)
    response = requests.get(url, headers=headers)
    result = json.loads(response.text)
    num = result['result']['count']['total']
    print(num)
