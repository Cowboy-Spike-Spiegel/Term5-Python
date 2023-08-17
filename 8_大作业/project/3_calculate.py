import pandas as pd
import json

# target cities
cities = {'北京': 'bj', '上海': 'sh', '广州': 'gz', '深圳': 'sz', '合肥': 'hf'}

# csv outputFile attributes
csv_attributes = ['title', 'name', 'area', 'rooms',
                  'price_lower', 'price_upper', 'price_average',
                  'price_square_lower', 'price_square_upper', 'price_square_average']


# calculate each city.json
for name, info in cities.items():

    # read data & convert into list -------------------------------------------
    data = pd.read_csv('data/preprocessing/'+name+'.csv')
    data = data.values.tolist()
    # preprocessing json list
    city_dict = dict()

    # generate city_json[0][1][2] (size & price & price_square) ---------------
    # variables
    price_total = 0
    price_lower = 0x3F3F3F
    price_upper = 0
    price_square_total = 0
    price_square_lower = 0x3F3F3F
    price_square_upper = 0

    # judge for each record
    for record in data:
        # update price-total, lower, upper
        price_total = price_total + float(record[6])
        price_lower = min(float(record[4]), price_lower)
        price_upper = max(float(record[5]), price_upper)
        # update price_square-total, lower, upper
        price_square_total = price_square_total + float(record[9])
        price_square_lower = min(float(record[7]), price_square_lower)
        price_square_upper = max(float(record[8]), price_square_upper)

    # calculate average and middle
    price_average = price_total / len(data)
    sorted(data, key=(lambda x: x[6]))  # sort by price_average
    index = int(len(data)/2)
    if len(data) & 1 == 1:
        price_middle = float(data[index][6])
    else:
        price_middle = (float(data[index][6]) + float(data[index+1][6])) / 2

    # calculate price_square average and middle for room_i
    price_square_average = price_square_total / len(data)
    sorted(data, key=(lambda x: x[9]))  # sort by price_square_average
    index = int(len(data)/2)
    if len(data) & 1 == 1:
        price_square_middle = float(data[index][9])
    else:
        price_square_middle = (float(data[index][9]) + float(data[index+1][9])) / 2

    # store calculate data into json
    city_dict['size'] = len(data)
    city_dict['price'] = {'average': price_average,
                          'lower': price_lower,
                          'upper': price_upper,
                          'middle': price_middle}
    city_dict['price_square'] = {'average': price_square_average,
                          'lower': price_square_lower,
                          'upper': price_square_upper,
                          'middle': price_square_middle}

    # generate city_json[3:5] (room1:3 calculate) -----------------------------
    # variables (list for room_1, room_2, room_3)
    rooms = [list(), list(), list()]
    price_total = [0, 0, 0]
    price_lower = [0x3F3F3F, 0x3F3F3F, 0x3F3F3F]
    price_upper = [0, 0, 0]
    # judge for each record
    for record in data:
        if record[3] <= 3:
            index = record[3]-1
            # store this record
            rooms[index].append(record)
            # update price-total, lower, upper
            price_total[index] = price_total[index] + float(record[6])
            price_lower[index] = min(float(record[4]), price_lower[index])
            price_upper[index] = max(float(record[5]), price_upper[index])

    # variables
    price_average = [0, 0, 0]
    price_middle = [0, 0, 0]
    for i in range(3):
        # calculate average and middle
        price_average[i] = price_total[i]/len(rooms[i])
        sorted(rooms[i], key=(lambda x: x[6]))  # sort by price_average
        index = int(len(rooms[i])/2)
        if len(rooms[i])&1 == 1:
            price_middle[i] = float(rooms[i][index][6])
        else:
            price_middle[i] = float(float(rooms[i][index][6])+float(rooms[i][index+1][6]))/2

        # store calculate data into city.json
        key = 'room_'+str(i+1)
        city_dict[key] = {'size': len(rooms[i]),
                          'average': price_average[i],
                          'lower': price_lower[i],
                          'upper': price_upper[i],
                          'middle': price_middle[i]}

    # generate city_json[6:9] (north & south & west & east) -------------------
    size = [0, 0, 0, 0]
    price_square_total = [0, 0, 0, 0]
    for record in data:
        if '北' in record[0]:
            size[0] += 1
            price_square_total[0] += float(record[9])
        if '南' in record[0]:
            size[1] += 1
            price_square_total[1] += float(record[9])
        if '西' in record[0]:
            size[2] += 1
            price_square_total[2] += float(record[9])
        if '东' in record[0]:
            size[3] += 1
            price_square_total[3] += float(record[9])

    # store calculate data into city.json
    city_dict['North'] = {'size': size[0], 'price_square_average': price_square_total[0] / size[0]}
    city_dict['South'] = {'size': size[1], 'price_square_average': price_square_total[1] / size[1]}
    city_dict['West'] = {'size': size[2], 'price_square_average': price_square_total[2] / size[2]}
    city_dict['East'] = {'size': size[3], 'price_square_average': price_square_total[3] / size[3]}

    # generate city_json[10] (plate) ------------------------------------------
    # store plates' name
    plate_set = set()
    for record in data:
        # cause some records has no plate!!!
        if type(record[1]) == str and record[1] != 'nan':
            plate_set.add(record[1].split('-')[1])

    # generate each plates' price_average
    plate_list = list(plate_set)
    plate_size = [0] * len(plate_list)
    plate_total = [0] * len(plate_list)
    for record in data:
        if type(record[1]) == str and record[1] != 'nan':
            index = plate_list.index(record[1].split('-')[1])
            plate_size[index] += 1
            plate_total[index] += record[6]
    plate_dict = dict()
    for i in range(len(plate_list)):
        plate_dict[plate_list[i]] = {'size': plate_size[i], 'average': plate_total[i] / plate_size[i]}

    # store calculate data into city.json
    city_dict['plates'] = {'size': len(plate_list), 'data': plate_dict}

    # write city.json ---------------------------------------------------------
    with open('data/json/' + name + ".json", 'w') as jsonFile:
        jsonFile.write(json.dumps(city_dict, indent=1, ensure_ascii=False))