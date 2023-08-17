import matplotlib.pyplot as plt

# set font and size
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(6, 4))

# initialize parameters
labels = ['酒店旅游', '转账红包', '餐饮美食', '日用百货', '交通出行', '充值缴费', '服饰装扮', '互助保障']
values = [21914.00, 827.20, 19973.20, 950.83, 10379.59, 2428.54, 9859.93, 8351.35]
colors = ['b', 'm', 'g', 'y', 'r', 'k', 'c', 'w']
plt.pie(values, labels=labels, colors=colors, labeldistance=1.02, autopct='%.2f%%', startangle=90, radius=0.9, center=(0.2, 0.2), textprops={'fontsize': 9, 'color': 'k'})

# draw figure
plt.title("2020年全年支出分布图")
plt.show()