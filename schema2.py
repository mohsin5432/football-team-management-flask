import sqlite3

connection = sqlite3.connect('teams.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE teams(
     pk INTEGER PRIMARY KEY AUTOINCREMENT,
     teamname VARCHAR(32),
     tmatches INTEGER,
     wins INTEGER,
     draws INTEGER,
     defeat INTEGER,
     score INTEGER,
     date TEXT
    );"""
)

connection.commit()
cursor.close()
connection.close()
