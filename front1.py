from tkinter import Entry,Tk,Label,Button,Toplevel,END
from tkinter import messagebox
from back1 import Database
class loginApp:
    def __init__(self,master,db):
        self.master=master
        self.db=db
        self.master.title('login window')
        self.master.geometry('300x200')
        self.label_username=Label(master,text='username:')
        self.label_username.pack(pady=10)
        self.entry_username=Entry(master)
        self.entry_username.pack(pady=5)
        self.label_password=Label(master,text='password:')
        self.label_password.pack(pady=10)
        self.entry_password=Entry(master,show='*')
        self.entry_password.pack(pady=5)
        self.button_login=Button(master,text='login',command=self.login)
        self.button_login.pack(pady=5)
        self.button_save=Button(master,text='save',command=self.save_user)
        self.button_save.pack(pady=5)
    def login(self):
        username=self.entry_username.get()
        password=self.entry_password.get()
        if self.db.validata_user(username,password):
            messagebox.showinfo('login','login successful!')
            self.master.destory()
            CrudApp(self.db)
        else:
            messagebox.showerror('login','invalid credentials!')
    def save_user(self):
        username=self.entry_username.get()
        password=self.entry_password.get()
        if self.db.save_user(username,password):
            messagebox.showinfo('save','user saved successfully! ')
        else:
            messagebox.showerror('save','user alreaddy exists!')
class CrudApp:
    def __init__(self,db):
        self.master=Tk()
        self.master=title('school manegment crud')
        self.master=geometry('400x300')
        self.db=db
        self.lable_title=Label(self.master,text='school manegment system',font=('arial',16))
        self.lable_title.pack(pady=20)
        self.button_students=Button(self.master,text='manage students',command=self.manage_students)
        self.button_students.pack(pady=10)
        self.button_instuctors=Button(self.master,text='manage instuctors',command=self.manage_instuctors)
        self.lable_title.pack(pady=10)
        self.button_scores=Button(self.master,text='manage scores',command=self.button_scores)
        self.button_scores.pack(pady=10)
        self.master.maianloop()
    def manage_students(self):
        students_window=Toplevel(self.master)
        students_window.title=('manage students')
        students_window.geometry=('300x300')
        self.lable_students=Label(students_window,text='student name:')
        self.lable_students.pack(pady=10)
        self.entry_students_name=Entry(students_window)
        self.entry_students_name.pack(pady=5)
        self.entry_students_name=Entry(students_window)
        self.entry_students_name.pack(pady=5)
        self.button_add_student=Button(students_window,text='Add Student',command=self.add_student)
        self.button_add_student.pack(pady=5)
        self.button_view_students=Button(students_window,text='View Students,command=self.view_students)
        self.button_view_students.pack(pady-5)
        def add_student(self):
            name=self.entry_student_name.get()
            if name:
                self.db.add_student(name)messagebox.showinfo('Success','Student added successfully!')
                self.entry_student_name.delete(0,END)
                def view_students(self):
                    students=self.db.view_students()
                    students_list="\n".join([f'(student[0]):(student[1]}'for student in students])
messagebox.showinfo