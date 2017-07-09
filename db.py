import sqlite3
conn=sqlite3.connect('prices.db')

c = conn.cursor()
c.execute('''CREATE TABLE price (id integer primary key AUTOINCREMENT ,pname text, url text, current_price real, min_price real)''')
conn.commit()
conn.close()
