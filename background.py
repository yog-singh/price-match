import sqlite3
import scraper
import time

while (True):
        conn=sqlite3.connect('prices.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM price'):
                pid=row[0]
                url=row[2]
                low_price=row[4]
                current_price=scraper.get_price(url)
                if (current_price<low_price):
                        low_price=current_price
                c.execute('UPDATE price SET current_price=? , min_price=? WHERE id = ?',(current_price, low_price, pid))
                conn.commit()
        time.sleep(600)
