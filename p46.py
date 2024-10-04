from tkinter import Tk,Label,Entry,Button
window=Tk()
def myfun():
    U=txtuser.get()
    P=txtpass.get()
    if U=='shabi' and P=='100':
        Label3.config(text='ok',bg='red',fg='black')
    else:
        Label3.config(text='ok',bg='green',fg='gold')
Label1=Label(window,text='enter name:')
Label1.grid(row=0,column=0)
Label2=Label1(window,text='enter password:')
Label2.grid(row=1,column=0)
btn1=Button(window,text='ok',command=myfun)
btn1.grid(row=2,column=0)
txtuser=Entry(window)
txtuser.grid(row=0,column=1)
txtpass=Entry(window,show='*')
txtpass.grid(row=1,column=1)
Label3=Label1(window,text='')
Label3.grid(row=2,column=1)
window.mainloop()