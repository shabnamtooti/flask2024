#سوال 1
mysql=select distinct name from student
#سوال 2
import mysql.connector
from contextlib import contextmanager
@contextmanager
def connect_to_db():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    try:
        yield conn
    finally:
        conn.close()
with connect_to_db()as conn:
    cursor=conn.cursor()
    cursor.execute('select*from student')
    for i in cursor.fetchall():
        print(i)
#سوال 3
import mysql.connector
class database:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
    def connect(self):
        if self.conn:
            self.conn.close()
    def fetch_students(self):
        self.connect()
        cursor=self.conn.cursor()
        cursor.execute('select*from students')
        students=cursor.fetchall()
        self.close()
        return students
db=database(
    host='localhost',
    user='root',
    password='',
    database='shabnamtooti')
students=db.fetch_students()
for student in students:
    print(student)             