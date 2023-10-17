import psycopg2

conn = psycopg2.connect(
    user='postgres',
    password='password',
    host='localhost',
    port=5432,
    database='demo_database')

conn.autocommit = True
cur = conn.cursor()

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

# Insert Multiple Rows 2
"""INSERT INTO demo_schema.demo_table (id, l_name) VALUES
(25, 'Tony'), 
(64, 'Vince'), 
(125, 'Zefren'), 
(8, 'Jorge' ), 
(295, 'Patel');"""



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

cur.execute()

conn.commit()
conn.close()
