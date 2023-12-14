import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calc_grade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        grade_average = self.calc_grade()
        return f"Name: {self.name}, Grade Average: {grade_average:.2f}"

def create_student():
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())

    student = Students(name, mark1, mark2, mark3)
    result_label.config(text=student.display())

root = tk.Tk()
root.title("Student Information")

name_label = tk.Label(root, text="Enter Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

mark1_label = tk.Label(root, text="Enter Mark 1:")
mark1_label.pack()

mark1_entry = tk.Entry(root)
mark1_entry.pack()

mark2_label = tk.Label(root, text="Enter Mark 2:")
mark2_label.pack()

mark2_entry = tk.Entry(root)
mark2_entry.pack()

mark3_label = tk.Label(root, text="Enter Mark 3:")
mark3_label.pack()

mark3_entry = tk.Entry(root)
mark3_entry.pack()

create_button = tk.Button(root, text="Create Student", command=create_student)
create_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()