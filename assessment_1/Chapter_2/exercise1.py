import tkinter 

# this is the program that will allow the font to switch once called to the button section
def font_switch():
    label.config(font=("Arial", 20, "bold"))

sam = tkinter.Tk() # sam is just a variable that i randomly thought about hehe :)
sam.geometry("300x200") # putting a fixed window size for this GUI
sam.resizable(False, False) # to disable resizing of the window
sam.config(background="pink") # just the background color

# The welcome message to be displayed on the GUI
label = tkinter.Label(sam, text="Welcome!!", font=("Monaco", 30, "bold")) 
label.pack(pady=20) # so the message could be at the center of the screen

# the button to change the font's style
font_button = tkinter.Button(sam, text="Click me to change font!!", command=font_switch)
font_button.pack() # leaving it as it is so it could be kept in the same location as the welcome message

sam.mainloop()

