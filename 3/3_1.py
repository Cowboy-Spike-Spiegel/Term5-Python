# get size
size = input()
row = int(size.split()[0])
column = int(size.split()[1])

# get matrix
matrix_A = eval(input())
matrix_B = eval(input())

#print
print('[', end='')
for i in range(row):

    print('[', end='')
    for j in range(column):
        print(matrix_A[i][j]+matrix_B[i][j], end='')
        if j!= column-1:
            print(',', end='')
    print(']', end='')

    if i != row-1:
        print(',', end='')
print(']', end='')
