from tkinter import *
from tkinter import messagebox
import tkinter as tk
import subprocess

dict1 = {"IU2141230213":"indus213","IU2141230214":"indus214","IU2141230215":"indus215","IU2141230216":"indus216","IU2141230217":"indus217","IU2141230218":"indus218","IU2141230219":"indus219","IU2141230220":"indus220"
         ,"IU2141230221":"indus221","IU2141230222":"indus222","IU2141230223":"indus223","IU2141230224":"indus224","IU2141230225":"indus225","IU2141230226":"indus226","IU2141230227":"indus227","IU2141230228":"indus228","IU2141230229":"indus229","IU2141230230":"indus230"
         ,"IU2141230231":"indus231","IU2141230232":"indus232","IU2141230233":"indus233","IU2141230234":"indus234","IU2141230235":"indus235","IU2141230236":"indus236","IU2141230237":"indus237","IU2141230238":"indus238","IU2141230239":"indus239","IU2141230240":"indus240"
         ,"IU2141230241":"indus241","IU2141230242":"indus242","IU2141230243":"indus243","IU2141230244":"indus244","IU2141230245":"indus245","IU2141230246":"indus246","IU2141230247":"indus247","IU2141230248":"indus248","IU2141230249":"indus249","IU2141230250":"indus250"
         ,"IU2141230251":"indus251","IU2141230252":"indus252","IU2141230253":"indus253","IU2141230254":"indus254","IU2141230255":"indus255","IU2141230256":"indus256","IU2141230257":"indus257","IU2141230258":"indus258","IU2141230259":"indus259","IU2141230260":"indus260"
         ,"IU2141230261":"indus261","IU2141230262":"indus262","IU2141230263":"indus263","IU2141230264":"indus264","IU2141230265":"indus265","IU2141230266":"indus266","IU2141230267":"indus267","IU2141230268":"indus268","IU2141230269":"indus269","IU2141230270":"indus270"
         ,"IU2141230271":"indus271","IU2141230272":"indus272","IU2141230273":"indus273","IU2141230274":"indus274","IU2141230275":"indus275","IU2141230276":"indus276","IU2141230277":"indus277","IU2141230278":"indus278","IU2141230279":"indus279","IU2141230280":"indus280"
         }

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

        # Reset Button
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
        subprocess.run(["python", "User.py"])
    except Exception as e:
        print(f"Error executing the file: {e}")

root = tk.Tk()
root.title("PSP_Attendance_App")
root.geometry("1000x800")
root.minsize(200,200)
#root.maxsize(1000,800)
parshwa = Label(text="Hi,Indusian\nTrack Your Attendance ", font="System 19 bold",borderwidth=3,padx = 15, pady=15, bg="lightblue", fg="black")
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