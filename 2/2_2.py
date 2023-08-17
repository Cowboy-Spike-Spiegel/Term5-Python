size_A = input()
A = []
line = input().split()
for number in line:
    A.append(number)


size_B = input()
B = []
line = input().split()
for number in line:
    B.append(number)


gather_intersect = list(set(A).intersection(set(B)))
gather_intersect.sort(key=int)
for i in range(len(gather_intersect)-1):
    print(gather_intersect[i], end=' ')
print(gather_intersect[len(gather_intersect)-1])

gather_union = list(set(A).union(set(B)))
gather_union.sort(key=int)
for i in range(len(gather_union)-1):
    print(gather_union[i], end=' ')
print(gather_union[len(gather_union)-1])

gather_except = list(set(A).difference(set(B)))
gather_except.sort(key=int)
for i in range(len(gather_except)-1):
    print(gather_except[i], end=' ')
print(gather_except[len(gather_except)-1], end=' ')
