import requests
from bs4 import BeautifulSoup as bs
import datetime
import csv
import os
import pandas as pd

#masternodesonline to csv
url = "https://masternodes.online"
r= requests.get(url)
html = r.content
soup = bs(html, "lxml")
table1 = soup.find("table", {"id": "masternodes_table"})
row = table1.find_all('tr')
cells = table1.find_all('td')
data =[]
today = datetime.datetime.now().strftime("%y-%m-%d")
filename = ("MNO-"+today+".csv")

print(filename)


#html table to dict
titles = []
"""
for c,i in enumerate(row):
    if(c==0):
        print(i.text+ "  "+str(c))
"""
for c,i in enumerate(cells):
    data.append(i.text)

coin = data[2::11]
price = data[3::11]
change = data[4::11]
volume = data[5::11]
mkap = data[6::11]
roi = data[7::11]
ncount = data[8::11]
coinreq = data[9::11]
tprice = data[10::11]
"""
for i in range(5):
    print(coin[i]+ " "+ roi[i]+" "+ tprice[i])
"""
table = {}
col_names = ['coin','price','change','volume', 'mkap', 'roi', 'ncount', 'coinreq', 'tprice']

for i,c in enumerate(coin):
    table[c] = roi[i], tprice[i], ncount[i], volume[i], mkap[i], change[i]
#print(table[coin[1]][0])
#to DataFrame

tdata = pd.DataFrame.from_dict(table, orient='index')
#write to file
print(tdata)
location = "E:\\MNO_Data\\"
save = location+filename
tdata.to_csv(save)
#with open(filename, 'wb') as csvfile:
