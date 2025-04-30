from tkinter import *
import tkinter 
from tkinter import messagebox
import subprocess

root = Tk()
root.title("PSP PROFILE")
root.geometry("1000x800")
root.minsize(200,200)

def execute_file():
     try:
         subprocess.run(["python", "courses.py"])
     except Exception as e:
         print(f"Error executing the file: {e}")
def execute_file1():
     try:
         subprocess.run(["python", "loginpage.py"])
     except Exception as e:
         print(f"Error executing the file: {e}")
def execute_file2():
     try:
         subprocess.run(["python", "TimeTable.py"])
     except Exception as e:
         print(f"Error executing the file: {e}")

def execute_file3():
     try:
         subprocess.run(["python", "view_attendance.py"])
     except Exception as e:
         print(f"Error executing the file: {e}")
def execute_file4():
     try:
         subprocess.run(["python", "User.py"])
     except Exception as e:
         print(f"Error executing the file: {e}")
def course():
    execute_file()
def ret_login():
    execute_file1()
def tt():
    execute_file2()
def att():
    execute_file3()
def done():
    execute_file4()
def reg_form():
    root11 = Tk()
    root11.title("My Profile")
    root11.configure(bg='#EAF6F6')  
    label7 = Label(root11,text="Enter Name:",font=('Arial',10),bg='#EAF6F6')
    label7.pack(pady=10)
    lentry = Entry(root11)
    lentry.pack()
    label8 = Label(root11,text="Student ID:",font=('Arial',10),bg='#EAF6F6')
    label8.pack(pady=10)
    lentry1 = Entry(root11)
    lentry1.pack()
    label9 = Label(root11,text="Gender:",font=('Arial',10),bg='#EAF6F6')
    label9.pack(pady=10)
    lentry2 = Entry(root11)
    lentry2.pack()
    label10 = Label(root11,text="Date of Birth:",font=('Arial',10),bg='#EAF6F6')
    label10.pack(pady=10)
    lentry3 = Entry(root11)
    lentry3.pack()
    label11 = Label(root11,text="Email Id:",font=('Arial',10),bg='#EAF6F6')
    label11.pack(pady=10)
    lentry4 = Entry(root11)
    lentry4.pack()
    label12 = Label(root11,text="Mobile Name:",font=('Arial',10),bg='#EAF6F6')
    label12.pack(pady=10)
    lentry5 = Entry(root11)
    lentry5.pack()
    sub = Button(root11,text="Submit",font="Arial 8 bold",bg='#EAF6F6',borderwidth=5,command=done,width=10,height=2)
    sub.pack(pady=10)
def feedback():
    root20=Tk()
    root20.title("Leave a Feedback")
    root20.configure(bg='#EAF6F6')  
    label22 = Label(root20,text="Give a Feedback:",font=('Arial',14),bg='#EAF6F6',width=20,height=2)
    label22.pack(pady=10)
    lentry22 = Entry(root20,font=('Arial',10))
    lentry22.pack()
    rating_label = Label(root20, text="Ratings:", font=('Arial', 14), bg='#EAF6F6',width=20,height=2)
    rating_label.pack(pady=20)
    rating_var = StringVar(root20)
    rating_var.set("5")
    rating_dropdown = OptionMenu(root20, rating_var, "5", "4","3","2","1")
    rating_dropdown.config(font=('Arial', 12))
    rating_dropdown.pack(pady=(0, 20))
    sub1 = Button(root20,text="Submit",font="Arial 8 bold",bg='#EAF6F6',borderwidth=5,width=10,height=2,command=done)
    sub1.pack(pady=10)
        
f1 = Frame(root,borderwidth=5,bg="grey")
f1.pack(side=LEFT,fill=Y)
lab= Label(f1,text="Profile",font="System 19 bold",bg="Light blue")
lab.pack(padx=100)
but2=Button(f1,padx=10,pady=10,command=reg_form,text="Personal Details",fg="red",bg="white",font="System 10 bold")
but2.pack(side=TOP,pady=60)
but3=Button(f1,padx=10,pady=10,command=ret_login,text="Reset Password",fg="red",bg="white",font="System 10 bold")
but3.pack(side=TOP,pady=60)
but4=Button(f1,padx=10,pady=10,command=feedback,text="Leave a Feedback",fg="red",bg="white",font="System 10 bold")
but4.pack(side=TOP,pady=60)
but1 = Button(f1,padx=10,pady=10,command=ret_login,text="Log Out",fg="red",bg="white",font="System 10 bold")
but1.pack(side=BOTTOM,pady=60)
f2= Frame(root,borderwidth=1)
f2.pack(side=TOP,fill=X,padx=10,pady=10)
logo1 = PhotoImage(file="Coll.png")
logo_label1 = Label(f2, image=logo1)
logo_label1.pack(pady=2,padx=2)
la1 = Label(f2,text="Indus Institute Of Technology and Engineering-Ahmedabad",font="Arial 10 bold")
la1.pack(padx=2,pady=2)
button1 = Button(root,text=" My Courses ",font = "System 19 bold",borderwidth=20,padx=100,pady=50,bg="light green",fg="black",command=course)
button1.pack(side=TOP)
button2 = Button(root,text="  Attendance  ",font = "System 19 bold",borderwidth=20,padx=100,pady=50,bg="light green",fg="black",command=att)
button2.pack(side=TOP)
button3 = Button(root,text="  Time Table  ",font = "System 19 bold",borderwidth=20,padx=100,pady=50,bg="light green",fg="black",command=tt)
button3.pack(side=TOP)
root.mainloop()