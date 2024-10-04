from bs4 import BeautifulSoup
with open('index1.html')as f:
    res=BeautifulSoup(f,'lxml')
    mytable=res.find('table')
    rows=mytable.find_all('tr')
    for i in rows:
        x=i.find_all('td')
        for j in x:
            print(j.text)