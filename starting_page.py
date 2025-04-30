from tkinter import *
from tkinter import messagebox
import tkinter as tk
import subprocess

def admin():
    execute_file10()

def student():
    execute_file11()

def execute_file10():
    try:
        subprocess.run(["python", "admin_login.py"])
    except Exception as e:
        print(f"Error executing the file: {e}")

def execute_file11():
    try:
        subprocess.run(["python", "loginpage.py"])
    except Exception as e:
        print(f"Error executing the file: {e}")

root = tk.Tk()
root.title("PSP Attendance App")
root.geometry("1000x800")
root.minsize(200,200)

logo10 = tk.PhotoImage(file="Coll.png")
logo11_label = tk.Label(root, image=logo10)
logo11_label.pack(pady=50, padx=10)

admin_button = tk.Button(root, text="Admin", height=5, width=30, relief=SUNKEN, borderwidth=20, background="lightgreen", font=("Arial", 14), command=admin)
admin_button.pack(pady=20)

user_button = tk.Button(root, text="Student", height=5, width=30, relief=SUNKEN, borderwidth=20, background="lightgreen", font=("Arial", 14), command=student)
user_button.pack(pady=20)

intro10=PhotoImage(file = "Psp.png")
intro11 = Label(image = intro10)
intro11.pack(side=BOTTOM,padx=5,pady=5,fill=X)

root.mainloop()
