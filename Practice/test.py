import psycopg2

conn = psycopg2.connect(
    user='postgres',
    password='password',
    host='localhost',
    port=5432)

conn.autocommit = True
cur = conn.cursor()

# Create Database:
create_database = """CREATE DATABASE IF NOT EXISTS demo_database;"""

# Rename Database
rename_database = """ALTER DATABASE demo_database RENAME TO demo_test_database;"""

# Drop Database
drop_database = """DROP DATABASE IF EXISTS demo_database;"""
drop_database_cascade = """DROP DATATBASE IF EXISTS demo_database CASCADE;"""

# Create Schema
create_schema = """CREATE SCHEMA IF NOT EXISTS demo_schema"""

# Rename Schema
rename_schema = """ALTER SCHEMA demo_schema RENAME TO demo_test_schema;"""

# Drop Schema
drop_schema = """DROP SCHEMA IF EXISTS demo_schema;"""
drop_schema_cascade = """DROP SCHEMA IF EXISTS demo_schema CASCADE;"""

# Set Schema search_path
set_search_path = """SET search_path TO demo_schema, public;"""

# Show Schema search_path
show_search_path = """SHOW search_path;"""

# Create Table
create_table = """CREATE TABLE IF NOT EXISTS demo_schema.demo_table(
    id SERIAL,
    f_name VARCHAR(50)
    );"""

create_table_test = """CREATE TABLE IF NOT EXISTS test_table(
    id SERIAL,
    city VARCHAR(225) DEFAULT 'Panama',
    population INTEGER,
    country VARCHAR(100)
    );"""

create_table_in_schema = """CREATE TABLE IF NOT EXISTS demo_schema.demo_schema_table(
    demo_schema_col_0 SERIAL,
    demo_schema_col_1 VARCHAR(225) ,
    demo_schema_col_2 VARCHAR(225)
    );"""

# Drop Table
drop_table = """DROP TABLE IF EXISTS demo_table;"""
drop_table_in_schema = """DROP TABLE IF EXISTS demo_schema.demo_schema_table;"""

# Alter Table
alter_table = """ALTER TABLE IF EXISTS demo_table RENAME TO demo_renamed_table"""
alter_table_in_schema = """ALTER TABLE IF EXISTS demo_schema.demo_schema_table RENAME TO demo_schema_renamed_table"""

# Alter Table Schema
# ex: From public to demo_schema
alter_table_move_schema = """ALTER TABLE IF EXISTS demo_table SET SCHEMA public"""
alter_table_set_schema = """ALTER TABLE IF EXISTS public.demo_table SET SCHEMA demo_schema"""

alter_table_add_column = """ALTER TABLE IF EXISTS demo_schema.demo_table ADD COLUMN IF NOT EXISTS l_name VARCHAR(50);"""
alter_table_in_schema_add_column = """ALTER TABLE IF EXISTS demo_schema.demo_schema_table ADD COLUMN IF NOT EXISTS test_column INTEGER;"""

alter_table_drop_column = """ALTER TABLE IF EXISTS demo_table DROP COLUMN IF EXISTS test_column;"""
alter_table_in_schema_drop_column = """ALTER TABLE IF EXISTS demo_schema.demo_schema_table DROP COLUMN IF EXISTS test_column;"""

alter_table_rename_column = """ALTER TABLE IF EXISTS demo_table  RENAME COLUMN test_column TO rename_test_column;"""
alter_table_in_schema_rename_column = """ALTER TABLE IF EXISTS demo_schema.demo_schema_table RENAME COLUMN test_column TO rename_test_column;"""

alter_table_alter_column_type = """ALTER TABLE IF EXISTS demo_table  ALTER COLUMN test_column TYPE VARCHAR(50);"""
alter_table_in_schema_alter_column_type = """ALTER TABLE IF EXISTS demo_schema.demo_schema_table ALTER COLUMN test_column TYPE VARCHAR(50);"""

alter_table_alter_column_default_value = """ALTER TABLE IF EXISTS demo_table  ALTER COLUMN test_column SET DEFAULT 'alien';"""
alter_table_in_schema_alter_column_default_value = """ALTER TABLE IF EXISTS demo_schema.demo_schema_table ALTER COLUMN test_column SET DEFAULT 'alien';"""

alter_table_alter_column_drop_default = """ALTER TABLE IF EXISTS demo_table  ALTER COLUMN test_column DROP DEFAULT;"""
alter_table_in_schema_alter_column_drop_default = """ALTER TABLE IF EXISTS demo_schema.demo_schema_table ALTER COLUMN test_column DROP DEFAULT;"""

# Copy Table
copy_table = """ALTER TABLE demo_schema.demo_table ADD COLUMN IF NOT EXISTS (SELECT city, population FROM public.test_table);"""

# Insert Values:
insert_values = """INSERT INTO demo_schema.demo_table (id, f_name) VALUES (5, 'Laila');"""
insert_multiple_values = """INSERT INTO demo_schema.demo_table (id) VALUES (95), (125), (7);"""
insert_multiple_values_multiple_columns = """INSERT INTO demo_schema.demo_table (id, f_name) VALUES (5, 'Laila'), (41, 'Juno'), (125, 'Yennefer'), (2, 'Ruby' ), (9852, 'Halifa');"""


"""CREATE TABLE customers (
id (SERIAL)"""
# Insert Multiple Rows 2
"""INSERT INTO demo_schema.demo_table (id, f_name, l_name) VALUES
(5, 'Laila', NULL), 
(69, 'Angel', 'Rivioni'),
(144, 'Safra', 'Barril'),
(27, 'Ravio', NULL),
(11, 'Delivio', 'Viona'),
(99, 'Ruby', 'Espinoza'),
(125, 'Travis', 'James'), 
(7, 'Ellen', 'Yashuda'), 
(3, 'Sirio', 'Forrel'),
(847, 'Waitecosta', 'Warren'),
(41, 'Juno', 'Thompson'),
(9852, 'Halifa', NULL), 
(2, 'Ruby', 'Thompson'),
(125, 'Yennefer', 'Patel'),
(125, 'Viola', NULL),
(25, 'Tony', 'Jessup'), 
(64, 'Vince', 'Warret'), 
(125, 'Zefren', 'Cassel'), 
(8, 'Jorge', 'Espinoza' ), 
(295, 'Patel', 'Travis');"""

# Drop Values:
drop_rows_where_value = """DELETE FROM demo_schema.demo_table WHERE id = 125;"""
drop_all_rows = """DELETE FROM demo_schema.demo_table;"""
drop_multiple_rows = """DELETE FROM demo_schema.demo_table WHERE demo_col_0 IN (9, 7);"""
drop_rows_value_null = """DELETE FROM demo_schema.demo_table WHERE f_name IS NULL;"""

# Update/Alter Values
change_single_value = """UPDATE demo_schema.demo_table SET demo_col_1 = 'Toronto' WHERE demo_col_1 = 'Juno';"""
change_multiple_values = """UPDATE demo_schema.demo_table SET demo_col_1 = 'Toronto' WHERE demo_col_1 IN ('Toronto', 'Sydney');"""
change_all_values = """UPDATE demo_schema.demo_table SET demo_col_1 = 'Toronto';"""
change_value_to_default = """UPDATE demo_schema.demo_table SET demo_col_1 = DEFAULT;"""

# Copy Values
copy_values_same_table = """INSERT INTO demo_schema.demo_table(demo_col_2) SELECT demo_col_1 FROM demo_schema.demo_table;"""
copy_values_different_table = """INSERT INTO demo_schema.demo_schema_table(demo_schema_col_1) SELECT demo_col_1 FROM demo_schema.demo_table;"""

# Order By
order = """SELECT f_name FROM demo_schema.demo_table ORDER BY f_name ASC;"""

# Where
where = """SELECT * FROM demo_schema.demo_table WHERE id = '125';"""
where_in = """SELECT * FROM demo_schema.demo_table WHERE id IN (125, 7, 9);"""
where_and = """SELECT * FROM demo_schema.demo_table WHERE id = '125' AND l_name = 'Cassel';"""
where_is_null = """SELECT * FROM demo_schema.demo_table WHERE id = '125' AND l_name IS NULL;"""
where_or = """SELECT * FROM demo_schema.demo_table WHERE id = '4' OR l_name = 'Espinoza';"""
where_between = """SELECT * FROM demo_schema.demo_table WHERE id BETWEEN 5 AND 100;"""
where_like_matches_first_to_case_sensitive = """SELECT * FROM demo_schema.demo_table WHERE f_name LIKE 'Vio%';"""
where_like_matches_num_of_single_chars_case_sensitive = """SELECT * FROM demo_schema.demo_table WHERE f_name LIKE '_i%';"""
where_like_matches_first_to_case_insensitive = """SELECT * FROM demo_schema.demo_table WHERE f_name ILIKE 'Vio%';"""
where_like_matches_num_of_single_chars_case_insensitive = """SELECT * FROM demo_schema.demo_table WHERE f_name ILIKE '_i%';"""
where_not = """SELECT * FROM demo_schema.demo_table WHERE l_name NOT IN ('James', 'Warren', 'Thompson', 'Patel', 'Yashuda', 'Travis');"""

# LIMIT
limit = """SELECT * FROM demo_schema.demo_table LIMIT 3;"""
offset = """SELECT * FROM demo_table LIMIT 5, offset 2;"""

# Inner Join
inner_join = """SELECT a_fruit, b_fruit FROM table_a INNER JOIN table_b ON a_fruit = b_fruit;"""

# Group By
group_by = """SELECT l_name FROM customers GROUP BY l_name;"""

table_alias = """SELECT f_name, l_name FROM customers AS last_name WHERE l_name = 'Thompson';"""
column_alias = """SELECT f_name, l_name AS last_name FROM customers WHERE f_name = 'Ruby';"""

cur.execute(column_alias)
result_returned = cur.fetchall()
# print(result_returned)

# To see the results in an indented form instead of a giant string
for row in result_returned:
    if len(result_returned) >= 1:
        for i in range(len(result_returned)):
            print("column" + str(i) + ": " + row[i])
    print("\n")

conn.commit()
conn.close()
