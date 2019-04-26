from pyecharts import Line
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='home', charset="utf8")
cur = conn.cursor()
sql = '''select * from homedb'''
cur.execute(sql)
conn.commit()
data=cur.fetchall()

list_date=[]
list_goods_center_area_sum=[]
list_goods_center_house_num=[]
list_goods_center_house_area=[]
list_goods_center_unhouse_area=[]
list_goods_suburb_area_sum=[]
list_goods_suburb_house_num=[]
list_goods_suburb_house_area=[]
list_goods_suburb_unhouse_are=[]
list_goods_city_area_sum=[]
list_goods_city_house_num=[]
list_goods_city_house_area=[]
list_goods_city_unhouse_area=[]
list_ungoods_center_area_sum=[]
list_ungoods_center_house_num=[]
list_ungoods_center_house_area=[]
list_ungoods_center_unhouse_area=[]
list_ungoods_suburb_area_sum=[]
list_ungoods_suburb_house_num=[]
list_ungoods_suburb_house_area=[]
list_ungoods_suburb_unhouse_area=[]
list_ungoods_city_area_sum=[]
list_ungoods_city_house_num=[]
list_ungoods_city_house_area=[]
list_ungoods_city_unhouse_area=[]

for row in data:
    date=row[0]
    goods_center_area_sum= row[1]
    goods_center_house_num = row[2]
    goods_center_house_area= row[3]
    goods_center_unhouse_area =row[4]
    goods_suburb_area_sum= row[5]
    goods_suburb_house_num = row[6]
    goods_suburb_house_area= row[7]
    goods_suburb_unhouse_area= row[8]
    goods_city_area_sum= row[9]
    goods_city_house_num = row[10]
    goods_city_house_area= row[11]
    goods_city_unhouse_area= row[12]
    ungoods_center_area_sum= row[13]
    ungoods_center_house_num = row[14]
    ungoods_center_house_area= row[15]
    ungoods_center_unhouse_area= row[16]
    ungoods_suburb_area_sum= row[17]
    ungoods_suburb_house_num = row[18]
    ungoods_suburb_house_area= row[19]
    ungoods_suburb_unhouse_area= row[20]
    ungoods_city_area_sum= row[21]
    ungoods_city_house_num= row[22]
    ungoods_city_house_area= row[23]
    ungoods_city_unhouse_area = row[24]
    list_date.append(date)
    list_goods_center_house_num.append(goods_center_house_num)
    list_goods_suburb_house_num.append(goods_suburb_house_num)
    list_goods_city_house_num.append(goods_city_house_num)
    list_ungoods_center_house_num.append(ungoods_center_house_num)
    list_ungoods_suburb_house_num.append(ungoods_suburb_house_num)
    list_ungoods_city_house_num.append(ungoods_city_house_num)
line=Line("房产走势图")
line.add("城区商品房",list_date,list_goods_center_house_num,mark_point=["max","min"])
line.add("郊区商品房",list_date,list_goods_suburb_house_num)
line.add("全市商品房",list_date,list_goods_city_house_num)
line.add("城区二手房",list_date,list_ungoods_center_house_num)
line.add("郊区二手房",list_date,list_ungoods_suburb_house_num)
line.add("全市二手房",list_date,list_ungoods_city_house_num)
line.show_config()
line.render()