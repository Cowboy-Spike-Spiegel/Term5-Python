str = input()

items = set()
for character in str:
    items.add(character)

ans = list(items)
ans.sort()
for i in range(len(ans)):
    print(ans[i], end='')