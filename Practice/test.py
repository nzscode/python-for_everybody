import psycopg2

conn = psycopg2.connect(
    user='postgres',
    password='password',
    host='localhost',
    port=5432)

conn.autocommit = True
cur = conn.cursor()

# cur.execute("""DROP DATABASE IF EXISTS demo_database""")

cur.execute("""CREATE DATABASE demo_database""")

conn.commit()
conn.close()
