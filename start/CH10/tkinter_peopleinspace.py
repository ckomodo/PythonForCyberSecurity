# third tkinter script
# Get people in space
# Create by 

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
import requests


def get_people_in_space():
    request_uri = "http://api.open-notify.org/astros.json"
    r = requests.get(request_uri)
    items = r.json()
    people_in_space = items["number"]
    tkinter.Label(my_window, text = people_in_space).pack()

# Create the GUI main window
my_window = tkinter.Tk()

#Add widgets:
my_label = tkinter.Label(my_window, text = "People in space", font = ("Calabria", 50))
my_label.pack()
my_button = tkinter.Button(my_window, text = "Click Here to Update", command = get_people_in_space)
my_button.pack()



# Using pack in a separate frame

# Using grid in another frame

# Using place in the root window


# Enter the main event loop
my_window.mainloop()
