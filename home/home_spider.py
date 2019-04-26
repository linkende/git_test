import requests
from bs4 import BeautifulSoup

#url="https://www.cdfgj.gov.cn/SCXX/Default.aspx"
#url="http://fgj.chengdu.gov.cn/cdsfgj/jsjy/jsjy.shtml"
url="https://www.cdfgj.gov.cn/SCXX/Default.aspx?action=ucEveryday"

html=requests.get(url)
html.encoding = 'utf-8'

htmls=html.text
list=[]
soup=BeautifulSoup(htmls,'html.parser')
#print(soup)
big_table=soup.find('div',class_='rightContent')
print(big_table)
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
#print(list)
#goods 商品房
goods_center_area_sum=list[1]
goods_center_house_num=list[2]
goods_center_house_area=list[3]
goods_center_unhouse_area=list[4]
goods_suburb_area_sum=list[6]
goods_suburb_house_num=list[7]
goods_suburb_house_area=list[8]
goods_suburb_unhouse_area=list[9]
goods_city_area_sum=list[11]
goods_city_house_num=list[12]
goods_city_house_area=list[13]
goods_city_unhouse_area=list[14]
#ungoods 二手房
ungoods_center_area_sum=list[16]
ungoods_center_house_num=list[17]
ungoods_center_house_area=list[18]
ungoods_center_unhouse_area=list[19]
ungoods_suburb_area_sum=list[21]
ungoods_suburb_house_num=list[22]
ungoods_suburb_house_area=list[23]
ungoods_suburb_unhouse_area=list[24]
ungoods_city_area_sum=list[26]
ungoods_city_house_num=list[27]
ungoods_city_house_area=list[28]
ungoods_city_unhouse_area=list[29]

print("商品房中心城区：",goods_center_area_sum,goods_center_house_num,goods_center_house_area,goods_center_unhouse_area)

print("二手房中心城区：",ungoods_center_area_sum,ungoods_center_house_num,ungoods_center_house_area,ungoods_center_unhouse_area)





