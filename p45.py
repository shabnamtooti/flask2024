from bs4 import BeautifulSoup
with open('index1.html')as f:
    res=BeautifulSoup(f,'lxml')
    fr=res.find('from')
    find_sub=fr.find('input',{'type':'submit'})
    print(find_sub)