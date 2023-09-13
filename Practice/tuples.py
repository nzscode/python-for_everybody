text = input("Enter file:")
file = open("../Resources/" + text)
senders = {}
tmp_lst = []
for line in file:
    if line.startswith("From "):
        line = line.split()
        hr = line[5].split(":")
        # print(hr[0])
        if hr[0] in senders.keys():
            senders[hr[0]] += 1
        else:
            senders[hr[0]] = 1

for k,v in senders.items():
    tmp_lst.append((k, v))

tmp_lst.sort()

for x in range(len(tmp_lst)):
    print(f"{tmp_lst[x][0]} {tmp_lst[x][1]}")
