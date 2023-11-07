import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

create_artist = """
DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);"""

create_genre = """
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);"""

create_album = """CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);"""

create_tracks = """CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);"""

insert_artists = """INSERT INTO Artist (name) VALUES
                    ('Taylor Swift'), ('Ed Sheeran'), ('Shawn Mendes');"""
insert_genres = """INSERT INTO Genre (name) VALUES
                    ('Soft Rock'), ('Electro Pop'), ('Synth Pop'), ('Chamber Folk'), ('Dance Pop'), ('Folk Pop'), ('Pop'),
                     ('R & B');"""
insert_album = """INSERT INTO Album (artist_id, title) VALUES
                    (1, '1989'), (1, 'Midnights'), (1, 'Evermore'), (1, 'Folklore'), (1, 'Lover'),
                     (1, 'Red'), (2, 'X - Multiply'), (2, '/ - Divide'), (2, '- - Minus'),
                      (3, 'Illuminate'), (3, 'Wonder');"""
insert_track = """INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES
                    ('Wildest Dreams', 1, 1, 4, 4, 9), ('Blank Space', 1, 2, 4, 4, 2), ('Style', 1, 3, 4, 5, 3), ('Out of the Woods', 1, 3, 4, 3, 4),
                      ('Lavender Haze', 2, 3, 4, 5, 1), ('Anti-Hero', 2, 3, 3, 5, 3), ('Midnight Rain', 2, 2, 3, 4, 6),
                       ('Willow', 3, 4, 4, 4, 1),
                       ('Cardigan', 4, 4, 4, 5,1),
                       ('Cruel Summer', 5, 3, 3, 5, 2), ('The Man', 5, 2, 3, 5, 4), ('Me!', 5, 3, 3, 3, 16),
                         ('Red', 6, 1, 4, 5, 2), ('I knew You Were Trouble', 6, 5, 4, 5, 4), ('Everything Has Changed', 6, 6, 4, 5, 14), ('22', 6, 7, 4, 5, 6),
                    ('Sing', 7, 8, 4, 3, 3), ('Photograph', 7, 6, 4, 5, 6), ('Thinking Out Loud', 7, 1, 5, 5, 11),
                    ('Castle On The Hill', 8, 6, 4, 5, 2), ('Shape Of You', 8, 7, 4, 5, 4),
                    ('Mercy',10, 7, 3, 4, 2), ('Treat You Better', 10, 7, 3, 5, 3),
                     ('Wonder',11, 7, 3, 5, 2);"""


cur.executescript(insert_track)

# file = '../Resources/Library.xml'
#
# def lookup(d, key):
#     found = False
#     for child in d:
#         if found: return child.text
#         if child.tag == 'key' and child.text == key:
#             found =True
#     return None
#
# stuff = ET.parse(file)
# all = stuff.findall('dict/dict/dict')
# print('Dict count: ', len(all))
# for entry in all:
#     if (lookup(entry, 'Track ID')is None):
#         continue
#
#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     album = lookup(entry, 'Album')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')
#
#     if name is None or artist is None or album is None:
#         continue
#
#     print(name, artist, album, count, rating, length)
#
#     cur.execute('''INSERT OR IGNORE INTO Artists (name)
#         VALUES (?)''', (artist, ))
#     cur.execute('SELECT')
#
cur.close()

