import mysql.connector
import re
import requests
from bs4 import BeautifulSoup
conn=mysql.connector.connect(user='root',password='Paruchuru@1997',host='localhost',database='stock')
mycursor=conn.cursor()
sql = "INSERT INTO profile(prof_ticker,name,Address,phonenum,website,sector,industry,full_time,bus_summ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
ind=0
list=['ACB','EOLS','VEEV','BMY','CRON','TWTR']
list1 =['Aurora Cannabis Inc.','Evolus Inc.','Veeva Systems Inc.','Bristol-Myers Squibb Company','Cronos Group Inc.','Twitter Inc.']
while ind<len(list1):
    f = open('C:/Users/Jyothshna/PycharmProjects/stock/' + list1[ind] + '/profile.html','r')
    soup = BeautifulSoup(f, 'html.parser')
    name = soup.find('h3', class_='Fz(m) Mb(10px)')
    print(name.get_text())
    t = soup.find(class_='D(ib) W(47.727%) Pend(40px)')
    t1 = t.findAll('a')
    for i in t1:
        if i.get('data-reactid') == '17':
            a= i.get_text()
            print(a)
        if i.get('data-reactid') == '19':
            webadd = i.get_text()
            print(webadd)
    add = soup.find('p', attrs={'data-reactid': '8'})
    print(add.text)
    si = soup.findAll('span', class_='Fw(600)')
    for row1 in si:
        if row1.get('data-reactid') == '23':
            sector = row1.get_text()
            print(sector)
        if row1.get('data-reactid') == '27':
            indu = row1.get_text()
            print(indu)
        if row1.get('data-reactid') == '31':
            fulltime = row1.get_text()
            print(fulltime)
    val = (list[ind], name.get_text(), add.text,a, webadd, sector, indu, fulltime,'summery')
    mycursor.execute(sql,val)
    conn.commit()
    ind+=1
    print(mycursor.rowcount,'record inserted')



