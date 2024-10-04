import requests
url='https://www.python.org/static/img/python-logo.png'
response=requests.get(url)
with open('i.jpg','wb')as f:
    f.write(response.content)