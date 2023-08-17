import matplotlib.pyplot as plt
import pandas as pd

# preprocessing data
df = pd.read_csv('BeijingPM20100101_20151231.csv', usecols=[1, 2, 6, 7, 8, 9])
df['PM_avg'] = df.iloc[:, 2:6].mean(axis=1)
df.groupby(['year', 'month'])['PM_avg'].mean().to_csv("data.csv")

# get data and cut into slice
data = pd.read_csv("data.csv")
x = data['month'][:12]
data_2010 = data['PM_avg'][:12]
data_2011 = data['PM_avg'][12:24]
data_2012 = data['PM_avg'][24:36]
data_2013 = data['PM_avg'][36:48]
data_2014 = data['PM_avg'][48:60]
data_2015 = data['PM_avg'][60:72]

# initialize figure parameters
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('2010-2015北京PM值折线图', fontsize=18)
plt.xticks(x, ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])
plt.xlabel('月份', loc='right')
plt.ylabel('月平均PM值', loc='top')
plt.ylim(0, 200)

# draw figure with plot
p1, = plt.plot(x, data_2010, 'o-', color='b')
p2, = plt.plot(x, data_2011, 'o-', color='m')
p3, = plt.plot(x, data_2012, 'o-', color='g')
p4, = plt.plot(x, data_2013, 'o-', color='y')
p5, = plt.plot(x, data_2014, 'o-', color='r')
p6, = plt.plot(x, data_2015, 'o-', color='k')
plt.legend([p1, p2, p3, p4, p5, p6], ['2010年', '2011年', '2012年', '2013年', '2014年', '2015年'], loc='upper right', fontsize=9)
plt.grid(linestyle='--')
plt.tick_params(axis='y', direction='in', color='r', grid_color='r')
plt.show()
