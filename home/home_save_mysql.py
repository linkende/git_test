import requests
from bs4 import BeautifulSoup
import pymysql
import time


times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
# print(times)
# print(date)

#url="https://www.cdfgj.gov.cn/SCXX/Default.aspx"
url="https://www.cdfgj.gov.cn/SCXX/Default.aspx?action=ucEveryday"

html=requests.get(url,headers={'Connection':'close'})
htmls=html.text
list=[]
soup=BeautifulSoup(htmls,'html.parser')
big_table=soup.find('div',class_='rightContent')
tables=big_table.find_all('table',class_='blank')
for table in tables:
    trs=table.find_all('tr',bgcolor="#FFFFFF")
    for tr in trs:
        td=tr.find_all('td')
        for data in td:
            datas=data.text
            datals=datas.strip()
            #print(date)
            list.append(datals)

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='home', charset="utf8")
    cur = conn.cursor()
    sql = '''insert into homedb(date,goods_center_area_sum,goods_center_house_num,goods_center_house_area,
        goods_center_unhouse_area,goods_suburb_area_sum,goods_suburb_house_num,goods_suburb_house_area,
        goods_suburb_unhouse_area,goods_city_area_sum,goods_city_house_num,goods_city_house_area,
        goods_city_unhouse_area,ungoods_center_area_sum,ungoods_center_house_num,ungoods_center_house_area,
        ungoods_center_unhouse_area,ungoods_suburb_area_sum,ungoods_suburb_house_num,ungoods_suburb_house_area,
        ungoods_suburb_unhouse_area,ungoods_city_area_sum,ungoods_city_house_num,ungoods_city_house_area,
        ungoods_city_unhouse_area) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cur.execute(sql, [date, list[1], list[2], list[3], list[4], list[6], list[7], list[8], list[9], list[11], list[12],
                      list[13], list[14], list[16], list[17], list[18], list[19], list[21], list[22], list[23],
                      list[24], list[26], list[27], list[28], list[29]])
    conn.commit()
except:
    print("存库错误")

finally:
    print("存库完成")