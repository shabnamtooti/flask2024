import requests
city='tehran'
appid_key='cbd8a61b665a724fd6ecd8db39a8eefa'
units='metric'
response=requests.get('https://api.openweathermap.org/data/3.0/weather?q={city}&appid={app_id}').json()
print(response['weather'][0]['description'])
print(response[])