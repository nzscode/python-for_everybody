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
create_table = """CREATE TABLE IF NOT EXISTS demo_table(
    demo_col_0 SERIAL,
    demo_col_1 VARCHAR(225) DEFAULT 'panama',
    demo_col_2 VARCHAR(225)
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
alter_table_set_schema = """ALTER TABLE IF EXISTS demo_table SET SCHEMA demo_schema"""

alter_table_add_column = """ALTER TABLE IF EXISTS demo_table ADD COLUMN IF NOT EXISTS test_column INTEGER;"""
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

cur.execute(alter_table_alter_column_default_value)

conn.commit()
conn.close()
