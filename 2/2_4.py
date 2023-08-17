size = input()
list = list(map(int, input().split()))

for i in range(1, len(list)):
    item = list[i]
    for j in range(i):
        if list[j]>item:
            del list[i]
            list.insert(j, item)
            break
    # output
    for i in range(len(list) - 1):
        print(list[i], end=' ')
    print(list[len(list) - 1])