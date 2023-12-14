import tkinter as tk
from tkinter import messagebox

def validate_password():
    password = password_entry.get()
    attempts_left = 5

    while attempts_left > 0:
        if (6 <= len(password) <= 12 and
                any(char.islower() for char in password) and
                any(char.isupper() for char in password) and
                any(char.isdigit() for char in password) and
                any(char in "$#@%" for char in password)):
            messagebox.showinfo("Success", "Password is valid!")
            break
        else:
            attempts_left -= 1
            if attempts_left > 0:
                messagebox.showwarning("Invalid Password",
                                       f"Invalid password! {attempts_left} attempts remaining.")
                password = password_entry.get()
            else:
                messagebox.showerror("Alert", "Authorities have been alerted!")
                break

root = tk.Tk()
root.title("Password Validator")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # Show * for password entry
password_entry.pack()

validate_button = tk.Button(root, text="Validate Password", command=validate_password)
validate_button.pack()

root.mainloop()