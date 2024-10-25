import requests
import threading
import time
def fetch_url(url):
    response=requests.get(url)
    print(f'url:{url},length:{len(response.text)}')
start_time=time.time()
urls=[
    'https://play.google.com/store/games?device=windows&pli=1'
    'https://www.google.com/chrome/what-you-make-of-it/'
    'https://www.youtube.com/'
    'https://www.samsung.com/iran/?msockid=3cc9b58d2350632a1466a09c22566266'
    'https://www.pinterest.com/'
]
threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_url,args=(url))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
end_time=time.time()
excecute_time=end_time - start_time
print(excecute_time)