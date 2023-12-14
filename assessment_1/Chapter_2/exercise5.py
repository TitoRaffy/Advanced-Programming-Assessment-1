from tkinter import *

# Functions for arithmetic operations
def add():
    result = float(first_number.get()) + float(second_number.get())
    result_label.config(text="Result: " + str(result))

def subtract():
    result = float(first_number.get()) - float(second_number.get())
    result_label.config(text="Result: " + str(result))

def multiply():
    result = float(first_number.get()) * float(second_number.get())
    result_label.config(text="Result: " + str(result))

def divide():
    result = float(first_number.get()) / float(second_number.get())
    result_label.config(text="Result: " + str(result))

def modulo():
    result = float(first_number.get()) % float(second_number.get())
    result_label.config(text="Result: " + str(result))

# Create the main window
window = Tk()
window.title("Basic Arithmetic Operations")

# Create widgets
first_number = Entry(window)
second_number = Entry(window)

first_number.grid(row=0, column=1)
second_number.grid(row=1, column=1)

result_label = Label(window)
result_label.grid(row=2, column=1)

add_button = Button(window, text="Add", command=add)
subtract_button = Button(window, text="Subtract", command=subtract)
multiply_button = Button(window, text="Multiply", command=multiply)
divide_button = Button(window, text="Divide", command=divide)
modulo_button = Button(window, text="Modulo", command=modulo)

add_button.grid(row=3, column=0)
subtract_button.grid(row=4, column=0)
multiply_button.grid(row=5, column=0)
divide_button.grid(row=6, column=0)
modulo_button.grid(row=7, column=0)

# Run the main event loop
window.mainloop()