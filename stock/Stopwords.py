import mysql.connector
import re
import requests
from bs4 import BeautifulSoup
conn=mysql.connector.connect(user='root',password='Paruchuru@1997',host='localhost',database='stock')
mycursor=conn.cursor()
Symbol= []
Name = []
tName=str()
a =input("enter any question? ")
#print(a)
q = a.split(" ")
print(q)

new_ques = []
file  = open("Stopwords.txt")
filedata = file.read()
for x in q:
    if '"'+x+'"' not in filedata:
        new_ques.append(x)
print(new_ques)

with open("store1.txt",'r') as file:
    for x in file:
        n = x.split(",")
        Symbol.append(n[0].rstrip())
        Name.append(n[1].rstrip())
print(Symbol)
print(Name)

for i in q:
    for j in range(len(Name)):
        t=Name[j].split(" ")
        #print(Symbol[j])
        if(i==t[0]):
            tName=str(Symbol[j])
            #print(tName)
#print("TnAME= "+tName)

dictionary = {'statistics':{'sno':'None','ticker':'what','marketcap':'what,how much','enterprise_value':'what,how much','return_on_assets':'how much,what','total_cash':'what','operating_cash_flow':'what','levered_free_cash_flow':'what','total_debt':'what','current_ratio':'what,how much','gross_profit':'what,how much','profit_margin':'what,how much'},
                'profile':{'sno':'None','ticker':'what','name':'what','address':'where,what','phonenum':'what','website':'what','sector':'what,which','industry':'what,which','full_time':'how many,what','bus_summ':'what'},
                'finances':{'sno':'None','ticker':'what','total_Revenue':'how much,what','cost_of_revenue':'how much,what','income_before_tax':'how much,what','net_income':'what'}}



queryList = []
for word in new_ques:
    #print(word)
    for type in dictionary:
        #print(word+"==="+type)
        for key in dictionary[type]:
            print(word+"="+type+"="+key)
            if(key.__contains__(word)):
               # print("KEY -"+key)
                queryList.append(key+"==>"+type)

print(queryList)
q1 = queryList[0].split("==>")
attribute = q1[0]
print(attribute)
tableName = q1[1]
print(tName)
query = "SELECT "+attribute+" FROM "+tableName+" WHERE Fin_ticker='" + tName + "'";
mycursor.execute(query)
data =mycursor.fetchone()
print(data)

conn.commit()
conn.close()
mycursor.close()
























