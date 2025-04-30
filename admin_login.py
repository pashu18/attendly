from tkinter import *
from tkinter import messagebox
import tkinter as tk
import subprocess

dict1 = {"indus_admin":"12345"}

def forgetpass():
    def reset_password():
        username = username_entry.get()
        new_password = new_password_entry.get()

        if username in dict1:
            dict1[username] = new_password
            messagebox.showinfo("Password Reset", "Password has been reset successfully!")
            root2.destroy()
        else:
            messagebox.showerror("Error", "Invalid username")

    root2 = Toplevel(root)
    root2.title("Forgot Password")
    root2.geometry("300x200")
    root2.configure(bg='#F6F6F6')

    label_font = ("Arial", 12)
    entry_font = ("Arial", 12)
    button_font = ("Arial", 12, "bold")

    label_username = Label(root2, text="Username:", font=label_font, bg='#F6F6F6')
    label_username.pack(pady=(20, 5))
    username_entry = Entry(root2, font=entry_font)
    username_entry.pack(pady=(0, 10), ipadx=20, ipady=3)

    label_new_password = Label(root2, text="New Password:", font=label_font, bg='#F6F6F6')
    label_new_password.pack(pady=(5, 5))
    new_password_entry = Entry(root2, show="*", font=entry_font)
    new_password_entry.pack(pady=(0, 10), ipadx=20, ipady=3)

  
    reset_button = Button(root2, text="Reset Password", command=reset_password, font=button_font, bg='#4CAF50', fg='#FFFFFF')
    reset_button.pack(pady=(10, 20), ipadx=10, ipady=3)


def login():
    username = username_entry.get()
    password = password_entry.get()


    if username in dict1 and dict1[username]==password:
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        execute_file()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
def execute_file():
    try:
        subprocess.run(["python", "mark_attendance.py"])
    except Exception as e:
        print(f"Error executing the file: {e}")

root = tk.Tk()
root.title("PSP_Attendance_App")
root.geometry("1000x800")
root.minsize(200,200)
#root.maxsize(1000,800)
parshwa = Label(text="Hi, Admin\nMark Your Attendance ", font="System 19 bold",borderwidth=3,padx = 15, pady=15, bg="lightblue", fg="black")
parshwa.pack(padx = 30,pady=30,side=TOP,fill=X)
logo = tk.PhotoImage(file="Coll.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=10,padx=10)

username_label = tk.Label(root, text="Username",font="Courier 19 bold",padx=10,pady=10)
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=10)


password_label = tk.Label(root, text="Password", font="Courier 19 bold", padx=10,pady=10 )
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)


login_button = tk.Button(root, text="Login", command=login, height=2, width=10,relief=SUNKEN,borderwidth=3)
login_button.pack(pady=15)
but1 = tk.Button(root,text="Forgot Password?",fg="red",relief=SUNKEN,command=forgetpass)
but1.pack(padx=5,pady=8)

intro=PhotoImage(file = "Psp.png")
intro1 = Label(image = intro)
intro1.pack(side=BOTTOM,padx=5,pady=5,fill=X)

root.mainloop()