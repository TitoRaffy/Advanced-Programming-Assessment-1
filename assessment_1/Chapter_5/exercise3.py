import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.id = 0
        self.salary = 0.0

    def set_data(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.id = employee_id
        self.salary = salary

    def get_data(self):
        return f"{self.name}\t\t{self.age}\t{self.salary}\t{self.id}"

employees = []

def add_employee():
    name = name_entry.get()
    age = int(age_entry.get())
    employee_id = int(id_entry.get())
    salary = float(salary_entry.get())

    employee = Employee()
    employee.set_data(name, age, employee_id, salary)
    employees.append(employee)
    clear_entries()

def display_employees():
    header = "Name\tAge\tSalary\tID\n"
    employee_info = header + "\n".join([employee.get_data() for employee in employees])
    messagebox.showinfo("Employee Details", employee_info)

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Employee Management")

name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

id_label = tk.Label(root, text="ID:")
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

salary_label = tk.Label(root, text="Salary:")
salary_label.pack()

salary_entry = tk.Entry(root)
salary_entry.pack()

add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.pack()

display_button = tk.Button(root, text="Display Employees", command=display_employees)
display_button.pack()

root.mainloop()