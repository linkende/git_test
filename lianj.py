import requests
import re

url='https://cd.lianjia.com/ershoufang/co32/'
hearder={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
html=requests.get(url,headers=hearder)
html.encoding='utf-8'
htmls=html.text
p1=r"(?<=共找到<span>).+?(?=</span>套成都二手房)"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,htmls)
lianjia=matcher1.group(0).strip()
print(lianjia)