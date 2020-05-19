import requests
from lxml import etree
import re
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

url = 'http://v.qq.com/x/page/t0923ntelmf.html'
#切割
target_url = 'https://ncgi.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid={}'.format(re.split('\/|\.', url)[-2])
print(target_url)
#获取target_id
response = requests.get(target_url, headers=headers)
target_id = re.findall(r'"comment_id":"(.*?)"', response.text)[0]
print(target_id)
#获取评论数
comment_url = 'https://video.coral.qq.com/article/{}/commentnum?callback=_article{}ommentnum'.format(target_id, target_id)
res = requests.get(comment_url, headers=headers)
read_num = re.findall(r'"commentnum":"(.*?)"', res.text)[0]
print(read_num)

