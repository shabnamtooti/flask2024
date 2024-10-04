#cbd8a61b665a724fd6ecd8db39a8eefa  (KEY)
import requests
url='https://api.openweathermap.org/data/3.0/weather'
params={
    'q':'tehran',
    'appid':'cbd8a61b665a724fd6ecd8db39a8eefa'
}
response=requests.get(url=url,params=params).json()
print(requests)