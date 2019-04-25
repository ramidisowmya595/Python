import mysql.connector

import re
import requests
from bs4 import BeautifulSoup

conn=mysql.connector.connect(user='root',password='Paruchuru@1997',host='localhost',database='stock')
mycursor=conn.cursor()
sql = "INSERT INTO Finances(fin_ticker,total_revenue,cost_of_revenue,income_before_tax,Net_income) VALUES (%s,%s,%s,%s,%s)"
ind=0
list=['ACB','EOLS','VEEV','BMY','CRON','TWTR']
list1 =['Aurora Cannabis Inc.','Evolus Inc.','Veeva Systems Inc.','Bristol-Myers Squibb Company','Cronos Group Inc.','Twitter Inc.']
while ind<len(list1):
    f = open('C:/Users/Jyothshna/PycharmProjects/stock/' + list1[ind] + '/financial.html', 'r')
    soup = BeautifulSoup(f, 'html.parser')
    t = soup.findAll('td', class_='Fz(s) Ta(end) Pstart(10px)')
    for i in t:
        if i.get('data-reactid') == '42':
            total = i.get_text()
            print(total)
        if i.get('data-reactid') == '52':
            revenue = i.get_text()
            print(revenue)
        if i.get('data-reactid') == '169':
            income = i.get_text()
            print(income)
    t1 = soup.findAll('td', class_='Fw(600) Ta(end) Py(8px) Pt(36px)')
    for k in t1:
        if(k.get('data-reactid') == '247'):
            net = k.get_text()
            print(net)
    val = (list[ind], total, revenue, income, net)
    mycursor.execute(sql, val)
    conn.commit()
    ind += 1
    print(mycursor.rowcount, 'record inserted')

