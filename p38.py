import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.skysports.com/')
soup=BeautifulSoup(response.text,'lxml')
row=soup.find('table')
print(row)