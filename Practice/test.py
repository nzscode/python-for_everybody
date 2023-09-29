dummy = [
    {'a': 3, 'b': 8, 'c': 4},
    {'a': 9, 'b': 4, 'c': 2},
    {'a': 9, 'b': 10, 'c': 6},
]

dingbat = [
    {'a': 6, 'b': 4, 'c': 1},
    {'a': 3, 'b': 8, 'c': 3}
]

dicty = {}
lst = []
for i in range(len(dummy)):
    lst.append(dummy[i])

for i in range(len(dingbat)):
    lst.append(dingbat[i])

for i in range(len(lst)):
    dicty[i] = lst[i]

print(dicty)