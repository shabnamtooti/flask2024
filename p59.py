from fastapi import FastAPI
from pydantic import BaseModel
class Item(BaseModel):
    x:int=None
    y:str
    z:int
app=FastAPI()
mylist=[5,10,15]
@app.get('/add/{x:int}')
def addTolist(x:int,y:str):
    mylist.append(x)
    mylist.append(y)
    return mylist
@app.post('/add2')
def addTolist2(item:Item):
    mylist.extend(item.x)
    mylist.extend(item.y)
    mylist.extend(item.z)