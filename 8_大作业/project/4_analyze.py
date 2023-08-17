import matplotlib.pyplot as plt
import json


# target cities
cities = {'北京': 'bj', '上海': 'sh', '广州': 'gz', '深圳': 'sz', '合肥': 'hf'}
city_name = ['北京', '上海', '广州', '深圳', '合肥']

# path
path_json = 'data/json/'
path_figure = 'figures/'
# figure count for saving
cnt_figure = 1


# read city.json data ---------------------------------------------------------
data_dict = dict()
for name in city_name:
    with open(path_json + name + '.json', 'r') as f:
        data_dict[name] = json.load(f)



# analyze preparations --------------------------------------------------------

# set each data size
city_size = 5
price_size = 4
room_size = 3
direction_size = 4

# set keys to find in data_dict
price_keys = ['average', 'lower', 'upper', 'middle']
room_keys = ['room_1', 'room_2', 'room_3']
direction_keys = ['North', 'South', 'West', 'East']

# set limits (has manually selected from json)
price_limit = 600000
price_square_limit = 3000

# set color list
color_city = ['orange', 'deepskyblue', 'orchid', 'g', 'y']
color_room = ['orange', 'deepskyblue', 'orchid', 'g']
color_direction = ['orange', 'deepskyblue', 'orchid', 'g']

# set pie label
pie_room = ['room_1', 'room_2', 'room_3', 'room_>=4']   # add last two show

# set font
plt.rcParams['font.sans-serif'] = ['SimHei']



# Task 1: compare 5 cities ----------------------------------------------------

# 1.1: compare 5 cities with price

plt.figure(figsize=(40, 20))
# find each price category with i (generate 4 sub figures)
for i in range(price_size):
    # basic settings
    plt.subplot(1, price_size, i + 1)
    plt.title('Price-'+price_keys[i], fontsize=30)
    plt.xlabel('cities', fontsize=15)
    plt.ylabel('price(￥/m^2)', fontsize=15)

    # generate x & y data
    x = [i for i in range(1, city_size+1)]
    y = list()
    for name in city_name:
        y.append(data_dict[name]['price'][price_keys[i]])

    # generate subplot
    plt.ylim((0, price_limit))
    plt.bar(x, y, color=color_city)
    # add text
    plt.xticks(x, city_name, size=30)
    for x_value, y_value in zip(x, y):
        plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=15)

# print & save plot
plt.suptitle('Price Compare',fontsize=30)
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()


# 1.2: compare 5 cities with price_average

plt.figure(figsize=(40, 20))
# find each price category with i (generate 4 sub figures)
for i in range(price_size):
    # basic settings
    plt.subplot(1, price_size, i + 1)
    plt.title('Price_square-'+price_keys[i], fontsize=30)
    plt.xlabel('cities', fontsize=15)
    plt.ylabel('price(￥/m^2)', fontsize=15)

    # generate x & y data
    x = [i for i in range(1, city_size+1)]
    y = list()
    for name in city_name:
        y.append(data_dict[name]['price_square'][price_keys[i]])

    # generate subplot
    plt.ylim((0, price_square_limit))
    plt.bar(x, y, color=color_city)
    # add text
    plt.xticks(x, city_name, size=30)
    for x_value, y_value in zip(x, y):
        plt.text(x_value,y_value,'%.4f'%y_value, ha='center', fontsize=15)

# print & save plot
plt.suptitle('Price Square Compare',fontsize=30)
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()



# Task 2: compare each cities' room1,2,3 --------------------------------------

# 2.1: self compare rate

plt.figure(figsize=(40, 20))
# find each city with i (generate 5 sub figures)
for i in range(city_size):
    # basic settings
    plt.subplot(1, city_size, i + 1)
    plt.title(city_name[i], fontsize=100)

    # generate room1, 2, 3, >=4 sizes
    sizes = list()
    for j in range(room_size):
        sizes.append(100 * data_dict[city_name[i]][room_keys[j]]['size'] / data_dict[city_name[i]]['size'])
    # generate the rest size for >=4
    total_123 = 0
    for item in sizes:
        total_123 += item
    sizes.append(100-total_123)

    # generate subplot with text
    patches, l_text, p_text = \
        plt.pie(sizes, labels=pie_room, colors=color_room, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    # adjust words size
    for item in p_text:
        item.set_size(20)

# print & save plot
plt.suptitle('Rooms Components',fontsize=30)
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()


# 2.2: compare room1, 2, 3 between cities depend on price

# find room_1, 2, 3 with i (generate 3 figures)
for i in range(room_size):
    plt.figure(figsize=(40, 20))

    # find price category with i (generate 4 sub figures)
    for j in range(price_size):
        # basic settings
        plt.subplot(1, price_size, j + 1)
        plt.title('Price-' + price_keys[j], fontsize=30)
        plt.xlabel('cities', fontsize=15)
        plt.ylabel('price(￥/m^2)', fontsize=15)

        # generate x & y data
        x = [i for i in range(1, city_size+1)]
        y = list()
        # find each city - room_i+1 - price_key - price number
        for name in city_name:
            y.append(data_dict[name][room_keys[i]][price_keys[j]])

        # generate subplot
        plt.bar(x, y, color=color_city)
        # add text
        plt.xticks(x, city_name, size=15)
        for x_value, y_value in zip(x, y):
            plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=15)

    # print & save plot
    plt.suptitle(room_keys[i]+' Compare (no limit to flush y)', fontsize=30)
    plt.savefig(path_figure + str(cnt_figure))
    cnt_figure += 1
    plt.show()



# Task 3: compare each cities' plates -----------------------------------------

# compare each city's plates (generate 5 figures)
for name in city_name:
    plt.figure(figsize=(40, 20))
    # basic settings
    plt.title(name+' plates average price', fontsize=30)
    plt.xlabel('plates', fontsize=15)
    plt.ylabel('price(￥/m^2)', fontsize=15)

    # select plates witch has big size(top 10 percent)
    temp = data_dict[name]['plates']['data']    # get all plates' information
    # store each plates tuple(name, size)
    temp_list = list()
    for info_name, info_data in temp.items():
        temp_list.append([info_name, info_data['size']])
    sorted(temp_list, key=(lambda x: x[1]), reverse=True)

    # generate x data
    x_size = int(data_dict[name]['plates']['size'] / 10)
    x = [i for i in range(1, x_size+1)]

    # generate x label and y data
    x_name = list()
    y = list()
    for i in range(x_size):
        info_name = temp_list[i][0]
        x_name.append(info_name)
        y.append(data_dict[name]['plates']['data'][info_name]['average'])

    # generate subplot
    plt.bar(x, y, color=color_city)
    # add text
    plt.xticks(x, x_name, size=30)
    for x_value, y_value in zip(x, y):
        plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=15)

    # print & save plot
    plt.savefig(path_figure + str(cnt_figure))
    cnt_figure += 1
    plt.show()


# Task 4: compare each cities' directions -------------------------------------

# compare each city's plates (generate 5 figures)
plt.figure(figsize=(40, 20))
for i in range(city_size):
    # basic settings
    plt.subplot(1, city_size, i+1)
    plt.title(city_name[i]+' directions\naverage square price', fontsize=30)
    plt.xlabel('direction', fontsize=15)
    plt.ylabel('price(￥/m^2)', fontsize=15)

    # generate x data
    x = [i for i in range(1, direction_size+1)]

    # generate y data
    y = list()
    for info in direction_keys:
        y.append(data_dict[city_name[i]][info]['price_square_average'])

    # generate subplot
    plt.bar(x, y, color=color_direction)
    # add text
    plt.xticks(x, direction_keys, size=30)
    for x_value, y_value in zip(x, y):
        plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=15)

# print & save plot
plt.suptitle('Direction Compare (no limit to flush y)', fontsize=30)
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()



# Task 5: compare each cities' GDP & price_square -----------------------------

GDP = {'北京': 183980, '上海': 173630, '广州': 151200, '深圳': 174600, '合肥': 121800}

'''ATTENTION:
    we suppose that each person need rent a room with 20m^2
    such we induct a rate to represent:
        20m^2 room price / GDP
'''

# generate this rate
square = 20
months = 12
rates = list()
for name, number in GDP.items():
    rates.append(months * square * data_dict[name]['price_square']['average'] / number)

# basic settings
plt.figure(figsize=(40, 20))
plt.title('Compare GDP & price_square\n with rate: 20m^2 room price / GDP', fontsize=30)
plt.xlabel('cities', fontsize=30)
plt.ylabel('rate(1)', fontsize=30)

# generate x & y data
x = [i for i in range(1, city_size+1)]
y = rates

# generate subplot
plt.bar(x, y, color=color_city)
# add text
plt.xticks(x, city_name, size=30)
for x_value, y_value in zip(x, y):
    plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=30)

# print & save plot
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()



# Task 6: compare each cities' Income & price_square --------------------------

Income = {'北京': 127535, '上海': 136752, '广州': 118133, '深圳': 153471, '合肥': 104729}

'''ATTENTION:
    we suppose that each person need rent a room with 20m^2
    such we induct a rate to represent:
        20m^2 room price / Income
'''

# generate this rate
square = 20
months = 12
rates = list()
for name, number in Income.items():
    rates.append(months * square * data_dict[name]['price_square']['average'] / number)

# basic settings
plt.figure(figsize=(40, 20))
plt.title('Compare Income & price_square\n with rate: 20m^2 room price / Income', fontsize=30)
plt.xlabel('cities', fontsize=30)
plt.ylabel('rate(1)', fontsize=30)

# generate x & y data
x = [i for i in range(1, city_size+1)]
y = rates

# generate subplot
plt.bar(x, y, color=color_city)
# add text
plt.xticks(x, city_name, size=30)
for x_value, y_value in zip(x, y):
    plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=30)

# print & save plot
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()



# Task 7: further analyze -----------------------------------------------------

# 人均可支配收入（税后）
Income_Discretionary = {'北京': 75002, '上海': 78027, '广州': 74416, '深圳': 70847, '合肥': 46009}

big_city_name = ['北京', '上海', '广州', '深圳']
# 租房人数比例（未查询到合肥）
Rate_rent = {'北京': 0.333, '上海': 0.384, '广州': 0.508, '深圳': 0.768}
# 非本地户籍人口比例
Rate_inward = {'北京': 0.385, '上海': 0.421, '广州': 0.489, '深圳': 0.665}


# Q1: Continue GDP and Income, how about Income_Discretionary? ----------------

'''ATTENTION:
    we suppose that each person need rent a room with 20m^2
    such we induct a rate to represent:
        20m^2 room price / Income_Discretionary
'''

# generate this rate
square = 20
months = 12
rates = list()
for name, number in Income_Discretionary.items():
    rates.append(months * square * data_dict[name]['price_square']['average'] / number)

# basic settings
plt.figure(figsize=(40, 20))
plt.title('Compare Income & price_square\n with rate: 20m^2 room price / Income_Discretionary', fontsize=30)
plt.xlabel('cities', fontsize=30)
plt.ylabel('rate(1)', fontsize=30)

# generate x & y data
x = [i for i in range(1, city_size+1)]
y = rates

# generate subplot
plt.bar(x, y, color=color_city)
# add text
plt.xticks(x, city_name, size=30)
for x_value, y_value in zip(x, y):
    plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=30)

# print & save plot
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()


# Q2: How about Rate_rent and Rate_inward? ------------------------------------

'''ATTENTION:
    we suppose that each person need rent a room with 20m^2
    such we induct a rate to represent:
        20m^2 room price / Income_Discretionary
'''

# generate this rate: rent in inward
rent_in_inward = list()
for s, t in zip(Rate_rent.values(), Rate_inward.values()):
    rent_in_inward.append(s/t)

# basic settings
plt.figure(figsize=(40, 20))
plt.title('Rate_rent / Rate_inward', fontsize=30)
plt.xlabel('cities', fontsize=30)
plt.ylabel('rate(1)', fontsize=30)

# generate x & y data
x = [i for i in range(1, len(rent_in_inward)+1)]
y = rent_in_inward

# generate subplot
plt.bar(x, y, color=color_city)
# add text
plt.xticks(x, big_city_name, size=30)
for x_value, y_value in zip(x, y):
    plt.text(x_value, y_value, '%.4f' % y_value, ha='center', fontsize=30)

# print & save plot
plt.savefig(path_figure + str(cnt_figure))
cnt_figure += 1
plt.show()