import requests
from bs4 import BeautifulSoup
import pandas
data=[]
for i in range(1,6):
	rec=requests.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_"+str(i)+"?_encoding=UTF8&pg="+str(i))
	soup=BeautifulSoup(rec.text,'html.parser')
	records=soup.find_all('div', attrs={'class':'zg_itemImmersion'})
	for record in records:
		try:
			name=record.find('div',attrs={'class':'p13n-sc-truncate p13n-sc-line-clamp-1'}).text
		except:
			name="Not Available"
		try:
			url="https://www.amazon.com" + record.find('a',attrs={'class':'a-link-normal'})['href']
		except:
			url="Not Available"
		try:
			author=record.find('div',attrs={'class':'a-row a-size-small'}).text
		except:
			author="Not Available"
		try:
			price=record.find('span',attrs={'class':'p13n-sc-price'}).text
		except:
			price="Not Available"
		try:
			stars=record.find('span',attrs={'class':'a-icon-alt'}).text
		except:
			stars="Not Available"
		try:
			rating=record.find(attrs={'class':'a-size-small a-link-normal'}).text
		except:
			rating="Not Available"
			stars="Not Available"
		data.append((name,url,author,price,rating,stars))
table = pandas.DataFrame(data,columns=['Name','URL','Author','Price','Number of Ratings','Average Rating'])
table.to_csv('com_book.csv',index=False,encoding='utf-8')