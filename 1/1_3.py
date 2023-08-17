number = int(input())
if number == 2:
    print('2')
elif number <= 4:
    print('2 3')
else:
    ans = list()
    ans.append(2)
    ans.append(3)
    for i in range(5, number+1):
        j = 2
        while(j < int(i/2)):
            if i%j==0:
                break
            j=j+1
        if j==int(i/2):
            ans.append(i)

    for i in range(len(ans)-1):
        print(ans[i], end=' ')
    print(ans[len(ans)-1], end='')