import requests,time,pymysql
from bs4 import BeautifulSoup
from pyecharts import Line

url= 'https://www.cdfgj.gov.cn/SCXX/Default.aspx?action=ucEveryday'
htm=requests.get(url)
htm.encoding='utf-8'
html=htm.text
soup=BeautifulSoup(html,'html.parser')
#print(soup)
list=[]
date=time.strftime('%Y-%m-%d',time.localtime(time.time()))

table=soup.find('div',class_='rightContent')
#print(table)
tables=table.find_all('table',class_='blank')
for table in tables:
    trs=table.find_all('tr',bgcolor="#FFFFFF")
    for tr in trs:
        td=tr.find_all('td')
        for data in td:
            datas=data.text
            datals=datas.strip()
            #print(date)
            list.append(datals)
#print(list)

new_center=list[2]
new_uncenter=list[7]
old_center=list[17]
old_uncenter=list[22]
#print(new_center,new_uncenter,old_center,old_uncenter)

try:
    conn=pymysql.connect(host='127.0.0.1', user='root', password='root', db='home', charset="utf8")
    cur=conn.cursor()
    sql='''insert into fangchan_data(date,new_center,new_uncenter,old_center,old_uncenter) values(%s,%s,%s,%s,%s)'''
    cur.execute(sql,[date,new_center,new_uncenter,old_center,old_uncenter])
    conn.commit()
except:
    print("存库错误")

finally:
    print("存库完成")

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='home', charset="utf8")
cur = conn.cursor()
sql = '''select * from fangchan_data'''
cur.execute(sql)
conn.commit()
data=cur.fetchall()

list_date=[]
list_new_center=[]
list_new_uncenter=[]
list_old_center=[]
list_old_uncenter=[]

for row in data:
    date=row[0]
    new_center=row[1]
    new_uncenter=row[2]
    old_center=row[3]
    old_uncenter=row[4]
    list_date.append(date)
    list_new_center.append(new_center)
    list_new_uncenter.append(new_uncenter)
    list_old_center.append(old_center)
    list_old_uncenter.append(old_uncenter)

line=Line("走势图")
line.add("市中心新",list_date,list_new_center)
line.add("市中心旧",list_date,list_old_center)
line.add("郊区新",list_date,list_new_uncenter)
line.add("郊区旧",list_date,list_old_uncenter)
line.show_config()
line.render()
