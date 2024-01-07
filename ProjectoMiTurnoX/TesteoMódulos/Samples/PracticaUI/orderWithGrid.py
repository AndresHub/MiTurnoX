import tkinter as tk
from tkinter import StringVar

def on_button_click(button_number):
    print(f"Button {button_number} clicked with text: {button_texts[button_number-1].get()}")

def create_buttons(num_buttons):
    for i in range(num_buttons):
        button = tk.Button(app, text=f"Button {i + 1} - {button_texts[i].get()}", command=lambda i=i: on_button_click(i + 1))
        button.grid(row=i, column=0, padx=5, pady=5)  # Adjust row, column, padx, and pady as needed

app = tk.Tk()
app.title("Dynamic Buttons with User-Defined Text Example")

label_num_buttons = tk.Label(app, text="Select the number of buttons:")
label_num_buttons.grid(row=0, column=0, pady=10)

selected_quantity = StringVar(app)
selected_quantity.set("1")

quantity_options = list(range(1, 11))
quantity_menu = tk.OptionMenu(app, selected_quantity, *quantity_options)
quantity_menu.grid(row=1, column=0, pady=10)

def create_buttons_handler():
    num_buttons = int(selected_quantity.get())

    for i in range(num_buttons):
        label = tk.Label(app, text=f"Enter text for Button {i + 1}:")
        label.grid(row=i + 2, column=0, pady=5)  # Adjust row, column, and pady as needed

        var = StringVar()
        entry = tk.Entry(app, textvariable=var)
        entry.grid(row=i + 2, column=1, padx=5, pady=5)  # Adjust row, column, padx, and pady as needed

        button_texts.append(var)

    def create_buttons_with_text():
        create_buttons(num_buttons)

    create_buttons_button = tk.Button(app, text="Create Buttons", command=create_buttons_with_text)
    create_buttons_button.grid(row=num_buttons + 2, column=0, pady=10)  # Adjust row and column as needed

button_texts = []

create_buttons_button = tk.Button(app, text="Create Buttons", command=create_buttons_handler)
create_buttons_button.grid(row=13, column=0, pady=10)  # Adjust row and column as needed

app.mainloop()
