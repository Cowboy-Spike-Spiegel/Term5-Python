import pandas as pd
import csv

# target cities
cities = {'北京': 'bj', '上海': 'sh', '广州': 'gz', '深圳': 'sz', '合肥': 'hf'}

# csv outputFile attributes
csv_attributes = ['title', 'name', 'area', 'rooms',
                  'price_lower', 'price_upper', 'price_average',
                  'price_square_lower', 'price_square_upper', 'price_square_average']


# preprocessing each city.csv with "deduplicate" and "append"
for name, info in cities.items():

    # read data & convert into list -------------------------------------------
    data = pd.read_csv('data/original/'+name+'.csv', encoding='utf-8-sig')
    data = data.values.tolist()
    original_size = len(data)
    print('preprocessing', name, original_size)

    # open log and error file
    logFile = open('data/logs/' + name + ".log", 'w', encoding='utf-8')
    repeatFile = open('data/logs/' + name + "_repeat.txt", 'w', encoding='utf-8')
    errorFile = open('data/logs/' + name + "_error.txt", 'w', encoding='utf-8')

    # generate deduplicated data & write into file ----------------------------
    with open('data/preprocessing/' + name + ".csv", 'w', newline='', encoding='utf-8-sig') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow(csv_attributes)

        # generate price_square_lower, price_square_upper & deduplicate
        i = 0
        cnt_delete = 0
        while i < len(data):
            # solve illegal records depend on rooms
            if str(data[i][3]).isdigit()==False or int(data[i][3])<=0:
                # write into error.log
                errorFile.write(str(data[i])+'\n')
                del data[i]
                cnt_delete += 1
                continue

            # deduplicate
            #print('deduplicate', i)
            cnt_repeat = 0
            j = i+1
            while j < len(data):
                # find repeat
                if data[i] == data[j]:
                    # write into repeat.log
                    repeatFile.write('['+str(i)+', '+str(j)+'] '+str(data[j])+'\n')
                    del data[j]
                    j -= 1
                    cnt_repeat += 1
                    cnt_delete += 1
                j += 1
            # for data[i], repeat cnt times
            if cnt_repeat > 0:
                logFile.write('repeat '+str(cnt_repeat)+' : '+str(data[i])+'\n')

            # append price_average, price_square_lower, price_square_upper, price_square_average
            if '-' in str(data[i][2]):
                area = str(data[i][2]).split('-')
                area = (float(area[0]) + float(area[1])) / 2
            else:
                area = float(data[i][2])
            data[i].append((float(data[i][4]) + float(data[i][5])) / 2)
            data[i].append(float(data[i][4]) / area)
            data[i].append(float(data[i][5]) / area)
            data[i].append((float(data[i][7]) + float(data[i][8])) / 2)
            # has deduplicated this record with writing into csv
            writer.writerow(data[i])

            i += 1

        # write delete counts
        summary = 'delete(repeat&illegal) : '+str(cnt_delete)+' | orignal '+str(original_size)+' remain '+str(len(data))
        logFile.write(summary)
        print(name, summary)

    # close log and error
    logFile.close()
    errorFile.close()