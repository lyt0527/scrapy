import requests
import csv
from lxml import etree

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
}
url='https://www.csdn.net'
response=etree.HTML(requests.get(url, headers=headers).text)

base = response.xpath('//div[@class="list_con"]')
for each in base:
    items={}

    
    items["title"] = each.xpath('./div[@class="title"]/h2/a/text()')[0].strip()
    items["author"] = each.xpath('./dl/dd[@class="name"]/a/text()')[0].strip()
    items["content"] = each.xpath('./div[@class="summary oneline"]/text()')[0]
    if items["content"]:
    	items["content"] = items["content"]
    else:
    	items["content"] = "无"
    items["read_num"] = each.xpath('./dl/div[@class="interactive floatR"]/dd[@class="read_num"]/a/span/text()')
    items["comments_num"] = each.xpath('./dl/div[@class="interactive floatR"]/dd[@class="common_num"]/a//text()')
    if items["comments_num"]:
        items["comments_num"] = items["comments_num"][0]
    else:
        items["comments_num"] = "无"

    print(items)

# read_num = str(items["read_num"][0]) + ":" + str(items["read_num"][1])
# with open("CSDN.csv", "a", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow([items["title"], items["author"], read_num, items["comments_num"]])
# print("保存完成")
