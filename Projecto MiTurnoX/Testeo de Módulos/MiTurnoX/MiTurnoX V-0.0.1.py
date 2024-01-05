import tkinter as tk
from tkinter import StringVar

#definición de métodos para botones de menú
#función para esconder el menú principal y cambiar la acción del botón a mostrar el menú
def esconder_menu_inicial():
    ventana_inicio.pack_forget()
    boton_inicio.configure(command=mostrar_menu_inicial)


#función para mostrar el menú principal, y cambiar la acción del botón a esconder el menú
def mostrar_menu_inicial():
    ventana_inicio.pack(fill="both", expand=1)
    boton_inicio.configure(command=esconder_menu_inicial)


def config_botones_servicios():
    cantidad_botones = selec_cantidad.get()
    if cantidad_botones == "1":
        edicion_servicios = tk.Frame(ventana_inicio, bg="black", borderwidth=1, border=1)
        edicion_servicios.grid(column=0, row=1, padx=5, pady=5, sticky="snew")
        primer_servicio = tk.Label(edicion_servicios, height=1, width=20, bg="black", fg="white", text="Definir Primer Servicio")
        primer_servicio.grid(column=0, row=0, padx=5, pady=5)
        entry_primer_servicio = tk.Entry(edicion_servicios, width=20)
        entry_primer_servicio.insert(0, "Servicio")
        entry_primer_servicio.grid(column=2, row=0, padx=5, pady=5)
        entry_primer_servicio.bind("<1>", lambda x: borrar_texto(entry_primer_servicio.get()))
        entry_primer_servicio_letra = tk.Entry(edicion_servicios, width=20,)
        entry_primer_servicio_letra.insert(0, "Letra")
        entry_primer_servicio_letra.grid(column=3, row=0, padx=5, pady=5)
        entry_primer_servicio_letra.bind("<1>", lambda x: borrar_texto(entry_primer_servicio_letra.get()))
    elif cantidad_botones == "2":
        edicion_servicios = tk.Frame(ventana_inicio, bg="white", borderwidth=1, border=1)
        edicion_servicios.grid(column=0, row=1, padx=5, pady=5, sticky="snew")
        primer_servicio = tk.Label(edicion_servicios, height=1, width=20, bg="black", fg="white", text="Definir Primer Servicio")
        primer_servicio.grid(column=0, row=0, padx=5, pady=5)
        entry_primer_servicio = tk.Entry(edicion_servicios, width=20)
        entry_primer_servicio.insert(0, "Servicio")
        entry_primer_servicio.grid(column=2, row=0, padx=5, pady=5)
        entry_primer_servicio.bind("<1>", lambda x: borrar_texto(entry_primer_servicio.get()))
        entry_primer_servicio_letra = tk.Entry(edicion_servicios, width=20,)
        entry_primer_servicio_letra.insert(0, "Letra")
        entry_primer_servicio_letra.grid(column=3, row=0, padx=5, pady=5)
        entry_primer_servicio_letra.bind("<1>", lambda x: borrar_texto(entry_primer_servicio_letra.get()))

    
    def borrar_texto(event):
        if event == "Servicio":
            entry_primer_servicio.delete(0, 8)
        elif event == "Letra":
            entry_primer_servicio_letra.delete(0, 5)



#creo mi ventana principal con el nombre app
app = tk.Tk()
#agrego título a la ventana
app.title("Mi Turno X versión 0.0.1")
app.configure(bg="black")
#Hago que la ventana inicie en modo maximizado
app.state('zoomed')
#atrapo el alto y ancho de la pantalla
width= app.winfo_screenwidth() 
height= app.winfo_screenheight()
#aplico los valores atrapados al método geometry del app
app.geometry("%dx%d" % (width, height))
#creo un frame para almacenar mis botones de menú
barra_menu = tk.Frame(app, bg="blue", height=30)
#lo empaco en el app llenando el ancho completo
barra_menu.pack(side="top", fill="x")
#creo los botones de mi menú y los empaqueto hacia la izq
boton_inicio = tk.Button(barra_menu, text="Inicio", bg="black", fg="white", height=1, width=10, padx=5, pady=5, command=esconder_menu_inicial)
boton_inicio.pack(side="left")

#creo frame para los elementos del menú principal
ventana_inicio = tk.Frame(app, bg="black")
#empaqueto el frame llenando los 2 axis, y asigno un expand de más de 0 para que llene X, si dejo sin expand, solo llena Y
ventana_inicio.pack(fill="both", expand=1)

#creación de elementos del menú Inicio
#selección de cantidad de servicios
cantidad_servicios_label = tk.Label(ventana_inicio, text="Cantidad de Servicios deseados", foreground="white", bg="black", relief="solid")
#empaqueto la etiqueta con grid para mantener un orden
cantidad_servicios_label.grid(column=0,row=0, padx=5, pady=5)
#opciones de cantidad con option menu
#creo variable stringvar en app y la seteo en 1
selec_cantidad = StringVar(app)
selec_cantidad.set("1")
#creo variable para almacenar lista con números del 1 al 10 (range inicia en 1 y termina antes del 11)
opc_cantidad = list(range(1, 11))
#creo el objeto option menu en la ventana de inicio, seteo la variable inicial, y le paso la lista de elementos
menu_opc_cantidad = tk.OptionMenu(ventana_inicio, selec_cantidad, *opc_cantidad)
#uso el método configure para acceder y cambiar el estilo del menú
menu_opc_cantidad.configure(bg="black", foreground="white", height=1, width=10, activebackground="blue", activeforeground="white", direction="right", padx=5, pady=5)
#ingreso a configure del atributo menú del objeto optionmenu ara editar el estilo del drop down
menu_opc_cantidad["menu"].configure(bg="black", fg="white")
#empaqueto el objeto a la ventana de menú respetando el orden de mis elementos con grid
menu_opc_cantidad.grid(column=1,row=0, padx=5, pady=5)
#boton de confirmación de cantidad de servicios deseados
boton_crear_atenciones = tk.Button(ventana_inicio, text="Crear Servicios", bg="black", fg="white", height=1, width=10, padx=5, pady=5, command=config_botones_servicios)
boton_crear_atenciones.grid(column=2,row=0, padx=5, pady=5)
#frame para edición de los servicios


#temporalmente creo un frame dentro de la app principal para desplegar los botones y poder probar funciones



app.mainloop()