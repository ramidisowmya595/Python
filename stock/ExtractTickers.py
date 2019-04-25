import csv

import requests
from bs4 import BeautifulSoup
url='https://finance.yahoo.com/trending-tickers'
code=requests.get(url)
f=csv.writer(open('store1.txt','w'))
f.writerow(['Symbol','Name'])
s=BeautifulSoup(code.content,'html.parser')
first=s.findAll('td',class_='data-col0 Ta(start) Pstart(6px) Pend(15px)')
second=s.findAll('td',class_='data-col1 Ta(start) Pstart(10px) Miw(180px)')

for link,link2 in zip(first,second):
    print(link.text,link2.text)
    f.writerow([link.text,link2.text])

