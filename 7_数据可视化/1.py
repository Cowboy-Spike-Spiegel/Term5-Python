import matplotlib.pyplot as plt

# set fonts, title, x, y and y-limit
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.title('历次普查全国人口')
plt.xlabel('(年份/year)s',loc='right')
plt.ylabel('(万人/10000 persons)',loc='top')
plt.ylim(0,160000)

years=['1953','1964','1982','1990','2000','2010','2020']
values=[58260, 69458, 100818, 113368, 126583, 133972, 141178]

# draw table
plt.bar(years, values, width=0.8,color='m',alpha=0.5,bottom=0.8)
plt.grid(axis='y', which='major')
for x,y in zip(years, values):
    plt.text(x, y, format(y, ','), ha='center', va='bottom', fontsize=10, color='m', alpha=0.9)
plt.legend(['人口数量'],loc='upper left')
plt.show()