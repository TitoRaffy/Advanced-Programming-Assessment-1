import tkinter as tk
from tkinter import messagebox

def count_character():
    user_input = char_entry.get()
    try:
        with open("sentences.txt", "r") as file:
            content = file.read()
            count = content.count(user_input)
            result_label.config(text=f"The character '{user_input}' appears {count} times.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'sentences.txt' not found.")

root = tk.Tk()
root.title("Count Character Occurrences")

char_label = tk.Label(root, text="Enter a character:")
char_label.pack()

char_entry = tk.Entry(root)
char_entry.pack()

count_button = tk.Button(root, text="Count Character", command=count_character)
count_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()