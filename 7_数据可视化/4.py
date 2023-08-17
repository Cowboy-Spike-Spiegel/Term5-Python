import matplotlib.pyplot as plt
import pandas as pd

# get data
data = pd.read_excel('八年级期末考试成绩表.xlsx')

# set font and size
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10, 10))

# draw figures
plt.subplot(3, 2, 1)
x = data["语文分数"]
plt.xlabel('分数', fontsize=10)
plt.ylabel('学生数量', fontsize=10)
plt.title("期末考试语文成绩", fontsize=10)
plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], facecolor='m', edgecolor="black", alpha=0.7)

plt.subplot(3, 2, 2)
x = data["数学分数"]
plt.xlabel('分数', fontsize=10)
plt.ylabel('学生数量', fontsize=10)
plt.title("期末考试数学成绩", fontsize=10)
plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], facecolor='m', edgecolor="black", alpha=0.7)

plt.subplot(3, 2, 3)
x = data["英语分数"]
plt.xlabel('分数', fontsize=10)
plt.ylabel('学生数量', fontsize=10)
plt.title("期末考试英语成绩", fontsize=10)
plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], facecolor='m', edgecolor="black", alpha=0.7)

plt.subplot(3, 2, 4)
x = data["物理分数"]
plt.xlabel('分数', fontsize=10)
plt.ylabel('学生数量', fontsize=10)
plt.title("期末考试物理成绩", fontsize=10)
plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], facecolor='m', edgecolor="black", alpha=0.7)

plt.subplot(3, 2, 5)
x = data["生物分数"]
plt.xlabel('分数', fontsize=10)
plt.ylabel('学生数量', fontsize=10)
plt.title("期末考试生物成绩", fontsize=10)
plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], facecolor='m', edgecolor="black", alpha=0.7)

plt.subplot(3, 2, 6)
x = data["政治分数"]
plt.xlabel('分数', fontsize=10)
plt.ylabel('学生数量', fontsize=10)
plt.title("期末考试政治成绩", fontsize=10)
plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], facecolor='m', edgecolor="black", alpha=0.7)

plt.tight_layout(pad=1.08)
plt.show()
