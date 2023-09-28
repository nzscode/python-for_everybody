import psycopg2

conn = psycopg2.connect(user='postgres', password='password', host='localhost', port='5432', database='master')

# create a cursor
cur = conn.cursor()

# cur.execute("""DROP TABLE IF EXISTS person""")
# # Create Table:
# new_table = """CREATE TABLE IF NOT EXISTS person (
#     id SERIAL,
#     first_name VARCHAR(255),
#     last_name VARCHAR(255)
# );
# """
# cur.execute(new_table)
# conn.commit()
# conn.close()

# f_names = ["Sophia", "Liam", "Olivia", "Noah"]
# l_names = ["Smith", "Kim", "Garcia", "Muller"]
#
# full_names = []
#
# for i in range(len(f_names)):
#     full_names.append((f_names[i], l_names[i]))
#
# # print(full_names)
#
# for i in range(len(full_names)):
#     cur.execute("""INSERT INTO person(first_name, last_name) VALUES
#     (%s, %s)""", full_names[i])
#
# conn.commit()
# conn.close()

cur.execute("""SELECT * FROM person LIMIT 0""")
column_names = [desc[0] for desc in cur.description]

# print(column_names)
#
# conn.commit()
# conn.close()




# # ADD ENTRIES TO TABLE
# cur.execute("""INSERT INTO person(id, first_name, last_name, age, gender, email) VALUES
# (1, 'Mike', 'Vronski', 25, 'm', 'mike.v@jksgslkdj.com'),
# (2, 'Sally', 'Penderson', 25, 'f', 'Penderson_Sal@adffdsdf.com'),
# (3, 'Tuong', 'Trin-Ha', 25, 'f', 'TTH.Viet@ghfgh.com'),
# (4, 'Paolo', 'Pereira', 25, 'm', 'Paolo_P85@jksgslkdj.org'),
# (5, 'Jim', 'Tammam', 25, 'm', 'Jim_Tammam@jksgslkdj.com'),
# (6, 'Heila', 'Gljaiopo', 25, 'f', 'Hail_of_Thorns@dfgfdg.com'),
# (7, 'Xavier', 'Iijadk', 25, 'm', 'X_a_V_8_9_i_E_r._Iijadk@dfgfdg.com'),
# (8, 'Gui', 'Domique', 25, 'm', 'GuiDomique@jksgslkdj.ca')
# """)
# headers = ["id", "first_name", "last_name"]

cur.execute(("""SELECT * FROM person ;"""))
# print(cur.fetchall())
for row in cur.fetchall():
    # print(len(row))
    for i in range(len(row)):
        print(f"{column_names[i]}: {row[i]}")

# sql = cur.mogrify("""SELECT * FROM person WHERE first_name LIKE '%m' ;""")
# cur.execute(sql)
#
# print(cur.fetchall())
#
#
# conn.commit()
# cur.close()
# conn.close()

conn.commit()
conn.close()