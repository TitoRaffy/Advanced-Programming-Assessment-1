import tkinter as tk
from tkinter import messagebox

def login(): # user inputs username and password from here
    username = user_entry.get()
    password = pwd_entry.get()

    if username == 'admin' and password == 'password': # if you type admin as your user and "password" as your password, you will be welcomed as an admin
        messagebox.showinfo('Login successful', 'Welcome, ' + username + '!')
    else:
        messagebox.showerror('Login failed', 'Invalid credentials') # any other credentials other then "admins" credentials, you will not be able to enter

root = tk.Tk()
root.title('Login')
root.geometry('300x200')

# to configure columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# this is the overall theme and appearance for the whole texts and GUI
tk.Label(root, text='Login', bg='lightblue', font=('Arial', 16)).grid(row=0, column=0, columnspan=2, sticky='nsew')

tk.Label(root, text='Username:', bg='lightgray', font=('Arial', 12)).grid(row=1, column=0, sticky='w')
tk.Label(root, text='Password:', bg='lightgray', font=('Arial', 12)).grid(row=2, column=0, sticky='w')

user_entry = tk.Entry(root, font=('Arial', 12))
pwd_entry = tk.Entry(root, font=('Arial', 12), show='*')

user_entry.grid(row=1, column=1, sticky='ew')
pwd_entry.grid(row=2, column=1, sticky='ew')

login_button = tk.Button(root, text='Login', command=login, bg='pink', fg='white', font=('Arial', 12), activebackground='pink')
login_button.grid(row=3, column=0, columnspan=2, sticky='nsew')

root.mainloop()