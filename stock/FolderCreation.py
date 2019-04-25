import os

import requests
from bs4 import BeautifulSoup

fh=open('store1.txt','r')
for line in fh:
    str = line.split(',')
    st=str[1].rstrip()
    path='C:/Users/Jyothshna/PycharmProjects/stock/%s' %st
    s='C:/Users/Jyothshna/PycharmProjects/stock/'
    if(os.path.exists(path)):
        print("path already exists")
    else:
        os.mkdir(path)

    url=" https://finance.yahoo.com/quote/"
    htmls =['profile','financials','key-statistics']

    #summary
    summary=url+""+str[0]+"?p="+str[0]
    new_link="C:/Users/Jyothshna/PycharmProjects/stock/" +str[1].rstrip()+"/summary.html"
    r=requests.get(summary,stream=True)
    with open(new_link,'wb') as f:
        f.write(r.content)
        f.close()

    finance = url + "" + str[0]+"/"+htmls[1]+ "?p=" + str[0]
    new_link = "C:/Users/Jyothshna/PycharmProjects/stock/" + str[1].rstrip() + "/financial.html"
    r = requests.get(finance, stream=True)
    with open(new_link, 'wb') as f:
        f.write(r.content)
        f.close()

    profile = url +""+ str[0] + "/" + htmls[0] + "?p=" + str[0]
    new_link = "C:/Users/Jyothshna/PycharmProjects/stock/" + str[1].rstrip() + "/profile.html"
    r = requests.get(profile, stream=True)
    with open(new_link, 'wb') as f:
        f.write(r.content)
        f.close()

    statistics = url + "" + str[0] + "/" + htmls[2] + "?p=" + str[0]
    new_link = "C:/Users/Jyothshna/PycharmProjects/stock/" + str[1].rstrip() + "/statistics.html"
    r = requests.get(statistics, stream=True)
    with open(new_link, 'wb') as f:
        f.write(r.content)
        f.close()
