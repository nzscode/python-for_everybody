import xml
import psycopg2
import sqlite3

conn = sqlite3.connect('Py4e-Musical Track.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artists;
''')

cur.close()

