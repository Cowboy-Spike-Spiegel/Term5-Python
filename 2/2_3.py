
import  queue

line = input()
n = int(line.split()[0])
m = int(line.split()[1])

q = []
times = 0
arr = list(input().split())
for number in arr:
    flag = False
    for i in range(len(q)):
        if q[i] == number:
            #print("find")
            del q[i]
            q.append(number)
            flag = True
            break
    if flag==True:
        continue
    flag = False

    if len(q) >= n:
        del q[0]
    q.append(number)
    times=times+1

print(times)
q.sort(key=int)
for i in range(len(q)-1):
    print(q[i], end=' ')
print(q[len(q)-1], end = '')