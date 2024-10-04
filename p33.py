import requests
from bs4 import BeautifulSoup
url='https://www.python.org/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
#rows=soup.find_all('a')
#rows=soup.findAll('p')
#row=soup.select_one('a')
#rows=soup.select('button.search_button')
rows=soup.select('button#submit')
for i in rows:
    print(i)