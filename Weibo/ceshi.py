import re

import requests
from lxml import etree
import json

# url = "https://weibo.com/tv/v/I5cKbblkH?fid=1034:4412404881156919"
# url = 'https://weibo.com/tv/v/I5cKbblkH'
url = 'https://weibo.com/ttarticle/p/show?id=2309404420377290866765'
headers={
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "weibo.com",
    'Cookie': 'SUB=_2AkMqg_Q7f8NxqwJRmfwRymjkZI12yAzEieKc3wXgJRMxHRl-yT83qmA7tRB6AQPa05DwzejUD1bu1Q0fddwBcSD8Oqkl; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhjuaJvs-Wj58OQy9-WyCTZ; YF-V5-G0=b1b8bc404aec69668ba2d36ae39dd980; _s_tentry=passport.weibo.com; Apache=6717664858370.38.1574927120218; SINAGLOBAL=6717664858370.38.1574927120218; ULV=1574927120227:1:1:1:6717664858370.38.1574927120218:; TC-Page-G0=2f200ef68557e15c78db077758a88e1f|1574927201|1574927190; YF-Page-G0=761bd8cde5c9cef594414e10263abf81|1574927810|1574927809; WBStorage=42212210b087ca50|undefined',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}

te = '<span class="num">阅读数：16411</span>'
te1 = '<span class="line S_line1" node-type="forward_btn_text">转发 3</span>'
te2 = '<span class="line S_line1" node-type="comment_btn_text">评论 1</span>'

response = requests.get(url, headers=headers)
res = etree.HTML(response.text)
# shoucang = response.xpath('//div[@class="WB_handle"]//li[1]//em[2]/text()')
# comment_num = response.xpath('//div[@class="WB_handle"]//li[2]//em[2]/text()')
# up_num = response.xpath('//div[@class="WB_handle"]//li[3]//em[2]/text()')
comment_num = re.findall(r'<span .*?>评论 (.*?)</span>', response.text)[0]
up_num = res.xpath('//span[@class="line S_line1"]//em/text()')[0]
zhuanfa = re.findall(r'<span .*?>转发 (.*?)</span', response.text)[0]
read_num = re.findall(r'<span class="num">阅读数：(.*?)</span', response.text)[0]
print(read_num, zhuanfa, comment_num, up_num)