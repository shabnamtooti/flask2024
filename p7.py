import mysql.connector
class schooldatabase:
    def __init__(self,host,user,password,database):
        self.host=host,
        self.user=user,
        self.password=password,
        self.database=None
    def __enter__(self):
        self.connection=mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.creat_database()
        return self
    def __exit__(self,exc_type,exc_val,exc_traceback):
        if self.connection:
            self.connection.close()
    def creat_database(self):
        cursor=self.connection.cursor()
        cursor.execute(f'creat database if not existe {self.databas}')
        cursor.execute(f'use {self.database}')
        cursor.execute('''
        create tabel if not exists students(
            id int auto_increment primary key,
            name varchar(100),
            age int,
            class varchar(150),
        )
        ''')
        cursor.execute('''
            create tabel if not exists taechers(
            id int auto_increment primary key,
            name varchar(100),
            sunject varchar(100)
        )
        ''')
        cursor.execute('''
            create tabel if not exists scores(
            id int auto_increment primary key,
            stident_id int,
            teacher_id int,
            scores int,
            forening key(student_id)references student(id),
            forening key(teacher_id)references teacher(id),
        )
        ''')
        self.connection.commit()
    def add_student(self,name,age,class_name):
        cursor=self.connection.cursor()
        cursor.execute(
            'insert into student (name,age,class_name)values(%s,%s,%s)',(name,age,class_name))
        self.connection.commit()
    def add_teachar(self,name,subject):
        cursor=self.connection.cursor()
        cursor.execute(
            'insert into teacher (name,subject)values(%s,%s)',(name,subject))
        self.connection.commit()
    def add_score(self,student_id,teacher_id,score):
        cursor=self.connection.cursor()
        cursor.execute(
            'insert into student (student_id,teacher_id,score)values(%s,%s,%s)',(student_id,teacher_id,score))
        self.connection.commit()         
    def get_all_studens(self):
        cursor=self.connection.cursor()
        cursor.execute('select*from students')
        return cursor.fetchall() 
    def get_all_teachers(self):
        cursor=self.connection.cursor()
        cursor.execute('select*from teachers')
        return cursor.fetchall()
    def get_all_scores(self):
        cursor=self.connection.cursor()
        cursor.execute('select*from scores')
        return cursor.fetchall()     
#استفاده از کلاس
if __name__=='__main__':
    db_prrms={
        'host':'localhost',
        'user':'root',
        'password':'',
        'database':'school'
        }       
with schooldatabase(**db_prrms)as db:
    db.add_student('shabi',19,'tooti')  
    db.add_teachar('mr','shahin','tooti')    
    db.add_score(0,1,2)  
    students=db.get_all_studens()
    print('students:',students)
    teachers=db.get_all_teachers()
    print('teachers:',teachers)
    score=db.get_all_scores()
    print('score:',score)