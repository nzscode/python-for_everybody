import re


# text = input("Enter text: ")
# file = open("../Resources/" + text)

count_lst = []
count = 0
for line in file:
    r = re.findall('[0-9]+', line)
    for x in r:
        count += int(x)

print(count)

