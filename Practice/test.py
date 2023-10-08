import psycopg2

conn = psycopg2.connect(
    user='postgres',
    password='password',
    host='localhost',
    port=5432,
    database='demo_database')

conn.autocommit = True
cur = conn.cursor()

cur.execute("""ALTER TABLE old_demo_table RENAME TO new_demo_table;""")

conn.commit()
conn.close()
# cur.execute("""DROP TABLE IF EXISTS demo_table1;""")
# cur.execute("""CREATE TABLE demo_table1(
#     id SERIAL PRIMARY KEY,
#     age INTEGER NOT NULL,
#     radius DECIMAL,
#     price MONEY,
#     department VARCHAR(225),
#     quote TEXT,
#     group_leader BOOLEAN NOT NULL,
#     date DATE,
#     time TIME with time zone,
#     tmwtz TIME without time zone
#     );""")

# cur.execute("""INSERT INTO demo_table1(age, radius, price, department, quote, group_leader, date, time, tmwtz) VALUES(
#
#     );""")



