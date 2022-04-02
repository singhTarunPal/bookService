import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, author) VALUES (?, ?)",
            ('First Missile', 'Abdul Kalam')
            )

cur.execute("INSERT INTO posts (title, author) VALUES (?, ?)",
            ('Second Missile', 'Manmohan Singh')
            )

connection.commit()
connection.close()
