from tkinter import *

def update_greeting():
    username = input_name.get()
    color = color_var.get()
    greeting = f"Hello, {username}! Nice to see you."
    greeting_label.config(text=greeting, fg=color)

# create the main window
win = Tk()

# create the input frame
frame = Frame(win, bg="light blue")
frame.pack(padx=10, pady=10)

name_label = Label(frame, text="Name:")
name_label.grid(row=0, column=0)

input_name = Entry(frame)
input_name.grid(row=0, column=1)

color_label = Label(frame, text="Select a color:")
color_label.grid(row=1, column=0)

color_var = StringVar()
color_menu = OptionMenu(frame, color_var, "red", "green", "blue", "yellow", "orange")
color_menu.grid(row=1, column=1)

up_btn = Button(frame, text="Update Greeting", command=update_greeting)
up_btn.grid(row=2, column=0, columnspan=2)

# Create the display frame
display_frame = Frame(win, bg="light green")
display_frame.pack(padx=10, pady=10)

greeting_label = Label(display_frame, text="", wraplength=300)
greeting_label.pack()

# Run the main event loop
win.mainloop()