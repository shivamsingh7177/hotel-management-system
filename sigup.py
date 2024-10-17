from tkinter import *
from tkinter import messagebox
import mysql.connector
import os

Window=Tk()
Window.title("sign-up")
Window.geometry('925x500+300+200')
Window.configure(bg="#fff")
Window.resizable(False, False)
        

def signup():
    username = user.get()
    password = code.get()   
    confirm_password = conform_code.get()
    
    if password == confirm_password:
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shivam@7177",
            database="management"
        )
        
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()
        
        if result:
            messagebox.showerror('Invalid', 'Username already exists')
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            messagebox.showinfo('Signup', 'Successfully signed up')
        
        db.close()
    else:
        messagebox.showerror('Invalid', 'Passwords do not match')    
    
def open_login_page():
    Window.destroy()  
    os.system("python LOGIN.py")    
    

img = PhotoImage(file="C:\\Users\\shiva\\OneDrive\\Desktop\\MINI PROJECT\\sigup.png")
Label(Window, image=img, bg='white').place(x=50, y=50)

frame = Frame(Window, width=350, height=390, bg="#fff")
frame.place(x=480, y=50)

heading = Label(frame, text="SIGN-UP", fg='#57a1f8', bg='white', font=("Microsoft YaHei UI Light", 23, 'bold'))
heading.place(x=100, y=5)

# ==============username=============
def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=2, bg='white', font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

frame_username_line = Frame(frame, width=295, height=2, bg='black')
frame_username_line.place(x=25, y=107)

# ==============password=============
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    name=code.get()
    if name == '':
        code.insert(0, 'Password')
        
        
code = Entry(frame, width=25, fg='black', border=2, bg='white', font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

frame_password_line = Frame(frame, width=295, height=2, bg='black')
frame_password_line.place(x=25, y=177)

#============conf- password==========
def on_enter(e):
    conform_code.delete(0,'end')
    
def on_leave(e):
    name=conform_code.get()
    if name == '':
        conform_code.insert(0, 'Conform Password')
        
        
conform_code = Entry(frame, width=25, fg='black', border=2, bg='white', font=("Microsoft YaHei UI Light", 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, 'Conform Password')
conform_code.bind('<FocusIn>', on_enter)
conform_code.bind('<FocusOut>', on_leave)

frame_password_line = Frame(frame, width=295, height=2, bg='black')
frame_password_line.place(x=25, y=247)

#===========button=====

Button(frame, width=39, pady=7, text='Sign-up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=284)
Label(frame, text="I have an account", fg='black', bg='white', font=("Microsoft YaHei UI Light", 9)).place(x=90, y=340)

sign_up = Button(frame, width=6, text='log-in', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=open_login_page)
sign_up.place(x=200, y=340)


Window.mainloop()