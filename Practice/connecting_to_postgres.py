import psycopg2

# connection = psycopg2.connect(
#     user='postgres',
#     password='password',
#     host='localhost',
#     port='5432',
#     database='master')

'''
Create a "database.ini" file with
[postgresql]
host=localhost
database=master
user=postgres
password=password
'''

'''
Create a config.py file with
from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # Read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for params in params:
            db[params[0]] = params[1]

    else:
        raise Exception(f'Section{section} is not found in the {filename} file')

    # print(db)
    return db

config()
'''

'''from config import config

def connect():
    connection = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        print('PostgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated')
#
# if __name__ == "__main__":
#     connect()

connect()'''

from config import config

def connect():
    conn = psycopg2.connect(user='postgres', password='password', host='localhost', port='5432', database='people')
    # create a cursor
    cur = conn.cursor()

    cur.execute(("""SELECT * FROM users WHERE name = 'anna' ;"""))
    print(cur.fetchall())

    conn.commit()
    cur.close()
    conn.close()
#
# if __name__ == "__main__":
#     connect()

connect()