import requests
url='python.org'
params={
    'q':'tehran',
    'appid':'cbd8a61b665a724fd6ecd8db39a8eefa'
}
response=requests.get('https://www.google.com')
print(response)