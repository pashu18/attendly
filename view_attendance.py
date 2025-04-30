import tkinter as tk
from tkcalendar import Calendar
import csv
import matplotlib.pyplot as plt

def generate_pie_chart():
    selected_date = cal.get_date()
    attendance = get_attendance_for_date(selected_date)
    if attendance:
        update_attendance_text(attendance)
    else:
        attendance_text.set(f"No records found for {selected_date}")
    generate_monthly_bar_chart()

def get_attendance_for_date(selected_date):
    enrollment = enrollment_var.get()
    subject = subject_var.get()
    try:
        with open('attendance.csv', mode='r') as file:
            reader = csv.reader(file)
            attendance = [row for row in reader if len(row) >= 4 and row[0] == enrollment and row[1] == subject and row[3] == selected_date]
            return attendance
    except FileNotFoundError:
        return []

def update_attendance_text(attendance):
    status = attendance[0][2]
    date = attendance[0][3]
    attendance_text.set(f'Status: {status}, Date: {date}')

def generate_monthly_bar_chart():
    enrollment = enrollment_var.get()
    subject = subject_var.get()
    try:
        with open('attendance.csv', mode='r') as file:
            reader = csv.reader(file)
            attendance = [row for row in reader if len(row) >= 4 and row[0] == enrollment and row[1] == subject]
            dates = [row[3] for row in attendance]
            status_counts = {'Present': 0, 'Absent': 0}
            for row in attendance:
                status_counts[row[2]] += 1
            
            labels = status_counts.keys()
            values = status_counts.values()

            plt.bar(labels, values)
            plt.xlabel('Status')
            plt.ylabel('Count')
            plt.title('Monthly Attendance')
            plt.show()
    except FileNotFoundError:
        pass


root = tk.Tk()
root.title("Attendance")
root.geometry("600x400")
root.configure(bg='#F6EFEF')  

logo = tk.PhotoImage(file="Coll.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=5,padx=10)

enrollment_label = tk.Label(root, text="Enrollment Number:", font=('Arial', 12), bg='#F6EFEF')
enrollment_label.pack(pady=(20, 5))

enrollment_var = tk.StringVar(root)
enrollment_var.set("Select Enrollment")
enrollment_numbers = [f"IU21412302{i}" for i in range(13, 81)]
enrollment_dropdown = tk.OptionMenu(root, enrollment_var, *enrollment_numbers)
enrollment_dropdown.config(font=('Arial', 12))
enrollment_dropdown.pack(pady=(0, 20))

subject_label = tk.Label(root, text="Subject:", font=('Arial', 12), bg='#F6EFEF')
subject_label.pack()
subject_var = tk.StringVar(root)
subject_var.set("DAA")  
subjects = ["DAA", "Python", "Advance Microprocessor", "Web Technology", "Computer Networks"]
subject_dropdown = tk.OptionMenu(root, subject_var, *subjects)
subject_dropdown.config(font=('Arial', 12))
subject_dropdown.pack(pady=(0, 20))

cal = Calendar(root, selectmode="day", year=2023, month=10, day=18, font=('Arial', 12))
cal.pack(pady=(0, 20))

view_button = tk.Button(root, text="View Attendance", command=generate_pie_chart, font=('Arial', 12))
view_button.pack()

attendance_text = tk.StringVar()
attendance_label = tk.Label(root, textvariable=attendance_text, font=('Arial', 14), bg='#F6EFEF')
attendance_label.pack()

root.mainloop()
