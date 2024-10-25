import sqlalchemy as sa
from sqlalchemy.orm import declarative_base,sessionmaker
from fastapi import FastAPI
app=FastAPI()
Base=declarative_base()
class Student(Base):
    __tablename__='St'
    id=sa.Column(sa.Integer,primary_key=True)
    name=sa.Column(sa.String(255))
    family=sa.Column(sa.String(255))
    age=sa.Column(sa.Integer)
engine=sa.create_engine('sqlite:///school53.db')
Base.metadata.create_all(engine)
s=sessionmaker(bin=engine)
session=s()
@app.get('/')
def index():
    students=session.query(Student).all()
    return [(student.id,student.name,student.family,student.age)for student in students]
@app.post('/addRecord')
def addRecord(name:str,family:str,age:int):
    new_rec=Student(name=name,family=family,age=age)
    session.add(new_rec)
    session.commit()
@app.delete('delete/{id:int}')
def del_Rec(id:int):
    del_Record=session.ge(Student,id)
    session.delete(del_Record)
    session.commit()
@app.put('/update/{id:int}')
def Update_Rec(id:int,name:str,family:str,age:int):
    update_Record=session.get(Student.id)
    update_Record.name=name
    update_Record.family=family
    update_Record.age=age
    session.commit()