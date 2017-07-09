from bs4 import BeautifulSoup
import requests

def get_price(url):
	contents=requests.get(url).content
	soup =BeautifulSoup(contents,'html.parser')
	data=soup.find('span', id='priceblock_ourprice')
	price=float(data.get_text())
	return price

def get_name(url):
	contents=requests.get(url).content
	soup =BeautifulSoup(contents,'html.parser')
	data=soup.find('span', id='productTitle')
	name=data.get_text()
	return (name.lstrip()).rstrip()

