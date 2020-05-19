import requests
from lxml import etree
import csv

url = "http://tieba.baidu.com/f?ie=utf-8&kw=%E4%BA%94%E8%8F%B1"
headers = {"User-Agent":"Mozilla/5.0"}

response = etree.HTML(requests.get(url, headers=headers).text)   
base = response.xpath('//div[@class="t_con cleafix"]')
#base = response.xpath('//*[@id="thread_top_list"]')

for each in base:

	items = {}  
	items["title"] = each.xpath('.//div[@class="threadlist_lz clearfix"]/div/a/text()')[0]
	items["author"] = each.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')
	if items["author"]:
		items["author"] = items["author"][0]
	else:
		items["author"] = "无"      
	items["content"] = each.xpath('.//div[@class="threadlist_text pull_left"]/div/text()')
	if items["content"]:
		items["content"] = items["content"][0]
	else:
		items["content"] = "无"  
	items["time"] = each.xpath('.//span[@class="threadlist_reply_date pull_right j_reply_data"]/text()')
	# if items["time"]:
	# 	items["time"] = items["time"][0]
	# else:
	# 	items["time"] = "无" 
	with open("tieba.csv", "a", newline="", encoding="utf8") as f:
		writer = csv.writer(f)
		writer.writerow([items["title"], items["author"], items["content"], items["time"]])
	# with open("tieba.txt", "a", encoding="utf8") as f:
	# 	f.write(items["title"])
	# 	f.write("\n")
# 		f.write(items["author"])
# 		f.write(items["content"])
# 		f.write(items["time"])
print("保存完成")
