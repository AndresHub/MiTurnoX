import tkinter as tk

def on_button_click(button_number):
    print(f"Button {button_number} clicked with text: {button_texts[button_number-1]}")

def create_buttons(num_buttons):
    for i in range(num_buttons):
        # Create a button widget and associate it with the corresponding click function
        button = tk.Button(app, text=f"Button {i + 1} - {button_texts[i]}", command=lambda i=i: on_button_click(i + 1))
        button.pack()

app = tk.Tk()
app.title("Dynamic Buttons with User-Defined Text Example")

label_num_buttons = tk.Label(app, text="Enter the number of buttons:")
label_num_buttons.pack()

entry_num_buttons = tk.Entry(app)
entry_num_buttons.pack()

label_button_texts = tk.Label(app, text="Enter button texts (comma-separated):")
label_button_texts.pack()

entry_button_texts = tk.Entry(app)
entry_button_texts.pack()

def create_buttons_handler():
    num_buttons = int(entry_num_buttons.get())
    
    # Get the user input for button texts and split them into a list
    button_texts_input = entry_button_texts.get()
    button_texts.extend(button_texts_input.split(','))

    # Call the function to create buttons based on user input
    create_buttons(num_buttons)

button_texts = []

create_buttons_button = tk.Button(app, text="Create Buttons", command=create_buttons_handler)
create_buttons_button.pack()

app.mainloop()
