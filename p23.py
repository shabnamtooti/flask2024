import requests
from bs4 import BeautifulSoup
url='https://www.python.org/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html5lib.parser')
print(soup)