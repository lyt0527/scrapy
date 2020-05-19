# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:28:29 2019

@author: liuyuntao
"""
#
#import requests
#import time
#import csv
#import re
#import aiohttp
#import asyncio


#url = "http://tieba.baidu.com/p/6162708782?pid=127414957486&cid=0#127414957486"
#data = csv.reader(open(r"C:\Users\liuyuntao\Desktop\贴吧.csv"))

#headers={
#    "User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
#}

import aiohttp
import asyncio

async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.text()
            print(response)
        
if __name__ == "__main__":
    url = "http://www.baidu.com"
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_data(url))

#with open(r"C:\Users\liuyuntao\Desktop\data.csv", "w+", newline="", encoding="utf-8") as f:
#    writer = csv.writer(f)
#    writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
#    for i in data:
#        req = requests.get(i[0], headers=headers)
#        time.sleep(15)
#        number = re.findall(r'<span class="red" style="margin-right:3px">(.+?)</span>', req.text)
#        if number == []:
#            writer.writerow([i[0], i[1], "", "", "", ""])
#            print("评论数：", "")
#        else:
#            writer.writerow([i[0], i[1], "", "", number[0], ""])
#            print("评论数：", number[0])