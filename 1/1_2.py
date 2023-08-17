m, n = input().split(' ')

i=j=0
while i < len(m) and m[i] == '0':
    i=i+1
while j < len(n) and n[j] == '0':
    j=j+1

ans = ""
while i < len(m) and j < len(n) :
    ans += m[i]+n[j]
    i=i+1
    j=j+1
while i < len(m) :
    ans += m[i]
    i=i+1
while j < len(n) :
    ans += n[j]
    j=j+1

print(ans)