import re

import requests
from lxml import etree

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
url = 'http://dy.163.com/v2/article/detail/EOA7FNU60527AQ4N.html'

response = etree.HTML(requests.get(url, headers=headers).text)
# data = json.loads(response.text)['outerCmtSum']
read_num = response.xpath('//span[@class="num"]/a/text()')
print(read_num)

