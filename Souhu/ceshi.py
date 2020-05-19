import re

import requests
from lxml import etree

headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "itssohu=true; BAIDU_SSP_lcr=https://www.baidu.com/link?url=AY9jjX4dWaxbM5nqPOzamV9_a_mp7Qi6YQhTu8-XfOa&wd=&eqid=ca1c815b00115a33000000065dd73419; reqtype=pc; gidinf=x099980109ee109f05a35b00f000e6ed95302581ad56; IPLOC=CN4502; SUV=191122090429K0VT; ipcncode=CN450200; sohu_user_ip=113.13.188.18; t=1574385851404; beans_new_turn=%7B%22news-article%22%3A10%2C%22auto-article%22%3A22%7D; beans_new_turn_1001800000=%7B%22auto-article%22%3A33%7D",
    "Host": "www.sohu.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
url = 'http://www.sohu.com/a/338852834_100208731'

response = etree.HTML(requests.get(url, headers=headers).text)
# data = json.loads(response.text)['outerCmtSum']
read_num = response.xpath('//div[@class="l read-num"]/text()')[0]
num = re.findall('\d+',read_num)
print(num[0])

