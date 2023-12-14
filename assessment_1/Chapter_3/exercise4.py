import tkinter as tk

def get_coordinates():
    x = int(entry_x.get())
    y = int(entry_y.get())
    z = int(entry_z.get())

    if x < 0 or x > 90:
        print("Error: x coordinate must be between 0 and 90")
        return
    if y < 0 or y > 90:
        print("Error: y coordinate must be between 0 and 90")
        return
    if z < 0 or z > 90:
        print("Error: z coordinate must be between 0 and 90")
        return

    # Continue with the rest of your program
    print("Coordinates:", x, y, z)

root = tk.Tk()

entry_x = tk.Entry(root)
entry_x.grid(row=0, column=0)

entry_y = tk.Entry(root)
entry_y.grid(row=0, column=1)

entry_z = tk.Entry(root)
entry_z.grid(row=0, column=2)

button = tk.Button(root, text="Submit", command=get_coordinates)
button.grid(row=1, columnspan=3)

root.mainloop()