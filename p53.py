from peewee import SqliteDatabase,Model,TextField,IntegerField
from fastapi import FastAPI
app=FastAPI()
db=SqliteDatabase('school.db')
class Student(Model):
    name=TextField()
    family=TextField()
    age=IntegerField()
    class Meta:
        Database=db
        db_table='student'
Student.create_table()
@app.post('/add')
def add(name:str,family:str,age:int):
    Student.create(name=name,family=family,age=age)
@app.get('/')
def index():
    st=Student.select()
    return [(i.id,i.name,i.family,i.age)for i in st]
@app.delete('/remove/{id:int}')
def delRec(id):
    x=Student.get(id==id)
    x.delete_intance()
@app.put('/update/{id:int}')
def updateRec(id:int,name:str,family:str,age:int):
    x=Student.get(id=id)
    x.name=name
    x.family=family
    x.age=age
    x.save()