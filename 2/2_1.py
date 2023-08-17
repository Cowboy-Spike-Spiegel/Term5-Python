size = int(input())

dict = {}
for i in range(size):
    word = input()
    word_cat = word.split(' ')[0]
    word_dog = word.split(' ')[1]
    dict[word_dog] = word_cat
#print(dict)

word = 'cat'
output = []
while True:
    word = input()
    if word=="dog":
        break

    translate = dict.get(word)
    if translate==None:
        translate = 'dog'
    output.append(translate)

for word in output:
    print(word)