import csv

dict_demo = [
    {'a': 3, 'b': 8, 'c': 4},
    {'a': 9, 'b': 4, 'c': 2},
    {'a': 9, 'b': 10, 'c': 6}
]
dict_list = []
fields = ("k", "v")

for i in range(len(dict_demo)):
    for k, v in dict_demo[i].items():
        dict_list.append((k, v))

path = "../Resources/"
with open(path + "dict.csv", 'w') as file:
    write = csv.writer(file)

    write.writerow(fields)
    write.writerows(dict_list)


