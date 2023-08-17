from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

districts={'dongcheng':'东城区','xicheng':'西城区','haidian':'海淀区','chaoyang':'朝阳区'}
attributes=["小区名","平米数","总价","均价"]

for item in districts.keys():
    # generate output file name
    file_name = districts[item]+'.csv'
    house_list = list()
    # get front 5 pages
    for i in range(1,6):
        HTML = BeautifulSoup(urlopen('https://bj.lianjia.com/ershoufang/'+item+'/'+'pg'+str(i)), features="lxml")
        # catch divs
        for p,q,m,n in zip(
                HTML.findAll("div",{"class":"positionInfo"}),
                HTML.findAll("div",{"class":"houseInfo"}),
                HTML.findAll("div",{"class":"totalPrice totalPrice2"}),
                HTML.findAll("div",{"class":"unitPrice"})
        ):
            msg = list()
            msg.append(p.get_text().split('-')[0])
            msg.append(q.get_text().split('|')[1])
            msg.append(m.get_text())
            msg.append(n.get_text())
            house_list.append(msg)
    # write into file
    with open(file_name,'w',newline='')as f:
        writer = csv.writer(f)
        writer.writerow(attributes)
        writer.writerows(house_list)