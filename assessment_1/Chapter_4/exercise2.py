import tkinter as tk
from tkinter import messagebox

def count_strings():
    string_to_count = [
        "Hello my name is Peter Parker",
        "I love Python Programming",
        "Love",
        "Enemy"
    ]

    try:
        with open("sentences.txt", "r") as file:
            content = file.read()
            counts = {string: content.count(string) for string in string_to_count}

            result_text = ""
            for string, count in counts.items():
                result_text += f"'{string}' appears {count} times.\n"

            result_label.config(text=result_text)
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'sentences.txt' not found.")

root = tk.Tk()
root.title("Count String Occurrences")

count_button = tk.Button(root, text="Count Strings", command=count_strings)
count_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()