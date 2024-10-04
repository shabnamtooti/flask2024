import mysql.connector
def create_database():
    myconn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='')
    mycursor=myconn.cursor()
    mycursor.execute('CREATE DATABASE IF NOT EXISTS shabnamtooti')
    myconn.close()
def create_table_student():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    mycursor=conn.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS student(
                        scode INT,
                        sname VARCHAR(50),
                        sfamily VARCHAR(50)
                        )
                     ''')
    conn.close()
def create_table_teacher():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    mycursor=conn.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS teacher(
                        tcode INT,
                        tname VARCHAR(50),
                        tfamily VARCHAR(50)
                        )
                     ''')
    conn.close()
def show_tables_student():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    mycursor=conn.cursor()
    mycursor.execute('SHOW TABLES')
    for i in mycursor:
        print(i)
    conn.close()
def show_databases():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='')
    mycursor=conn.cursor()
    mycursor.execute('SHOW DATABASES')
    for i in mycursor:
        print(i)
    conn.close()
def show_student_records():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='')
    database='shabnamtooti)'
    mycursor=conn.cursor()
    mycursor.execute('select *from student')
    for i in mycursor:
        print(i)
def show_teacher_records():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='')
    database=('shabnamtooti')
    mycursor=conn.cursor()
    mycursor.execute('select *from student')
    for i in mycursor:
        print(i)
def insert_into_student(c,n,f):
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    mycursor=conn.cursor()
    sql='insert into student(scode,sname,sfamily)values(%s,%s,%s)'
    val=(c,n,f)
    mycursor.execute(sql,val)
    conn.commit()
def insert_into_teacher(c,n,f):
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    mycursor=conn.cursor()
    sql='insert into teacher(tcode,tname,tfamily)values(%s,%s,%s)'
    val=(c,n,f)
    mycursor.execute(sql,val)
    conn.commit()
def delete_from_student(c):
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    mycursor=conn.cursor()
    try:
        sql='delete from student where scode=%s'
        val=(c,)
        mycursor.execute(sql,val)
        conn.commit()
    except mysql.connector.Error as error:
        print('Error:', error)
def delete_from_teacher(c):
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='shabnamtooti')
    mycursor=conn.cursor()
    try:
        sql='delete from teacher where tcode=%s'
        val=(c,)
        mycursor.execute(sql,val)
        conn.commit()
    except mysql.connector.Error as error:
        print('Error:', error)
create_database()
create_table_student()
create_table_teacher()
while True:
    print('0-Show tables')
    print('1-Show databases')
    print('2-Insert into student')
    print('3-Insert into teacher')
    print('4-Show student records')
    print('5-Show teacher table')
    print('6-Delete from student table')
    print('7-Delete from teacher table')
    print('8-Update student')
    print('9-Update teacher')
    print('10-Exit')
    x=int(input('Enter 1,2,3,4,5,6,7,8,9,10,11:'))
    if x==0:
        show_tables_student()
    elif x==1:
        show_databases()
    elif x==2:
        c,n,f=input('enter code,name,family in one line:').split()
        c=int(c)
        insert_into_student(c,n,f)
    elif x==3:
        c,n,f=input('enter code,name,family in one line:').split()
        c=int(c)
        insert_into_teacher(c,n,f)
    elif x==4:
        show_student_records()
    elif x==5:
        show_teacher_records()
    elif x==6:
        c=int(input('Enter student code to delete:'))
        delete_from_student(c)
    elif x==7:
        c=int(input('Enter teacher code to delete:'))
        delete_from_teacher(c)
    elif x==8:
        pass
    elif x==9:
        pass
    elif x==10:
        pass