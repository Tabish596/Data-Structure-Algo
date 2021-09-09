list = []
with open('list.txt') as f:
    words = f.readlines()
    for word in words:
        list.append(word[:-1])
print(list)


class node:
