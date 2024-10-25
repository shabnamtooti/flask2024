from fastapi import FastAPI
app=FastAPI()
mylist=[10,20,30]
@app.get('/')
def index():
    return mylist
@app.post('/add/{x:int}')
def add(x:int):
    mylist.append(x)
    return mylist
@app.put('/update/{x:int}')
def UpdateList(x:int,index:int):
    mylist[index]=x
    return mylist
@app.delete('/delete/{x:int}')
def DeleteFromList(x:int):
    if x in mylist:
        mylist.remove(x)
        return mylist