import tkinter as tk
from tkinter import StringVar


listado = []
siguiente = [0]
listado_preferencial = []
siguiente_preferencial= [0]

def on_button_click(button_number):
    if len(listado) == 0:
        print("No hay turnos en espera")
    else:
        llamado = listado.pop(0) 
        print(f"Caja {button_number} llamando a ticket {llamado}")

def create_buttons(num_buttons):
    for i in range(num_buttons):
        button = tk.Button(app, text=f"Button {i + 1} - {button_texts[i].get()}", command=lambda i=i: on_button_click(i + 1))
        button.pack(side=tk.LEFT, padx=5, pady=5)  # Adjust side, padx, and pady as needed
        opcion_att = tk.OptionMenu(app, atenciones, *atenciones_dif)
        opcion_att.pack(side=tk.LEFT, padx=5, pady=5)

def ticket():
    if len(listado) == 0:
        listado.append(siguiente[0] + 1)
        nuevo = siguiente.pop()
        siguiente.append(nuevo + 1)
        print(f"{listado}")
        print(f"{siguiente}")
    else:
        ultimo = listado.pop(len(listado) - 1)
        nuevo = ultimo + 1
        listado.append(ultimo)
        listado.append(nuevo)
        print(f"{listado}")
        siguiente.pop()
        siguiente.append(nuevo)
        print(f"{siguiente}")

def ticket_preferencial():
        if len(listado_preferencial) == 0:
            listado_preferencial.append(siguiente_preferencial[0] + 1)
            nuevo_preferencial = siguiente_preferencial.pop()
            siguiente_preferencial.append(nuevo_preferencial + 1)
            print(f"{listado_preferencial}")
            print(f"{siguiente_preferencial}")
        else:
            ultimo_preferencial = listado_preferencial.pop(len(listado_preferencial) - 1)
            nuevo_preferencial = ultimo_preferencial + 1
            listado_preferencial.append(ultimo_preferencial)
            listado_preferencial.append(nuevo_preferencial)
            print(f"{listado_preferencial}")
            siguiente_preferencial.pop()
            siguiente_preferencial.append(nuevo_preferencial)
            print(f"{siguiente_preferencial}")

app = tk.Tk()
app.title("Testing MiTurnoX")
app.geometry('700x500')

label_num_buttons = tk.Label(app, text="Select the number of buttons:")
label_num_buttons.pack()

selected_quantity = StringVar(app)
selected_quantity.set("1")

quantity_options = list(range(1, 11))
quantity_menu = tk.OptionMenu(app, selected_quantity, *quantity_options)
quantity_menu.pack()

atenciones = StringVar(app)
atenciones.set("P o N")

atenciones_dif = ["Preferencial", "Normal"]

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

frame_botones = tk.Frame(app)
frame_botones.pack()

conteo_cliente = tk.Button(frame_botones, text="Generar turno", command=ticket, height=2, width=15)
conteo_cliente.pack(side=tk.LEFT, padx=5, pady=5)

conteo_preferencial = tk.Button(frame_botones, text="Preferencial", command=ticket_preferencial, height=2, width=15)
conteo_preferencial.pack(side=tk.LEFT, padx=5, pady=5)




app.mainloop()
