from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# target cities
cities = {'北京': 'bj', '上海': 'sh', '广州': 'gz', '深圳': 'sz', '合肥': 'hf'}

# csv outputFile attributes
csv_attributes = ['title', 'name', 'area', 'rooms', 'price_lower', 'price_upper']


# ***
records_in_a_page = 30

# get cities rent data
for name, info in cities.items():
    # root url path
    url_root = 'https://' + info + '.lianjia.com'

    # generate name.csv -------------------------------------------------------
    with open('data/original/'+name+".csv", 'w', newline='', encoding='utf-8-sig') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow(csv_attributes)

        # 1, get districts path in this city ----------------------------------
        html = BeautifulSoup(urlopen(url_root + '/zufang'), features="lxml")
        # find all district blocks
        blocks = html.findAll(name='li', attrs={'class': 'filter__item--level2', 'data-type': 'district'})
        # get all district path (ignore the first district-'不限')
        district_path_list = list()
        for i in range(1, len(blocks)):
            district_path_list.append(blocks[i].find('a')['href'])

        # 2. get data each from each district pages ---------------------------
        for path in district_path_list:
            # 2.1 get page size for this city from city's index page
            html = BeautifulSoup(urlopen(url_root + path), features="lxml")
            size_record = int(html.findAll(name="span", attrs={"class": "content__title--hl"})[0].text)
            size_page = int(size_record / records_in_a_page)
            if( size_record % records_in_a_page > 0 ):
                size_page = size_page+1
            print(path, size_record, size_page)

            # 2.2 scrapy data in pages & copy data into file
            for i in range(1, size_page+1):
                print(i)
                html = BeautifulSoup(urlopen(url_root + path + 'pg' + str(i)), features="lxml")

                # get data into list
                title_block = html.findAll("p", {"class": "content__list--item--title"})
                des_block = html.findAll("p", {"class": "content__list--item--des"})
                price_block = html.findAll("span", {"class": "content__list--item-price"})
                for title, des, price in zip(title_block, des_block, price_block):
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