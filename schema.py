import sqlite3

connection = sqlite3.connect('insta.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
     pk INTEGER PRIMARY KEY AUTOINCREMENT,
     username VARCHAR(16),
     fname VARCHAR(32),
     password VARCHAR(32),
     email VARCHAR(32),
     intro VARCHAR(65535),
     picname TEXT,
     date TEXT
    );"""
)

connection.commit()
cursor.close()
connection.close()
