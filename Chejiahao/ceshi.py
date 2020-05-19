import csv

import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

# data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\资料\chejiahao.csv'))
# for i in list(data)[:5]:
#     if i[0][18:19] == 'm':
#         i[0] = 'https://chejiahao.'+ i[0][20:]
#         # res = requests.get(url, headers)
#     print(i[0])
# url = url.strip('.m')
# print(url)
url = 'https://chejiahao.autohome.com.cn/info/4593907'
res = requests.get(url, headers)
# tex1 = '<small data-starcount="0">3</small>'
# tex2 = '<small id="ReplyCount">3</small>'
num = re.findall(r'<span>(.*?)&', res.text)[0]
# num1 = re.findall(r'<small data-starcount="0">(\d+)</small>', tex1)[0]
# num2 = re.findall(r'<small id="ReplyCount">(\d+)</small>', tex2)[0]
print(num)