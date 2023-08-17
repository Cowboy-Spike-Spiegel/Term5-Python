size = int(input())
my_stack = input().split()
pop_out = list()

# one turn
turn = input().split()
action = turn[0]
del turn[0]
if action == "pop":
    times = min(int(turn[0]), len(my_stack))
    for i in range(times):
        pop_out.append(my_stack[len(my_stack) - 1])
        del my_stack[len(my_stack)-1]
elif action == "push":
    for i in range(len(turn)):
        my_stack.append(turn[i])

# two turn
turn = input().split()
action = turn[0]
del turn[0]
if action == "pop":
    times = min(int(turn[0]), len(my_stack))
    for i in range(times):
        pop_out.append(my_stack[len(my_stack) - 1])
        del my_stack[len(my_stack)-1]
elif action == "push":
    for i in range(len(turn)):
        my_stack.append(turn[i])


# print out my_stack
print("len = "+str(len(my_stack)), end='')
if len(my_stack) != 0:
    print(", data =", end='')
    for i in range(len(my_stack)):
        print(" "+str(my_stack[i]), end='')
print("")

# print out pop_out
print("len = "+str(len(pop_out)), end='')
if len(pop_out) != 0:
    print(", data =", end='')
    for i in range(len(pop_out)):
        print(" "+str(pop_out[i]), end='')
#print("")