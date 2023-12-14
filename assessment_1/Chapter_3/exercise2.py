from tkinter import *
from tkinter import messagebox

def show_order(): # this is basically the whole receipt of the coffee that the user ordered
    name = name_entry.get()
    choose_size = size_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()
    coffee_size = "Small" if choose_size == "Small" else "Large"
    message = f"Hello, {name}! Here is your {coffee_size} coffee with {sugar} sugar and {milk} milk."
    messagebox.showinfo("Order Details", message)

# creates the whole GUI window
window = Tk()

# creates the frame for the GUI, this is basically the whole appearance
input_frame = Frame(window, bg="crimson")
input_frame.pack(padx=10, pady=10)

# user enters his/her name for their coffee
name_label = Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0)

name_entry = Entry(input_frame)
name_entry.grid(row=0, column=1)

# the user then chooses the size for the coffee to their own liking
size_label = Label(input_frame, text="Select a coffee size: ")
size_label.grid(row=2, column=0)

size_var = StringVar()
size_menu = OptionMenu(input_frame, size_var, "Small", "Large")
size_menu.grid(row=2, column=1)

# the user will choose the amount of sugar they want to add
sugar_label = Label(input_frame, text="Sugar:")
sugar_label.grid(row=3, column=0)

sugar_var = StringVar()
sugar_menu = OptionMenu(input_frame, sugar_var, "0", "1", "2")
sugar_menu.grid(row=3, column=1)

# same here, users will choose the amount of milk
milk_label = Label(input_frame, text="Milk:")
milk_label.grid(row=4, column=0)

milk_var = StringVar()
milk_menu = OptionMenu(input_frame, milk_var, "0", "1", "2")
milk_menu.grid(row=4, column=1)

# and finally once you place an order, everything will printed as par the "def" function above
order_button = Button(input_frame, text="Place Order", command=show_order)
order_button.grid(row=5, column=0, columnspan=2)

# Run the main event loop
window.mainloop()