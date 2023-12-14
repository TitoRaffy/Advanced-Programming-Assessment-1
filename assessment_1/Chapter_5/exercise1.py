import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}"

    @classmethod
    def oldest_dog_woof(cls, *dogs):
        oldest_dog = max(dogs, key=lambda dog: dog.age)
        messagebox.showinfo("Oldest Dog", f"{oldest_dog.name} woofs! It's the oldest dog.")

def show_dog_info():
    dog1 = Dog(name_entry1.get(), breed_entry1.get(), int(age_entry1.get()))
    dog2 = Dog(name_entry2.get(), breed_entry2.get(), int(age_entry2.get()))

    dog1_info_label.config(text=dog1.display_info())
    dog2_info_label.config(text=dog2.display_info())

    Dog.oldest_dog_woof(dog1, dog2)

root = tk.Tk()
root.title("Dog Information")

# Dog 1
dog1_label = tk.Label(root, text="Dog 1")
dog1_label.pack()

name_label1 = tk.Label(root, text="Name:")
name_label1.pack()
name_entry1 = tk.Entry(root)
name_entry1.pack()

breed_label1 = tk.Label(root, text="Breed:")
breed_label1.pack()
breed_entry1 = tk.Entry(root)
breed_entry1.pack()

age_label1 = tk.Label(root, text="Age:")
age_label1.pack()
age_entry1 = tk.Entry(root)
age_entry1.pack()

# Dog 2
dog2_label = tk.Label(root, text="Dog 2")
dog2_label.pack()

name_label2 = tk.Label(root, text="Name:")
name_label2.pack()
name_entry2 = tk.Entry(root)
name_entry2.pack()

breed_label2 = tk.Label(root, text="Breed:")
breed_label2.pack()
breed_entry2 = tk.Entry(root)
breed_entry2.pack()

age_label2 = tk.Label(root, text="Age:")
age_label2.pack()
age_entry2 = tk.Entry(root)
age_entry2.pack()

info_button = tk.Button(root, text="Show Dog Info", command=show_dog_info)
info_button.pack()

dog1_info_label = tk.Label(root, text="")
dog1_info_label.pack()

dog2_info_label = tk.Label(root, text="")
dog2_info_label.pack()

root.mainloop()