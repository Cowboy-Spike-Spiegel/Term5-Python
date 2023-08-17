from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# target cities
cities = {'北京': 'bj', '上海': 'sh', '广州': 'gz', '深圳': 'sz', '合肥': 'hf'}

# csv outputFile attributes
csv_attributes = ['title', 'name', 'area', 'rooms', 'price_lower', 'price_upper']


# get cities rent data
for name, info in cities.items():
    # get page size for this city from city's index page
    html = BeautifulSoup(urlopen("https://" + info + ".lianjia.com/zufang"), features="lxml")
    size_record = int(html.findAll(name="span", attrs={"class":"content__title--hl"})[0].text)
    size_page = int(size_record/30)
    if( size_record%30 > 0 ):
        size_page = size_page+1
    print(name, size_record, size_page)

    # generate name.csv
    with open('data/'+name + ".csv", 'w', newline='', encoding='utf-8-sig') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow(csv_attributes)
        # scrapy data in pages & copy data into file
        for i in range(1, size_page+1):
            print(i)
            html = BeautifulSoup(urlopen("https://" + info + ".lianjia.com/zufang/pg" + str(i)),
                                 features="lxml")
            # get data into list
            for title, des, price in zip(
                    html.findAll("p", {"class": "content__list--item--title"}),
                    html.findAll("p", {"class": "content__list--item--des"}),
                    html.findAll("span", {"class": "content__list--item-price"})
            ):
                # solve title
                title = title.get_text().strip()
                # solve des
                des_list = des.get_text().split('/')
                if len(des_list) == 5:
                    name = des_list[0].replace("\n","").strip()
                    area = des_list[1].replace("\n","").strip()[:-1]
                    rooms = des_list[3].replace("\n", "").strip()[0]
                elif len(des_list) == 3:
                    name = ""
                    area = des_list[0].replace("\n", "").strip()[:-1]
                    rooms = des_list[2].replace("\n", "").strip()[0]
                # solve price
                text = price.get_text().split(' ')[0]
                if '-' in text:
                    text = text.split('-')
                    price_lower = text[0]
                    price_upper = text[1]
                else:
                    price_lower = text
                    price_upper = text
                writer.writerows([[title, name, area, rooms, price_lower, price_upper]])