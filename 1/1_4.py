size = int(input())
data = list(map(int,input().split(' ')))

sum = cnt = 0
for i in range(len(data)):
    sum += data[i]
    if(data[i] >= 60):
        cnt = cnt+1

print("average =", "%.1f"%(sum/size))
print("count =", cnt)