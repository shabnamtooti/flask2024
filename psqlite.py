import sqlite3
class schooldatabase:
    def __init__(self,database):
        self.Connection=sqlite3.connect(database)
        self.cursor=self.Connection.cursor()
    def __enter__(self):
        self.create_tables()
        return self
    def __exit__(self,*args,**kwargs):
        if self.Connection:
            self.Connection.commit()
            self.Connection.close()
    def create_tables(self):
        self.cursor.execute('''
        create table if not exists students(
            id integer primary key autoincrement,
            name varchar(100) not null,
            age integer not null,
            class varchar(150)
) 
''')
        self.cursor.execute('''
        create table if not exists teachers(
            id integer primary key autoincrement,
            name varchar(100) not null,
            age integer not null
) 
''')
        self.cursor.execute('''
        create table if not exists scores(
            id integer primary key autoincrement,
            stident_id integer,
            teacher_id integer,
            scores integer,
            forening key(student_id)references student(id),
            forening key(teacher_id)references teacher(id)
)
''')
    def add_student(self,name,age,class_name):
        self.cursor.execute(
            'insert into student(name,age,class)values(?,?,?)',(name,age,class_name))
    def add_teacher(self,name,subject):
        self.cursor.execute(
            'insert into teacher(name,age,subject)values(?,?,?)',(name,subject))
    def add_score(self,sid,tid,s):
        self.cursor.execute(
            'insert into(student_id,teacher_id,score)values(?,?,?)',(sid,tid,s))
    def get_all_students(self):
        return self.cursor.execute('select*from students').fetchall()
    def get_all_teachers(self):
        return self.cursor.execute('select*from teachers').fetchall()
    def get_all_scores(self):
        return self.cursor.execute('select*from scores').fetchall()
    def delete_from_students(self):
        a=self.cursor.execute('select*from students where id=?',(id))
        if a.fetchone()is not None:
            self.cursor.execute('delete from students where id=?',(id))
        else:
            print('not found')
    def delete_from_teachers(self):
        a=self.cursor.execute('select*from teachers where id=?',(id))
        if a.fetchone()is not None:
            self.cursor.execute('delete from teachers where id=?',(id))
        else:
            print('not found')
    def delete_from_scores(self):
        a=self.cursor.execute('select*from scores where id=?',(id))
        if a.fetchone()is not None:
            self.cursor.execute('delete from scores where id=?',(id))
        else:
            print('not found')
    def updata_students_name(self):
        a=self.cursor.execute('select*from students where id=?',(id))
        if a.fetchone()is not None:
            self.cursor.execute('updata from students where id=?',(id))
            print('record updata success fully')
        else:
            print('not found!')
    def updata_teachers_name(self):
        a=self.cursor.execute('select*from teachers where id=?',(id))
        if a.fetchone()is not None:
            self.cursor.execute('updata from teachers where id=?',(id))
            print('record updata success fully')
        else:
            print('not found!')
    def update_score_score(self,id1,id2,id3,score):
        a=self.cursor.execute('select*from scores where id=?',(id1,))
        if a.fetchone()is not None:
            b=self.cursor.execute(
                'select*from students where id=?',(id2,))
            if b.fetchone()is not None:
                c=self.cursor.execute(
                    'select*from teachers where id=?',(id3,))
                if c.fetchone()is not None:
                    self.cursor.execute(
                        f'update scores set score={score}where id={id1}and student_id={id2}and teacher_id={id3}')
                    print('record updated success fully')
                else:
                    print('not found this teacher!')
            else:
                print('not found this student!')
        else:
            print('not found this score!')
if __name__=='__main__':
    database='school.db'
    with schooldatabase(database)as db:
        #db.add_student('shabi',19,'classA')
        #db.add_teacher('reza','physice')  
        #db.add_score(0,1,2)
        #print(db.get_all_scores())
        db.updata_score_score(0,1,2,3)