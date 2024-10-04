import requests
'''
params={
    'q':'tehran',
    'appid':'cbd8a61b665a724fd6ecd8db39a8eefa'
}
response=requests.get(url=url,params=params)
'''
city='tehran'
app_id='cbd8a61b665a724fd6ecd8db39a8eefa'
response=requests.get(
    f'https://api.openweathermap.org/data/3.0/weather?q={city}&appid={app_id}').json()
print(response)