import tkinter as tk
from tkinter import messagebox

def write_bio():
    name = name_entry.get()
    age = age_entry.get()
    hometown = hometown_entry.get()

    with open("bio.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

    messagebox.showinfo("Success", "Bio has been written to bio.txt")

def read_bio():
    try:
        with open("bio.txt", "r") as file:
            content = file.read()
            bio_output.config(text=content)
    except FileNotFoundError:
        messagebox.showerror("Error", "Bio file not found. Please write your bio first.")

root = tk.Tk()
root.title("Bio Information")

name_label = tk.Label(root, text="Enter Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Enter Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

hometown_label = tk.Label(root, text="Enter Hometown:")
hometown_label.pack()

hometown_entry = tk.Entry(root)
hometown_entry.pack()

write_button = tk.Button(root, text="Write to File", command=write_bio)
write_button.pack()

read_button = tk.Button(root, text="Read from File", command=read_bio)
read_button.pack()

bio_output = tk.Label(root, text="")
bio_output.pack()

root.mainloop()