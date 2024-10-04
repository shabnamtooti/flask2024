import sqlite3
class Database:
    def __init__(self):
        self.conn=sqlite3.connect('school_managment.db')
        self.create_tables()
    def creat_tables(self):
        cursor=self.conn.cursor()
        cursor.execute('''creat table if not exists user(
            id integer primary key autoincrement,
            username text unique,
            password text
        )''')
        self.conn.commit()
        cursor.execute('''creat table if not exists studens(
            id integer primary key autoincrement,
            text name
        )''')
        cursor.execute('''creat table if not exists instructors(
            id integer primary key autoincrement,
            text name
        )''')
        cursor.execute('''creat table if not exists scores(
            id integer primary key autoincrement,
            student_id integer,
            score integer,
            foreign key(student_id)references student(id)
        )''')
    def save_user(self,username,password):
        cursor=self.conn.cursor()
        try:
            cursor.execute('insert into user(username,password)valuse(?,?)',(username,password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    def validata_user(self,username,password):
        cursor=self.conn.cursor()
        cursor.execute('select*from users where username=?and password=?',(username,password))
        return cursor.fetchall()is not None
    def add_stident(self,name):
        cursor=self.conn.cursor()
        cursor.execute('insert into students(name)valuse(?)',(name))
        self.conn.commit()
    def view_students(self):
        cursor=self.conn.cursor()
        cursor.execute('select*from students')
        return cursor.fetchall()
    def add_instrutor(self,name):