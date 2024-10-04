from peewee import SqliteDatabase,Model,CharField,ForeignKeyField,IntegerField
db=SqliteDatabase('school_management.db')
class Basemodel(Model):
    class Meta:
        database=db
class Student(Basemodel):
    name=CharField()
class Teacher(Basemodel):
    name=CharField()  
class Score(Basemodel):
    Student=ForeignKeyField(Student,backref='score')
    Teacher=ForeignKeyField(Teacher,backref='score')
    Score=IntegerField()
    Subject=CharField()
db.connect()
db.create_tables([Student,Teacher,Score])