import csv
import re
import requests
import json


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

data = csv.reader(open(r'C:\Users\liuyuntao\Desktop\weixin.csv'))

count = 0
count1 = 0
for i in data:
    req = requests.get(i[0], headers=headers)
    if req.status_code != 200:
        count += 1
        print(count)
    else:
        count1 += 1
print("为请求成功有：", count, "请求成功有：", count1, "====")

# comment_id = re.findall(r'"comment_id": "(.*?)"', req.text)[0]
# url2 = 'https://coral.qq.com/article/' + comment_id + '/commentnum'
# print(url2)
# res = requests.get(url2, headers=headers)
# response = json.loads(res.text)['data']['commentnum']
# print(response)