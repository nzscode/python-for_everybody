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