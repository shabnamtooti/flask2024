import requests
from bs4 import BeautifulSoup
url='https://www.python.org/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
print(soup.find_all('a'))