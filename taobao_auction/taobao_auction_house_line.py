from pyecharts import Line
import pymysql

conn=pymysql.connect(host='127.0.0.1', user='root', password='root', db='home', charset="utf8")
cur=conn.cursor()
sql='''select * from taobao_auction_house'''
cur.execute(sql)
conn.commit()
data=cur.fetchall()



list_date=[]
list_count=[]
list_ing=[]
list_begin=[]
list_lianjia=[]

for row in data:
    date=row[0]
    count=row[1]
    ing=row[2]
    begin=row[3]
    lianjia=row[4]
    list_date.append(date)
    list_count.append(count)
    list_ing.append(ing)
    list_begin.append(begin)
    list_lianjia.append(lianjia)

line=Line('法拍走势图')
line.add('总数量',list_date,list_count)
#line.add('正在进行',list_date,list_ing)
#line.add('即将开始',list_date,list_begin)
line.add('链家二手',list_date,list_lianjia)
line.show_config()
line.render()
