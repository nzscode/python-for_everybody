import psycopg2

conn = psycopg2.connect(user='postgres', password='password', host='localhost', port='5432', database='master')
# create a cursor
cur = conn.cursor()

# Create Table:
# cur.execute("""CREATE TABLE IF NOT EXISTS person (
#     id INT PRIMARY KEY,
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     age INT,
#     gender CHAR,
#     email VARCHAR(255)
# ) ;
#     """)
#
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
# headers = ["id", "first_name", "last_name", "age", "gender", "email"]
#
# cur.execute(("""SELECT * FROM person ;"""))
# # print(cur.fetchall())
# for row in cur.fetchall():
#     # print(len(row))
#     for i in range(len(row)):
#         print(f"{headers[i]}: {row[i]}")

sql = cur.mogrify("""SELECT * FROM person WHERE first_name LIKE '%m' ;""")
cur.execute(sql)

print(cur.fetchall())


conn.commit()
cur.close()
conn.close()
