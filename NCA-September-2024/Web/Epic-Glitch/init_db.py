import sqlite3

connection = sqlite3.connect('ctf.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, password, uid) VALUES (?, ?, ?)",
            ('admin', 'sdf435wepefjSup3rH4rdPassw0rd124dxf23!', 0))

connection.commit()
connection.close()
