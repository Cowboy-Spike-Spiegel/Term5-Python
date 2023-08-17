import requests
import parsel
import pandas
import csv
import matplotlib.pyplot as plt

# create outputFile and write header
with open('houses.csv', 'w', newline='', encoding='utf-8') as outputFile:
    f_csv = csv.writer(outputFile)
    f_csv.writerow(['name', 'district', 'town', 'position', 'room', 'area', 'average', 'price'])

# crawl data from front 25 pages
for i in range(1, 25):
    # get data and store into result
    selector = parsel.Selector(requests.get(f"https://bj.fang.lianjia.com/loupan/pg{i}/").text)
    result = selector.css('.resblock-list.post_ulog_exposure_scroll.has-results')

    for li in result:
        # name
        name = li.css('.resblock-name a::text').get()
        # location
        location = li.css('.resblock-location span::text').getall()
        district = location[0]
        town = location[1]
        position = li.css('.resblock-location a::text').get()
        # size
        room = li.css('.resblock-room span::text').get()
        # area
        area = li.css('.resblock-area span::text').get()
        if area == None:
            continue
        area = area.split(' ')
        area = area[1]
        area = area.split('-')
        if len(area) != 1:
            area = area[0]
        else:
            area = "".join(list(filter(str.isdigit, "".join(area))))

        # average & price
        average = li.css('.main-price span::text').get()
        priceList = average.split('-')
        if len(priceList) == 1:
            price = f"{int(average) * int(area) / 10000:.4f}"
        else:
            price = priceList[0]
            average = int(price) * 10000 / int(area)
        agerage = int(average)

        # write this record into outputFile
        with open('houses.csv', 'a', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)
            f_csv.writerow([name, district, town, position, room, area, average, price])


# analyze data statistics
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
data = pandas.read_csv('houses.csv', encoding='utf-8')

# price
print("\nPrice most expensive:\n",data[data['price'] == data['price'].max()], '\n')
print("Price most cheap:\n",data[data['price'] == data['price'].min()], '\n')
print("Price middle:\n",data['price'].median())

# average
print("\nAverage most expensive:\n",data[data['average'] == data['average'].max()], '\n')
print("Average most cheap:\n",data[data['average'] == data['average'].min()], '\n')
print("Average middle:\n",data['average'].median())

# price beyond 3*average
print("\nThose price beyond 3*average:")
mean = data['price'].mean()
std = data['price'].std()
low_border = mean-3*std
high_border = mean+3*std
print(data[(data['price'] > high_border) | (data['price'] < low_border)])

# Average exception
print("\nThose average exception:")
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
data.boxplot(['average'])
plt.show()
q1 = data['average'].quantile(q=0.25)
q3 = data['average'].quantile(q=0.75)
low_limit = q1-1.5*(q3-q1)
high_limit = q3+1.5*(q3-q1)
print(data[(data['average'] > high_limit) | (data['average'] < low_limit)])

# discretization processing
avgMax=data['average'].max()
avgMin=data['average'].min()
num=int(avgMax/avgMin)
cuts = pandas.cut(data['average'], num)
print(pandas.value_counts(cuts).sort_index())
value_list=[]
for i in pandas.value_counts(cuts):
    value_list.append(i)
plt.figure()
index=pandas.value_counts(cuts).index
plt.pie(value_list,labels=index,autopct='%0.2f%%')
plt.show()
