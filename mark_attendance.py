import tkinter as tk
from tkcalendar import Calendar
import csv

def mark_attendance():
    enrollment = enrollment_var.get()
    subject = subject_var.get()
    status = status_var.get()
    date = cal.get_date()

    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([enrollment, subject, status, date])

root = tk.Tk()
root.title("Mark Attendance")
root.geometry("400x350")
root.configure(bg='#EAF6F6')  

logo = tk.PhotoImage(file="Coll.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=5, padx=10)

enrollment_label = tk.Label(root, text="Enrollment Number:", font=('Arial', 12), bg='#EAF6F6')
enrollment_label.pack(pady=(20, 5))

enrollment_var = tk.StringVar(root)
enrollment_var.set("Select Enrollment")
enrollment_numbers = [f"IU21412302{i}" for i in range(13, 81)]
enrollment_dropdown = tk.OptionMenu(root, enrollment_var, *enrollment_numbers)
enrollment_dropdown.config(font=('Arial', 12))
enrollment_dropdown.pack(pady=(0, 20))

subject_label = tk.Label(root, text="Subject:", font=('Arial', 12), bg='#EAF6F6')
subject_label.pack()
subject_var = tk.StringVar(root)
subject_var.set("DAA")  
subjects = ["DAA", "Python", "Advance Microprocessor", "Web Technology", "Computer Networks"]
subject_dropdown = tk.OptionMenu(root, subject_var, *subjects)
subject_dropdown.config(font=('Arial', 12))
subject_dropdown.pack(pady=(0, 20))

status_label = tk.Label(root, text="Status:", font=('Arial', 12), bg='#EAF6F6')
status_label.pack()
status_var = tk.StringVar(root)
status_var.set("Present")
status_dropdown = tk.OptionMenu(root, status_var, "Present", "Absent")
status_dropdown.config(font=('Arial', 12))
status_dropdown.pack(pady=(0, 20))

cal = Calendar(root, selectmode="day", year=2023, month=10, day=18, font=('Arial', 12))
cal.pack(pady=(0, 20))

mark_button = tk.Button(root, text="Mark Attendance", command=mark_attendance, font=('Arial', 12))
mark_button.pack()

root.mainloop()
