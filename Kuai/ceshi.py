import requests
import json
import re

# url = 'https://u.api.look.360.cn/comment/lists?page_key=75683f132cfbac23'
url = 'https://www.360kuai.com/9fbb37221291bd905'

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(response.status_code)
# num = re.findall(r'"rptid":"(.*?)"', response.text)[0]
#
# url = 'https://u.api.look.360.cn/comment/lists?page_key=' + num
# res = requests.get(url, headers=headers)
# num = json.loads(res.text)
# print(num['data']['total'])