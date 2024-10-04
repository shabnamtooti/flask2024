from bs4 import BeautifulSoup
with open('index1.html')as f:
    res=BeautifulSoup(f,'lxml')
    mytable=res.find('table')
    print(mytable)