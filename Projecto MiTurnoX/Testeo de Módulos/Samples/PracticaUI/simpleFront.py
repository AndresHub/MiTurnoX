import tkinter as tk
from tkinter import StringVar

# Create the main application window
app = tk.Tk()
app.title("Simple UI Example")

# Function to handle button click
def on_button_click():
    # Get the text from the entry widget and display it in the console
    user_input = entry.get()
    print("User input:", user_input)

# Create and place a label widget
label = tk.Label(app, text="Enter some text:")
label.pack()

# Create and place an entry widget (text box)
entry = tk.Entry(app)
entry.pack()

# Create a button widget and associate it with the on_button_click function
button = tk.Button(app, text="Click me!", command=on_button_click)
button.pack()

# Create a drop-down list (OptionMenu) with some options
options = ["Option 1", "Option 2", "Option 3"]
selected_option = StringVar(app)
selected_option.set(options[0])  # Set the default selected option
option_menu = tk.OptionMenu(app, selected_option, *options)
option_menu.pack()

# Start the Tkinter event loop
app.mainloop()
