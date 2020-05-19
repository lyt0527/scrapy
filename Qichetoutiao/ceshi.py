import re




te = '<span style="color:#17abc1">23755</span>'

text = re.findall(r'<span style="color:#17abc1">(.*?)</span>', te)[0]
print(text)