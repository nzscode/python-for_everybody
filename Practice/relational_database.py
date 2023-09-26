import psycopg2
import re

# conn = sqlite3.connect('emaildb.sqlite')
conn = psycopg2.connect(user='postgres', password='password', host='localhost', port='5432', database='postgres')
# conn = psycopg2.connect('orgdb.psycopg2')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = "../Resources/mbox.txt"
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    org = ""
    r = re.findall('@([a-zA-Z0-9.]*)', email)
    if len(r) > 0:
        org = r[0].split()
    # print(org[0])


#
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
