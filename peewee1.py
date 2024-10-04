from peewee import*
db=SqliteDatabase('school1.db')
class Student(Model):
    id=TextField(unique=True)
    sname=TextField()
    sfamily=CharField(max_length=5)
    age=IntegerField()
    class Meta:
        database=db
        db_table='student'
Student.create_table()
#solution1
st1=Student(sname='ali',sfamily='ahmadi',age=15)
st1.save()
#solution2
Student.create(sname='ahmad',sfamily='mohammadi',age=18)
#solution3
st1=Student.insert(sname='reza',sfamily='salehi',age=19)
st1.execute()
print(st1.sql())
Student=Student.select()
for i in Student:
    print(i.sname)
s=Student.delete()
s.execute()