import sqlite3

conn=sqlite3.connect('prices.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM price'):
    print (row)
