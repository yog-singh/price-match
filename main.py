import sqlite3
import scraper

def add_product():
	print (" [+] Enter the URL of the product: ")
	url = input()
	conn=sqlite3.connect('prices.db')
	c = conn.cursor()
	names=scraper.get_name(url)
	cprice=scraper.get_price(url)
	lprice=cprice
	c.execute('INSERT INTO price ( pname, url, current_price, min_price) VALUES(?, ?, ?, ?)', (names,url, cprice, lprice))
	conn.commit()
	conn.close()

def check_db():
        print ("[+] The product prices are as follows: \n")
        conn=sqlite3.connect('prices.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM price'):
                print (row)
        conn.close()

def delete_product():
        conn=sqlite3.connect('prices.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM price'):
                print (row)
        print ("Enter the id of product to delete: ")
        inp=input()
        c.execute('DELETE FROM price WHERE id=?', inp)
        conn.commit()
        conn.close()


print ("[+] Select from the following options: \n")
print ("[.] 1. Add product url. \n")
print ("[.] 2. Check database. \n")
print ("[.] 3. Delete product. \n")
choice = int(input())
if (choice==1):
	add_product()
elif (choice==2):
	check_db()
else:
	delete_product()


