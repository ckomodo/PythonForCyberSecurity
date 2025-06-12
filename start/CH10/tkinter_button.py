# Seconder tkinter script
# Add a button and command
# Create 

# Import tkinter

# Functions

# Create the GUI main window

# Add widgets

# Enter the main event loop

# Various tkinter geometry managers
# View how pack, grid, place work together
# Created by Christopher W 11/15

# Import tkinter
import tkinter
from tkinter import messagebox

def button_clicked():
    tkinter.Label(my_window, text = "button was clicked").pack()
    messagebox.showerror("Error", my_button)



# Create the GUI main window
my_window = tkinter.Tk()

#Add widgets:
my_label = tkinter.Label(my_window, text = "Dad Jokes", font = ("Calabria", 50))
my_label.pack()
my_button = tkinter.Button(my_window, text = "Another Joke", command = button_clicked)
my_button.pack()



# Using pack in a separate frame

# Using grid in another frame

# Using place in the root window


# Enter the main event loop
my_window.mainloop()
