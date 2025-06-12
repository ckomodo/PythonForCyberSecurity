# third tkinter script
# Get people in space
# Create by 

# Import tkinter

# Functions

# Create the GUI main window

# Create font object
# Set wraplength to 25 characters

# Add widgets

# Enter the main event loop

# Import tkinter
import tkinter
import requests


def get_dad_joke():
    request_uri = "https://icanhazdadjoke.com/"
    headers = { "Accept" : "application/json" }
    r = requests.get(request_uri, headers = headers)
    items = r.json()
    print(items)
    joke = items["joke"]
    #tkinter.Label(my_window, text = joke).pack()
    my_label.configure(text = joke)

# Create the GUI main window
my_window = tkinter.Tk()

#Add widgets:
my_label = tkinter.Label(my_window, text = "Get Dad Joke", font = ("Calabria", 50))
my_label.pack()
my_button = tkinter.Button(my_window, text = "New Joke", command = get_dad_joke)
my_button.pack()

my_window.mainloop()