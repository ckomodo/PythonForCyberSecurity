# Various tkinter geometry managers
# View how pack, grid, place work together
# Created by Christopher W 11/15

# Import tkinter
import tkinter

# Create the GUI main window
my_window = tkinter.Tk()

#Add widgets:
my_label = tkinter.Label(my_window, text = "Hello world", font = ("Calabria", 50))
my_label.pack()



# Using pack in a separate frame

# Using grid in another frame

# Using place in the root window


# Enter the main event loop
my_window.mainloop()
