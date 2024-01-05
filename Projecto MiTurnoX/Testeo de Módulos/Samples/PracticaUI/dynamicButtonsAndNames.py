import tkinter as tk
from tkinter import StringVar

def on_button_click(button_number):
    print(f"Button {button_number} clicked with text: {button_texts[button_number-1].get()}")

def create_buttons(num_buttons):
    for i in range(num_buttons):
        button = tk.Button(app, text=f"Button {i + 1} - {button_texts[i].get()}", command=lambda i=i: on_button_click(i + 1))
        button.pack()

app = tk.Tk()
app.title("Dynamic Buttons with User-Defined Text Example")

label_num_buttons = tk.Label(app, text="Select the number of buttons:")
label_num_buttons.pack()

# Use a StringVar to store the selected quantity
selected_quantity = StringVar(app)
selected_quantity.set("1")  # Set the default selected quantity

# Create an OptionMenu with values from 1 to 10
quantity_options = list(range(1, 11))
quantity_menu = tk.OptionMenu(app, selected_quantity, *quantity_options)
quantity_menu.pack()

def create_buttons_handler():
    num_buttons = int(selected_quantity.get())

    for i in range(num_buttons):
        label = tk.Label(app, text=f"Enter text for Button {i + 1}:")
        label.pack()

        var = StringVar()
        entry = tk.Entry(app, textvariable=var)
        entry.pack()

        button_texts.append(var)

    def create_buttons_with_text():
        create_buttons(num_buttons)

    create_buttons_button = tk.Button(app, text="Create Buttons", command=create_buttons_with_text)
    create_buttons_button.pack()

button_texts = []

create_buttons_button = tk.Button(app, text="Create Buttons", command=create_buttons_handler)
create_buttons_button.pack()

app.mainloop()

