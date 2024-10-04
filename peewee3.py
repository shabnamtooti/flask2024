from peewee import IntegerField,CharField,Model,ForeignKeyField,SqliteDatabase
db=SqliteDatabase('school1.db')
class student(Model):
    id=IntegerField(primary_key=True)
    name=CharField(max_length=50)
    age=IntegerField()
    class_name=CharField(max_length=50)
    class Meta:
        database=db
        db_tables='Students'
class Teacher(Model):
    id=IntegerField(primary_key=True)
    name=CharField(max_length=50)
    age=IntegerField()
    subject=CharField(max_length=50)
    class Meta:
        database=db
        db_table='Teachers'
class Scores (Model):
    id=IntegerField(primary_key=True)
    student_id=ForeignKeyField(student)
    Teacher_id=ForeignKeyField(Teacher)
    class Meta:
        database=db
        db_table='Scores'
db.create_tables([student,Teacher,Scores])        
class C:
    def insert_student(n,a,cn):
        try:
            s=student(name=n,age=a,class_name=cn)
            s.save()
            if s:
                return 'insert successfully'
            else:
                return 'error'
        except Exception as e:
            return e
        except:
            return 'error'
    def insert_teacher(n,a,s):
        try:
            t=Teacher(name=n,age=a,subject=s)
            t.save()
            if t:
                return 'insert successfully'
            else:
                return 'error'
        except Exception as e:
            return e
        except:
            return 'error'
    def insert_score(ti,si,s):
        try:
            s=Scores(student_id=si,Teacher_id=ti,Score=s)
            s.save()
            if s:
                return 'insert successfully'
            else:
                return 'error'
        except Exception as e:
            return e
        except:
            return 'error'
class R:
    def get_all_students():
        try:
            s=student.select()
            for i in s:
                print(f'id={i},name={i},age={i},class_name{i}')
        except Exception as e:
            return e
        except:
            return 'error'
    def get_all_teachers():
        try:
            t=Teacher.select()
            print(type(t))
            for i in t:
                print(f'id={i.id},name={i.name},age={i.age},subjec{i.subject}')
        except Exception as e:
            return e
        except:
            return 'error'
    def get_all_scores():
        try:
            s=Scores.select()
            for i in s:
                print(f'id={i.id},student_id={i.student_id},teacher_id={i.teacher_id}')  
        except Exception as e:
            return e
        except:
            return 'error'