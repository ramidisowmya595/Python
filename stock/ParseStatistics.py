import mysql.connector

import re
import requests
from bs4 import BeautifulSoup

conn=mysql.connector.connect(user='root',password='Paruchuru@1997',host='localhost',database='stock')
mycursor=conn.cursor()
sql = "INSERT INTO statistics(sno,stat_ticker,marketcap,enterprise_value,profit_margin,return_on_assets,gross_profit,total_cash,total_debt,current_ratio,operating_cash_flow,levered_free_cash_flow) VALUES (%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
ind=0
list=['ACB','EOLS','VEEV','BMY','CRON','TWTR']
list1 =['Aurora Cannabis Inc.','Evolus Inc.','Veeva Systems Inc.','Bristol-Myers Squibb Company','Cronos Group Inc.','Twitter Inc.']
while ind<len(list1):
    f = open('C:/Users/Jyothshna/PycharmProjects/stock/' + list1[ind] + '/statistics.html', 'r')
    soup = BeautifulSoup(f, 'html.parser')
    t = soup.findAll('td', class_='Fz(s) Fw(500) Ta(end)')
    ind += 1
    print(ind)
    for i in t:
        if i.get('data-reactid') == '19':
            market = i.get_text()
            print(market)
        if i.get('data-reactid') == '26':
            enterprise = i.get_text()
            print(enterprise)
    t1 = soup.findAll('td', class_='Fz(s) Fw(500) Ta(end)')
    for k in t1:
        if k.get('data-reactid') == '138':
            assets = k.get_text()
            print(assets)
        if k.get('data-reactid') == '222':
            tcash = k.get_text()
            print(tcash)
        if k.get('data-reactid') == '272':
            ocf = k.get_text()
            print(ocf)
        if k.get('data-reactid') == '280':
            ltcf = k.get_text()
            print(ltcf)
        if k.get('data-reactid') == '238':
            tdebt = k.get_text()
            print(tdebt)
        if k.get('data-reactid') == '253':
            cratio = k.get_text()
            print(cratio)
        if k.get('data-reactid') == '180':
            gprofit = k.get_text()
            print(gprofit)
        if (k.get('data-reactid') == '119'):
            pmargin = k.get_text()
            print(pmargin)
    val = (list[ind], market,enterprise,pmargin,assets,gprofit,tcash,tdebt,cratio,ocf,ltcf)
    mycursor.execute(sql, val)
    conn.commit()
    print(mycursor.rowcount, 'record inserted')

