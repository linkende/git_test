from bs4 import BeautifulSoup
import time
import requests
import re
import pymysql

list=[]
date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
list.append(date)

#总数量
url="https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.45.2a3424b099MVnZ&category=50025969&auction_source=0&city=%B3%C9%B6%BC&province=&st_param=-1&auction_start_seg=-1"
html=requests.get(url).text
soup=BeautifulSoup(html,'html.parser')
table=soup.find('div',class_='sf-wrap')
count=table.find('li',class_='block')
counts=count.find('em',class_='count')
#print(counts.text)
list.append(counts.text)
#正在进行的数量
url1='https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.101.43ef1b95p7j0d1&category=50025969&auction_source=0&city=%B3%C9%B6%BC&sorder=0&st_param=-1&auction_start_seg=-1'
html1=requests.get(url1).text
soup1=BeautifulSoup(html1,'html.parser')
table1=soup1.find('div',class_='sf-wrap')
ing=table1.find('li',class_='block')
ings=ing.find('em',class_='count')
#print(ings.text)
list.append(ings.text)
#即将开始的数量
url2='https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.101.7df31b95yaerbU&category=50025969&auction_source=0&city=%B3%C9%B6%BC&sorder=1&st_param=-1&auction_start_seg=-1'
html2=requests.get(url2).text
soup2=BeautifulSoup(html2,'html.parser')
table2=soup2.find('div',class_='sf-wrap')
begin=table2.find('li',class_='block')
begins=begin.find('em',class_='count')
#print(begins.text)
list.append(begins.text)

#链家二手总数据
url2='https://cd.lianjia.com/ershoufang/co32/'
hearder={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
html2=requests.get(url2,headers=hearder)
html2.encoding='utf-8'
htmls2=html2.text
p1=r"(?<=共找到<span>).+?(?=</span>套成都二手房)"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,htmls2)
lianjia=matcher1.group(0).strip()
#print(lianjia)
list.append(lianjia)

#print(list)

#保存数据库
try:
    conn=pymysql.connect(host='127.0.0.1', user='root', password='root', db='home', charset="utf8")
    cur=conn.cursor()
    sql='''insert into taobao_auction_house(date,count,ing,begin,lianjia) values(%s,%s,%s,%s,%s)'''
    cur.execute(sql,[list[0],list[1],list[2],list[3],list[4]])
    conn.commit()
except:
    print("存库错误")
finally:
    print("存库完成")