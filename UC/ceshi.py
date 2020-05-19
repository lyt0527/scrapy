import requests
import re
from lxml import etree

headers={
    'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

url = 'http://blog.sina.com.cn/s/blog_677256230102yxzy.html'

# te = '<span id="r_677256230102yxzy" class="SG_txtb">(22)</span>'
response = etree.HTML(requests.get(url, headers=headers).text)
# comment_num = response.xpath('//div[@class="articalInfo"]//span[1]/text()')
comment_num = re.findall(r'<span id="r_677256230102yxzy" class="SG_txtb">(.*?)</span>', response.text)
print(comment_num)