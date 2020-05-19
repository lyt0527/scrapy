import csv
import json
import requests
from lxml import etree

url = 'https://mtongzhen.58.com/tzbl/fresh/detail/0/94226209.shtml'

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}


response = etree.HTML(requests.get(url, headers=headers).text)
num = response.xpath('//div[@class="comment-infos_9df22a"]/div[3]/div/text()')
print(num, '[]')
