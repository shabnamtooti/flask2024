from peewee import IntegerField, CharField, Model, ForeignKeyField, SqliteDatabase
db=SqliteDatabase('school1.db')
class Student(Model):
    id=IntegerField(primary_key=True)
    name=CharField(max_length=10) # Corrected field name
    age=IntegerField()
    class_name=CharField(max_length=15)
    class Meta:
        database=db
        db_table='students'
    def __str__(self):
        return f'id={id},name={name},age={age},class_name={class_name}'
class Teacher(Model):
    id=IntegerField(primary_key=True)
    name=CharField(max_length=10) # Corrected field name
    age=IntegerField()
    subject=CharField(max_length=15) # Corrected field name
    class Meta:
        database=db
        db_table='teachers'
class Score(Model):
    id=IntegerField(primary_key=True)
    student_id=ForeignKeyField(Student) # Corrected field name
    teacher_id=ForeignKeyField(Teacher) # Corrected field name
    score=IntegerField() # Added missing field
    class Meta:
        database=db
        db_table='scores'

db.create_tables([Student,Teacher,Score])

#Rest of your code(insert functions,retrieval functions)goes here
#Example usage:#C.insert_student('John',18,'Math')
#C.insert_teacher('Mr.Smith',35,'Physics')
#C.insert_score(1,1,90)
#R.get_all_students()
#R.get_all_teachers()