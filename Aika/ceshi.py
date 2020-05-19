import requests
import re

url = 'https://aikahao.xcar.com.cn/item/147722.html'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
# a = '<span class="browse_number">2110浏览</span>'
num = re.findall(r'<span class="browse_number">(\d+)', response.text)
print(num)

