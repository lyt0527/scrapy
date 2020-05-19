import requests
import re

headers={
    "accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8",
    "accept - encoding": "gzip, deflate, br",
    "accept - language": "zh - CN, zh;q = 0.9",
    "cache - control": "max - age = 0",
    "cookie": "__tasessionId = shecta5eg1574305718226; csrftoken = ba01108220d1b82b6b2d6499f84c3d74; tt_webid = 6761591501002262029",
    "upgrade - insecure - requests": "1"
}

tex = '''commentInfo: {
      groupId: '6734480260647109133',
      itemId: '6734480260647109133',
      comments_count: 0,
      ban_comment: 0
    }'''

comment_num = re.findall(r'comments_count: (\d+)', tex)[0]
print(comment_num)