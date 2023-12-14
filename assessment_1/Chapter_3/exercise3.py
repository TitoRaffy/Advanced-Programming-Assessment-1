import tkinter as tk
from tkinter import ttk, messagebox
import math

def calculate_circle_area():
    try:
        radius = float(radius_circle.get())
        area = math.pi * (radius ** 2)
        circle_result.config(text=f"Area of Circle: {area:.2f} square units")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid radius.")

def calculate_square_area():
    try:
        side = float(side_square.get())
        area = side ** 2
        square_result.config(text=f"Area of Square: {area:.2f} square units")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid side length.")

def calculate_rectangle_area():
    try:
        length = float(length_rect.get())
        width = float(width_rect.get())
        area = length * width
        rectangle_area_result.config(text=f"Area of Rectangle: {area:.2f} square units")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid length and width.")

root = tk.Tk()
root.title("Area Calculator")

tab_control = ttk.Notebook(root)

circle_tab = ttk.Frame(tab_control)
square_tab = ttk.Frame(tab_control)
rectangle_tab = ttk.Frame(tab_control)

tab_control.add(circle_tab, text='Circle')
tab_control.add(square_tab, text='Square')
tab_control.add(rectangle_tab, text='Rectangle')

# Circle tab
circle_radius_label = tk.Label(circle_tab, text="Enter radius:")
circle_radius_label.pack()

radius_circle = tk.Entry(circle_tab)
radius_circle.pack()

circle_calculate_button = tk.Button(circle_tab, text="Calculate", command=calculate_circle_area)
circle_calculate_button.pack()

circle_result = tk.Label(circle_tab, text="")
circle_result.pack()

# Square tab
square_side_label = tk.Label(square_tab, text="Enter side length:")
square_side_label.pack()

side_square = tk.Entry(square_tab)
side_square.pack()

square_calculate_button = tk.Button(square_tab, text="Calculate", command=calculate_square_area)
square_calculate_button.pack()

square_result = tk.Label(square_tab, text="")
square_result.pack()

# Rectangle tab
rectangle_length_label = tk.Label(rectangle_tab, text="Enter length:")
rectangle_length_label.pack()

length_rect = tk.Entry(rectangle_tab)
length_rect.pack()

rectangle_width_label = tk.Label(rectangle_tab, text="Enter width:")
rectangle_width_label.pack()

width_rect = tk.Entry(rectangle_tab)
width_rect.pack()

rectangle_calculate_button = tk.Button(rectangle_tab, text="Calculate", command=calculate_rectangle_area)
rectangle_calculate_button.pack()

rectangle_area_result = tk.Label(rectangle_tab, text="")
rectangle_area_result.pack()

tab_control.pack(expand=1, fill="both")

root.mainloop()