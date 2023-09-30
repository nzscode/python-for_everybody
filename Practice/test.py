import psycopg2

conn = psycopg2.connect(user='postgres', password='password', host='localhost', port='5432', database='master')

cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS dict_demo""")

cur.execute("""CREATE TABLE dict_demo(
    num SERIAL,
    keys VARCHAR(225),
    values VARCHAR(225)
    );""")

data = [
    {'a': 3, 'b': 8, 'c': 4},
    {'a': 9, 'b': 4, 'c': 2},
    {'a': 9, 'b': 10, 'c': 6}
]

# entries = [("a", 1), ("b", "f"), {"r": [3, "c"]}, [(4, 5), (1, 2, 3)]]
# entries = "b", "c", "e", [5, 4], {"j": [1,2,3]}

path = "../Resources/"

entries = []
for i in range(len(data)):
    for k, v in data[i].items():
        entries.append((k, v))
# print(entries)

# entries = []
# for i in range(len(data)):
#     entries.append(data[i])
#     print(entries)

for i in range(len(entries)):
    cur.execute("""INSERT INTO dict_demo(keys, values) VALUES
    (%s, %s)""", entries[i])



#
# with open(path + "demp.json", 'w') as file:
#     json.dump(entries, file, indent=4)

conn.commit()
conn.close()
