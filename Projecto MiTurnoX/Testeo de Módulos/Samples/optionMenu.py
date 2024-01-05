import tkinter as tk
from tkinter import ttk

def option_selected(event):
    selected_option = event.widget.get()
    print(f"Selected option: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Dynamic Option Menus")

# Create a list of options for each menu
options_lists = [
    ["Option A", "Option B", "Option C"],
    ["Option 1", "Option 2", "Option 3"],
    ["Option X", "Option Y", "Option Z"]
]

# Create and configure option menus inside a for loop
for i, options in enumerate(options_lists):
    label = tk.Label(root, text=f"Menu {i + 1}:")
    label.grid(row=i, column=0, padx=10, pady=10)

    # Create a StringVar to store the selected option
    selected_option = tk.StringVar()

    # Create the option menu and link it to the StringVar
    option_menu = ttk.Combobox(root, textvariable=selected_option, values=options)
    option_menu.grid(row=i, column=1, padx=10, pady=10)

    # Set a default value for the option menu
    option_menu.set(options[0])

    # Bind the event handler to the <<ComboboxSelected>> event
    option_menu.bind("<<ComboboxSelected>>", option_selected)

# Start the Tkinter event loop
root.mainloop()
