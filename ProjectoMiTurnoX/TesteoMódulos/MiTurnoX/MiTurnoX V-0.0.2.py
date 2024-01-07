import customtkinter as ctk
import tkinter as tk
from tkinter import StringVar


def print_letra(letra):
    print(f"{letra}")

#muestra/esconde los frames relacionados a los botones del menú principal.
    #pack(fill = "both", pady = 10, expand = 1)
def mostrar(evento):
    if evento == "1":
        frame_configuracion.grid(
            column = 0,
            row = 1,
            padx = 10,
            pady = 10
        )
        frame_atenciones.grid_remove()
        frame_video.grid_remove()
    elif evento == "2":
        frame_configuracion.grid_remove()
        frame_atenciones.grid(
            column = 0,
            row = 1,
            padx = 10,
            pady = 10
        )
        frame_video.grid_remove()
    else:
        frame_configuracion.grid_remove()
        frame_atenciones.grid_remove()
        frame_video.grid(
            column = 0,
            row = 1,
            padx = 10,
            pady = 10
        )


#maneja el estado del checkbox preferencial, indica "on" u "off", y modifica las opciones de cantidad de atenciones
##si está "on", debe haber al menos 2 servicios para que uno sea preferencial, por lo tanto elimina el 1 como opción de cantidad
### OJO! este checkbox también debería ser tomado en cuenta al momento de crear atenciones
def activacion_preferencial():
    boton_submenu_config_preferencial.configure(text = estado_preferencial.get())
    if boton_submenu_config_preferencial.get() == "on":
        dropmenu_config_num_atenciones.set("2")
        dropmenu_config_num_atenciones.configure(values= ["2", "3", "4", "5", "6", "7", "8", "9", "10"])
    else:
        dropmenu_config_num_atenciones.set("1")
        dropmenu_config_num_atenciones.configure(values= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])


#muestra/esconde los frames relacionados a las opciones del submenú de configuración
def mostrar_frame_submenu_config(evento):
    if evento == "1":
        frame_submenu_configuracion_atenciones.grid(
        column = 0,
        row = 3
        )
        frame_submenu_configuracion_servidor.grid_remove()
        frame_submenu_configuracion_video.grid_remove()
    elif evento == "2":
        frame_submenu_configuracion_servidor.grid(
        column = 0,
        row = 3
        )
        frame_submenu_configuracion_atenciones.grid_remove()
        frame_submenu_configuracion_video.grid_remove()
    else:
        frame_submenu_configuracion_video.grid(
        column = 0,
        row = 3
        )
        frame_submenu_configuracion_servidor.grid_remove()
        frame_submenu_configuracion_atenciones.grid_remove()

#obtiene un número del menú de opciones de cantidad de atenciones deseadas
#crea la cantidad de labels y entrys necesarios para definir el nombre y letra de cada botón de atención a ser creados
#alimenta 2 listas, una con nombres de los botones, y otra con la letra asignada al servicio
#con la información capturada en las listas, debería crear los botones en el frame de atenciones
# OJO! tomar en cuenta si la opción de preferencial está activada para evitar errores
def definir_atenciones(num):
    for i in range(num):
        label_nombre = ctk.CTkLabel(
            frame_submenu_configuracion_atenciones,
            text= f"Atención # {i + 1}"
            )
        label_nombre.grid(
            column = 0,
            row = i + 3,
            padx = 10,
            pady = 5
            )
        texto_atencion = StringVar()
        entry_texto = ctk.CTkEntry(
            frame_submenu_configuracion_atenciones,
            textvariable= texto_atencion,
            width= 300
            )
        entry_texto.grid(
            column = 1,
            row = i + 3,
            padx = 10,
            pady = 5
        )
        texto_botones.append(texto_atencion)
        label_letra = ctk.CTkLabel(
            frame_submenu_configuracion_atenciones,
            text= "Letra"
            )
        label_letra.grid(
            column = 2,
            row = i + 3,
            padx = 10,
            pady = 5
            )
        texto_letra = StringVar()
        entry_letra = ctk.CTkEntry(
            frame_submenu_configuracion_atenciones,
            textvariable= texto_letra,
            width= 50
        )
        entry_letra.grid(
            column = 3,
            row = i + 3,
            padx = 10,
            pady = 5
        )
        letra_atenciones.append(texto_letra)
        print(letra_atenciones[i].get())
    
    def crear_atenciones():
        letra_var = letra_atenciones
        print(letra_var)
        for i in range(0, num):
            boton_atencion_definida = ctk.CTkButton(
                frame_atenciones,
                text= (f"{texto_botones[i].get()}"),
                command= lambda: print_funcion(f"{letra_var[i]}")
            )

            boton_atencion_definida.grid(
                column= 0,
                row = i,
                padx = 10,
                pady = 10
            )


    def print_funcion(letra):
        print(letra)

    boton_confirmar_entrys = ctk.CTkButton(
        frame_submenu_configuracion_atenciones,
        text= "Crear Botones",
        command= crear_atenciones
        )
    boton_confirmar_entrys.grid(
        column = 3,
        row = 13,
        padx = 10,
        pady = 5
    )

texto_botones = []
letra_atenciones = []


app = ctk.CTk()
ctk.set_appearance_mode("dark")
app.title("Mi Turno X v0.0.2")
app.after(
    0, 
    lambda: app.wm_state('zoomed')
    )

estado_preferencial = tk.StringVar(value="off")

menu_principal = ctk.CTkFrame(
    app,
    height= 50
    )
menu_principal.grid(
    column = 0,
    row = 0
    )

boton_configuracion = ctk.CTkButton(
    menu_principal, text="Configuración",
    command= lambda: mostrar("1"),
    font=("verdana", 15)
    )
boton_configuracion.grid(
    column = 0,
    row = 0,
    padx = 10,
    pady = 10
    )

boton_atenciones = ctk.CTkButton(
    menu_principal, text="Atenciones",
    command= lambda: mostrar("2"),
    font=("verdana", 15)
    )
boton_atenciones.grid(
    column = 2,
    row = 0,
    padx = 10,
    pady = 10
    )

boton_video = ctk.CTkButton(
    menu_principal, text="Video",
    command= lambda: mostrar("3"),
    font=("verdana", 15)
    )
boton_video.grid(
    column = 3,
    row = 0,
    padx = 10,
    pady = 10
    )

frame_configuracion = ctk.CTkFrame(app)
frame_atenciones = ctk.CTkFrame(app)
frame_video = ctk.CTkFrame(app)

label_configuracion = ctk.CTkLabel(
    frame_configuracion,
    text="Configuración",
    font=("verdana", 18)
    )
label_configuracion.grid(
    column = 0,
    row = 1
    )
label_atenciones = ctk.CTkLabel(
    frame_atenciones,
    text="Atenciones",
    font=("verdana", 18)
    )
label_atenciones.grid(
    column = 0,
    row = 1
    )
label_video = ctk.CTkLabel(
    frame_video,
    text="Video",
    font=("verdana", 18)
    )
label_video.grid(
    column = 0,
    row = 1
    )

frame_submenu_configuracion = ctk.CTkFrame(frame_configuracion)
frame_submenu_configuracion.grid(
    column = 0,
    row = 2
    )

boton_submenu_config_atenciones = ctk.CTkButton(
    frame_submenu_configuracion,
    text= "Configurar Atenciones",
    command = lambda: mostrar_frame_submenu_config("1")
    )
boton_submenu_config_atenciones.grid(
    column = 0,
    row = 0,
    padx = 10,
    pady = 10
    )
boton_submenu_config_server = ctk.CTkButton(
    frame_submenu_configuracion,
    text= "Configurar Server",
    command = lambda: mostrar_frame_submenu_config("2")
    )
boton_submenu_config_server.grid(
    column = 1,
    row = 0,
    padx = 10,
    pady = 10
    )
boton_submenu_config_video = ctk.CTkButton(
    frame_submenu_configuracion,
    text= "Configurar Video",
    command = lambda: mostrar_frame_submenu_config("3")
    )
boton_submenu_config_video.grid(
    column = 2,
    row = 0,
    padx = 10,
    pady = 10
    )

frame_submenu_configuracion_atenciones = ctk.CTkFrame(frame_configuracion)
frame_submenu_configuracion_servidor = ctk.CTkFrame(frame_configuracion)
frame_submenu_configuracion_video = ctk.CTkFrame(frame_configuracion)

label_submenu_config_preferencial = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text= "Preferencial", anchor= "w",
    width= 150
    )
label_submenu_config_preferencial.grid(
    column = 0,
    row = 0,
    padx = 10,
    pady = 10
    )
label_submenu_config_num_atenciones = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text= "Cantidad de Atenciones",
    anchor="w",
    width= 150
    )
label_submenu_config_num_atenciones.grid(
    column = 0,
    row = 1,
    padx = 10,
    pady = 10
    )

boton_submenu_config_preferencial = ctk.CTkCheckBox(
    frame_submenu_configuracion_atenciones,
    text="off", variable= estado_preferencial,
    onvalue= "on",
    offvalue= "off",
    command= activacion_preferencial
    )
boton_submenu_config_preferencial.grid(
    column = 1,
    row = 0,
    padx = 10
    )


dropmenu_config_num_atenciones = ctk.CTkOptionMenu(
    frame_submenu_configuracion_atenciones,
    values= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
dropmenu_config_num_atenciones.grid(
    column = 1,
    row = 1,
    padx = 10
    )
dropmenu_config_num_atenciones.set("1")

boton_definir_num_atenciones = ctk.CTkButton(
    frame_submenu_configuracion_atenciones,
    text= "Definir Atenciones",
    command= lambda: definir_atenciones(int(dropmenu_config_num_atenciones.get()))
    )
boton_definir_num_atenciones.grid(
    column = 2,
    row = 1,
    padx = 10
    )













app.mainloop()

