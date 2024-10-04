import requests
from bs4 import BeautifulSoup
url='https://www.python.org/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
#rows=soup.find_all('a')
rows=soup.findAll('a')
for i in rows:
    print(i)