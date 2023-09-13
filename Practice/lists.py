fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        line.rstrip()
        ls = line.split(" ")
        print(ls[1])
        count += 1



print(f"There were {count} lines in the file with From as the first word")
