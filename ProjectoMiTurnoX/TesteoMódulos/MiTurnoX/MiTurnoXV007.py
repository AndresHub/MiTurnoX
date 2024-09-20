import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from config import config
from collections import deque
import psycopg2
import socket
import threading

        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ####----SETEO BASE DE VENTANA PRINCIPAL----####
        #self.minsize(700, 560)
        self.title("Mi Turno X - V 0.0.6")
        ctk.set_appearance_mode("dark")
        #self.after(0, lambda: self.wm_state('zoomed'))
        self.resizable(False, False)
        self.win_height = 700
        self.win_width = 600
        self.desk_height = self.winfo_screenheight()
        self.desk_width = self.winfo_screenwidth()
        self.x_axis = int((self.desk_width/2) - (self.win_width/2))
        self.y_axis = int((self.desk_height/2) - (self.win_height/2))
        self.geometry("{}x{}+{}+{}".format(self.win_width, self.win_height, self.x_axis, self.y_axis))
        ####----VARIABLES VARIAS----####
        self.estado_preferencial = ctk.Variable(value="Off")
        ####----ESTADOS DE WIDGETS PARA ACTIVAR O DESACTIVAR LOS MISMOS----####
        self.status_config = False
        self.status_atenciones = False
        self.status_video = False
        self.status_config_atenciones = False
        ####----CREACIÓN DE MENÚ PRINCIPAL----####
        self.menu_principal = MenuPrincipal(self)
        ####----WIDGETS----####
        self.ventana_atenciones = VentanaAtenciones(self)
        self.ventana_config = VentanaConfig(self)
        self.ventana_video = VentanaVideo(self)
        self.ventana_config_atenciones = VentanaConfigAtenciones(self)
        self.frame_nombrar_atenciones = FrameAtenciones(self.ventana_config_atenciones.frame_config_atenciones, self)
        self.frame_atenciones_individuales = FrameAtencionesIndividuales(self.frame_nombrar_atenciones.frame_creacion_atenciones, self)
        

        

    ####----MOSTRAR/ESCONDER VENTANA DE CONFIGURACIÓN----####
    def mostrar_menu_config(self, origen):
        if origen == "menu":
            if self.status_atenciones == True:
                self.ventana_atenciones.frame_atenciones.pack_forget()
                self.status_atenciones = False
                self.menu_principal.boton_atenciones.configure(command = lambda: self.mostrar_atenciones("menu"))

            if self.status_video == True:
                self.ventana_video.frame_video.pack_forget()
                self.status_video = False
                self.menu_principal.boton_video.configure(command = lambda: self.mostrar_video("menu"))
            
            if self.status_config == False:
                self.ventana_config.frame_botones_config.pack(fill = "x", padx = 5)
                self.menu_principal.boton_configuracion.configure(command = lambda: self.esconder_menu_config("menu"))
                self.status_config = True
        
    def esconder_menu_config(self, origen):
        if origen == "menu":
            if self.status_config_atenciones == True:
                self.ventana_config_atenciones.frame_config_atenciones.pack_forget()
                self.frame_nombrar_atenciones.frame_creacion_atenciones.pack_forget()
                self.status_config_atenciones = False
            self.ventana_config.frame_botones_config.pack_forget()
            self.menu_principal.boton_configuracion.configure(command = lambda: self.mostrar_menu_config("menu"))
            self.ventana_config.boton_config_atenciones.configure(command= lambda: self.mostrar_config_atenciones("menu"))
            self.status_config = False
    
    ####----MOSTRAR/ESCONDER VENTANA DE ATENCIONES----####
    def mostrar_atenciones(self, origen):
        if origen == "menu":
            if self.status_config_atenciones == True:
                self.ventana_config_atenciones.frame_config_atenciones.pack_forget()
                self.frame_nombrar_atenciones.frame_creacion_atenciones.pack_forget()
                self.status_config_atenciones = False
            
            if self.status_config_atenciones == True:
                self.ventana_config_atenciones.frame_config_atenciones.pack_forget()
                self.status_config_atenciones = False

            if self.status_config == True:
                self.ventana_config.frame_botones_config.pack_forget()
                self.status_config = False
                self.menu_principal.boton_configuracion.configure(command = lambda: self.mostrar_menu_config("menu"))

            if self.status_video == True:
                self.ventana_video.frame_video.pack_forget()
                self.status_video = False
                self.menu_principal.boton_video.configure(command = lambda: self.mostrar_video("menu"))
            
            if self.status_atenciones == False:
                self.ventana_atenciones.frame_atenciones.pack(fill = "x", padx = 5)
                self.menu_principal.boton_atenciones.configure(command = lambda: self.esconder_atenciones("menu"))
                self.status_atenciones = True
        self.ventana_config.boton_config_atenciones.configure(command= lambda: self.mostrar_config_atenciones("menu"))

    def esconder_atenciones(self, origen):
        if origen == "menu":
            self.ventana_atenciones.frame_atenciones.pack_forget()
            self.menu_principal.boton_atenciones.configure(command = lambda: self.mostrar_atenciones("menu"))
            self.status_atenciones = False

    ####----MOSTRAR/ESCONDER VENTANA DE VIDEO----####
    def mostrar_video(self, origen):
        if origen== "menu":
            if self.status_config_atenciones == True:
                self.ventana_config_atenciones.frame_config_atenciones.pack_forget()
                self.frame_nombrar_atenciones.frame_creacion_atenciones.pack_forget()
                self.status_config_atenciones = False
                #self.desactivar_preferencial()
            if self.status_config_atenciones == True:
                self.ventana_config_atenciones.frame_config_atenciones.pack_forget()
                self.status_config_atenciones = False
                #self.desactivar_preferencial()
            if self.status_config == True:
                self.ventana_config.frame_botones_config.pack_forget()
                self.status_config = False
                self.menu_principal.boton_configuracion.configure(command = lambda: self.mostrar_menu_config("menu"))

            if self.status_atenciones == True:
                self.ventana_atenciones.frame_atenciones.pack_forget()
                self.status_atenciones = False
                self.menu_principal.boton_atenciones.configure(command = lambda: self.mostrar_atenciones("menu"))
            
            if self.status_video == False:
                self.ventana_video.frame_video.pack(fill = "x", padx = 5)
                self.menu_principal.boton_video.configure(command = lambda: self.esconder_video("menu"))
                self.status_video = True
        self.ventana_config.boton_config_atenciones.configure(command= lambda: self.mostrar_config_atenciones("menu"))

    def esconder_video(self, origen):
        if origen == "menu":
            self.ventana_video.frame_video.pack_forget()
            self.menu_principal.boton_video.configure(command = lambda: self.mostrar_video("menu"))
            self.status_video = False

    ####----MOSTRAR/ESCONDER FRAME DE CONFIGURACIÓN DE ATENCIONES----####
    def mostrar_config_atenciones(self, origen):
        if origen == "menu":
            self.ventana_config_atenciones.frame_config_atenciones.pack(fill = "x", padx = 5)
            self.frame_nombrar_atenciones.frame_creacion_atenciones.pack(fill = "both", padx = 5, expand= 1)
            self.status_config_atenciones = True
            self.ventana_config.boton_config_atenciones.configure(command = self.nulo)

    ####----ACTIVAR/DESACTIVAR OPCIÓN DE ATENCIÓN PREFERENCIAL----####
    def activar_preferencial(self):
        self.ventana_config_atenciones.toggle_preferencial.configure(text = "On", command = self.desactivar_preferencial)
        self.frame_atenciones_individuales.entry_nombre_atencion_1.insert(0,"PREFERENCIAL")
        self.frame_atenciones_individuales.entry_letra_atencion_1.insert(0,"P")
        self.ventana_config_atenciones.dropmenu_cant_atenciones.configure(values= ("2", "3", "4", "5", "6", "7", "8", "9", "10"))
        self.ventana_config_atenciones.dropmenu_cant_atenciones.set("2")
    
    def desactivar_preferencial(self):
        self.ventana_config_atenciones.toggle_preferencial.configure(text = "Off", command = self.activar_preferencial)
        self.estado_preferencial = ctk.Variable(value= "Off")
        self.frame_atenciones_individuales.entry_nombre_atencion_1.delete(0, len(self.frame_atenciones_individuales.entry_nombre_atencion_1.get()))
        self.frame_atenciones_individuales.entry_letra_atencion_1.delete(0)
        self.ventana_config_atenciones.dropmenu_cant_atenciones.configure(values= ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
        self.ventana_config_atenciones.dropmenu_cant_atenciones.set("1")

    def reset_config(self):
        self.desactivar_preferencial()
        self.ventana_config_atenciones.frame_config_atenciones.pack_forget()
        self.frame_nombrar_atenciones.frame_creacion_atenciones.pack_forget()
        self.status_config_atenciones = False
        self.ventana_config.frame_botones_config.pack_forget()
        self.menu_principal.boton_configuracion.configure(command = lambda: self.mostrar_menu_config("menu"))
        self.ventana_config.boton_config_atenciones.configure(command= lambda: self.mostrar_config_atenciones("menu"))
        self.status_config = False
        self.ventana_config_atenciones = VentanaConfigAtenciones(self)
        self.frame_nombrar_atenciones = FrameAtenciones(self.ventana_config_atenciones.frame_config_atenciones, self)
        self.frame_atenciones_individuales = FrameAtencionesIndividuales(self.frame_nombrar_atenciones.frame_creacion_atenciones, self)
        

    ####----CONFIRMAR ATENCIONES----####
    def crear_pantalla_atenciones(self, num):
        self.num = num
        self.listado_nombres = []
        self.listado_letras = []
        match num:
            case "1":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                if len(self.atencion_1_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "2":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "3":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "4":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                self.atencion_4_letra = self.frame_atenciones_individuales.entry_letra_atencion_4.get().upper()
                self.atencion_4_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_4.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1 or len(self.atencion_4_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1 or len(self.atencion_4_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1 or len(self.atencion_4_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.listado_nombres.append(self.atencion_4_nombre)
                self.listado_letras.append(self.atencion_4_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_4.configure(text = self.atencion_4_nombre, command = lambda: self.llamar_turno(4, self.atencion_4_letra))
                self.ventana_atenciones.boton_atencion_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "5":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                self.atencion_4_letra = self.frame_atenciones_individuales.entry_letra_atencion_4.get().upper()
                self.atencion_4_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_4.get().upper()
                self.atencion_5_letra = self.frame_atenciones_individuales.entry_letra_atencion_5.get().upper()
                self.atencion_5_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_5.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1 or len(self.atencion_4_letra) > 1 or len(self.atencion_5_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1 or len(self.atencion_4_letra) < 1 or len(self.atencion_5_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1 or len(self.atencion_4_nombre) < 1 or len(self.atencion_5_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.listado_nombres.append(self.atencion_4_nombre)
                self.listado_letras.append(self.atencion_4_letra)
                self.listado_nombres.append(self.atencion_5_nombre)
                self.listado_letras.append(self.atencion_5_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_4.configure(text = self.atencion_4_nombre, command = lambda: self.llamar_turno(4, self.atencion_4_letra))
                self.ventana_atenciones.boton_atencion_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_5.configure(text = self.atencion_5_nombre, command = lambda: self.llamar_turno(5, self.atencion_5_letra))
                self.ventana_atenciones.boton_atencion_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "6":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                self.atencion_4_letra = self.frame_atenciones_individuales.entry_letra_atencion_4.get().upper()
                self.atencion_4_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_4.get().upper()
                self.atencion_5_letra = self.frame_atenciones_individuales.entry_letra_atencion_5.get().upper()
                self.atencion_5_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_5.get().upper()
                self.atencion_6_letra = self.frame_atenciones_individuales.entry_letra_atencion_6.get().upper()
                self.atencion_6_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_6.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1 or len(self.atencion_4_letra) > 1 or len(self.atencion_5_letra) > 1 or len(self.atencion_6_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1 or len(self.atencion_4_letra) < 1 or len(self.atencion_5_letra) < 1 or len(self.atencion_6_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1 or len(self.atencion_4_nombre) < 1 or len(self.atencion_5_nombre) < 1 or len(self.atencion_6_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.listado_nombres.append(self.atencion_4_nombre)
                self.listado_letras.append(self.atencion_4_letra)
                self.listado_nombres.append(self.atencion_5_nombre)
                self.listado_letras.append(self.atencion_5_letra)
                self.listado_nombres.append(self.atencion_6_nombre)
                self.listado_letras.append(self.atencion_6_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_4.configure(text = self.atencion_4_nombre, command = lambda: self.llamar_turno(4, self.atencion_4_letra))
                self.ventana_atenciones.boton_atencion_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_5.configure(text = self.atencion_5_nombre, command = lambda: self.llamar_turno(5, self.atencion_5_letra))
                self.ventana_atenciones.boton_atencion_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_6.configure(text = self.atencion_6_nombre, command = lambda: self.llamar_turno(6, self.atencion_6_letra))
                self.ventana_atenciones.boton_atencion_6.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "7":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                self.atencion_4_letra = self.frame_atenciones_individuales.entry_letra_atencion_4.get().upper()
                self.atencion_4_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_4.get().upper()
                self.atencion_5_letra = self.frame_atenciones_individuales.entry_letra_atencion_5.get().upper()
                self.atencion_5_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_5.get().upper()
                self.atencion_6_letra = self.frame_atenciones_individuales.entry_letra_atencion_6.get().upper()
                self.atencion_6_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_6.get().upper()
                self.atencion_7_letra = self.frame_atenciones_individuales.entry_letra_atencion_7.get().upper()
                self.atencion_7_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_7.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1 or len(self.atencion_4_letra) > 1 or len(self.atencion_5_letra) > 1 or len(self.atencion_6_letra) > 1 or len(self.atencion_7_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1 or len(self.atencion_4_letra) < 1 or len(self.atencion_5_letra) < 1 or len(self.atencion_6_letra) < 1 or len(self.atencion_7_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1 or len(self.atencion_4_nombre) < 1 or len(self.atencion_5_nombre) < 1 or len(self.atencion_6_nombre) < 1 or len(self.atencion_7_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.listado_nombres.append(self.atencion_4_nombre)
                self.listado_letras.append(self.atencion_4_letra)
                self.listado_nombres.append(self.atencion_5_nombre)
                self.listado_letras.append(self.atencion_5_letra)
                self.listado_nombres.append(self.atencion_6_nombre)
                self.listado_letras.append(self.atencion_6_letra)
                self.listado_nombres.append(self.atencion_7_nombre)
                self.listado_letras.append(self.atencion_7_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_4.configure(text = self.atencion_4_nombre, command = lambda: self.llamar_turno(4, self.atencion_4_letra))
                self.ventana_atenciones.boton_atencion_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_5.configure(text = self.atencion_5_nombre, command = lambda: self.llamar_turno(5, self.atencion_5_letra))
                self.ventana_atenciones.boton_atencion_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_6.configure(text = self.atencion_6_nombre, command = lambda: self.llamar_turno(6, self.atencion_6_letra))
                self.ventana_atenciones.boton_atencion_6.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_7.configure(text = self.atencion_7_nombre, command = lambda: self.llamar_turno(7, self.atencion_7_letra))
                self.ventana_atenciones.boton_atencion_7.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "8":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                self.atencion_4_letra = self.frame_atenciones_individuales.entry_letra_atencion_4.get().upper()
                self.atencion_4_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_4.get().upper()
                self.atencion_5_letra = self.frame_atenciones_individuales.entry_letra_atencion_5.get().upper()
                self.atencion_5_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_5.get().upper()
                self.atencion_6_letra = self.frame_atenciones_individuales.entry_letra_atencion_6.get().upper()
                self.atencion_6_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_6.get().upper()
                self.atencion_7_letra = self.frame_atenciones_individuales.entry_letra_atencion_7.get().upper()
                self.atencion_7_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_7.get().upper()
                self.atencion_8_letra = self.frame_atenciones_individuales.entry_letra_atencion_8.get().upper()
                self.atencion_8_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_8.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1 or len(self.atencion_4_letra) > 1 or len(self.atencion_5_letra) > 1 or len(self.atencion_6_letra) > 1 or len(self.atencion_7_letra) > 1 or len(self.atencion_8_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1 or len(self.atencion_4_letra) < 1 or len(self.atencion_5_letra) < 1 or len(self.atencion_6_letra) < 1 or len(self.atencion_7_letra) < 1 or len(self.atencion_8_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1 or len(self.atencion_4_nombre) < 1 or len(self.atencion_5_nombre) < 1 or len(self.atencion_6_nombre) < 1 or len(self.atencion_7_nombre) < 1 or len(self.atencion_8_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.listado_nombres.append(self.atencion_4_nombre)
                self.listado_letras.append(self.atencion_4_letra)
                self.listado_nombres.append(self.atencion_5_nombre)
                self.listado_letras.append(self.atencion_5_letra)
                self.listado_nombres.append(self.atencion_6_nombre)
                self.listado_letras.append(self.atencion_6_letra)
                self.listado_nombres.append(self.atencion_7_nombre)
                self.listado_letras.append(self.atencion_7_letra)
                self.listado_nombres.append(self.atencion_8_nombre)
                self.listado_letras.append(self.atencion_8_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_4.configure(text = self.atencion_4_nombre, command = lambda: self.llamar_turno(4, self.atencion_4_letra))
                self.ventana_atenciones.boton_atencion_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_5.configure(text = self.atencion_5_nombre, command = lambda: self.llamar_turno(5, self.atencion_5_letra))
                self.ventana_atenciones.boton_atencion_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_6.configure(text = self.atencion_6_nombre, command = lambda: self.llamar_turno(6, self.atencion_6_letra))
                self.ventana_atenciones.boton_atencion_6.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_7.configure(text = self.atencion_7_nombre, command = lambda: self.llamar_turno(7, self.atencion_7_letra))
                self.ventana_atenciones.boton_atencion_7.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_8.configure(text = self.atencion_8_nombre, command = lambda: self.llamar_turno(8, self.atencion_8_letra))
                self.ventana_atenciones.boton_atencion_8.pack(fill = "x", expand = 1, padx = 5, pady = 5)
            case "9":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                self.atencion_4_letra = self.frame_atenciones_individuales.entry_letra_atencion_4.get().upper()
                self.atencion_4_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_4.get().upper()
                self.atencion_5_letra = self.frame_atenciones_individuales.entry_letra_atencion_5.get().upper()
                self.atencion_5_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_5.get().upper()
                self.atencion_6_letra = self.frame_atenciones_individuales.entry_letra_atencion_6.get().upper()
                self.atencion_6_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_6.get().upper()
                self.atencion_7_letra = self.frame_atenciones_individuales.entry_letra_atencion_7.get().upper()
                self.atencion_7_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_7.get().upper()
                self.atencion_8_letra = self.frame_atenciones_individuales.entry_letra_atencion_8.get().upper()
                self.atencion_8_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_8.get().upper()
                self.atencion_9_letra = self.frame_atenciones_individuales.entry_letra_atencion_9.get().upper()
                self.atencion_9_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_9.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1 or len(self.atencion_4_letra) > 1 or len(self.atencion_5_letra) > 1 or len(self.atencion_6_letra) > 1 or len(self.atencion_7_letra) > 1 or len(self.atencion_8_letra) > 1 or len(self.atencion_9_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1 or len(self.atencion_4_letra) < 1 or len(self.atencion_5_letra) < 1 or len(self.atencion_6_letra) < 1 or len(self.atencion_7_letra) < 1 or len(self.atencion_8_letra) < 1 or len(self.atencion_9_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1 or len(self.atencion_4_nombre) < 1 or len(self.atencion_5_nombre) < 1 or len(self.atencion_6_nombre) < 1 or len(self.atencion_7_nombre) < 1 or len(self.atencion_8_nombre) < 1 or len(self.atencion_9_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.listado_nombres.append(self.atencion_4_nombre)
                self.listado_letras.append(self.atencion_4_letra)
                self.listado_nombres.append(self.atencion_5_nombre)
                self.listado_letras.append(self.atencion_5_letra)
                self.listado_nombres.append(self.atencion_6_nombre)
                self.listado_letras.append(self.atencion_6_letra)
                self.listado_nombres.append(self.atencion_7_nombre)
                self.listado_letras.append(self.atencion_7_letra)
                self.listado_nombres.append(self.atencion_8_nombre)
                self.listado_letras.append(self.atencion_8_letra)
                self.listado_nombres.append(self.atencion_9_nombre)
                self.listado_letras.append(self.atencion_9_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_4.configure(text = self.atencion_4_nombre, command = lambda: self.llamar_turno(4, self.atencion_4_letra))
                self.ventana_atenciones.boton_atencion_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_5.configure(text = self.atencion_5_nombre, command = lambda: self.llamar_turno(5, self.atencion_5_letra))
                self.ventana_atenciones.boton_atencion_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_6.configure(text = self.atencion_6_nombre, command = lambda: self.llamar_turno(6, self.atencion_6_letra))
                self.ventana_atenciones.boton_atencion_6.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_7.configure(text = self.atencion_7_nombre, command = lambda: self.llamar_turno(7, self.atencion_7_letra))
                self.ventana_atenciones.boton_atencion_7.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_8.configure(text = self.atencion_8_nombre, command = lambda: self.llamar_turno(8, self.atencion_8_letra))
                self.ventana_atenciones.boton_atencion_8.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_9.configure(text = self.atencion_9_nombre, command = lambda: self.llamar_turno(9, self.atencion_9_letra))
                self.ventana_atenciones.boton_atencion_9.pack(fill = "x", expand = 1, padx = 5, pady = 5)   
            case "10":
                self.atencion_1_letra = self.frame_atenciones_individuales.entry_letra_atencion_1.get().upper()
                self.atencion_1_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_1.get().upper()
                self.atencion_2_letra = self.frame_atenciones_individuales.entry_letra_atencion_2.get().upper()
                self.atencion_2_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_2.get().upper()
                self.atencion_3_letra = self.frame_atenciones_individuales.entry_letra_atencion_3.get().upper()
                self.atencion_3_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_3.get().upper()
                self.atencion_4_letra = self.frame_atenciones_individuales.entry_letra_atencion_4.get().upper()
                self.atencion_4_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_4.get().upper()
                self.atencion_5_letra = self.frame_atenciones_individuales.entry_letra_atencion_5.get().upper()
                self.atencion_5_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_5.get().upper()
                self.atencion_6_letra = self.frame_atenciones_individuales.entry_letra_atencion_6.get().upper()
                self.atencion_6_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_6.get().upper()
                self.atencion_7_letra = self.frame_atenciones_individuales.entry_letra_atencion_7.get().upper()
                self.atencion_7_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_7.get().upper()
                self.atencion_8_letra = self.frame_atenciones_individuales.entry_letra_atencion_8.get().upper()
                self.atencion_8_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_8.get().upper()
                self.atencion_9_letra = self.frame_atenciones_individuales.entry_letra_atencion_9.get().upper()
                self.atencion_9_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_9.get().upper()
                self.atencion_10_letra = self.frame_atenciones_individuales.entry_letra_atencion_10.get().upper()
                self.atencion_10_nombre = self.frame_atenciones_individuales.entry_nombre_atencion_10.get().upper()
                if len(self.atencion_1_letra) > 1 or len(self.atencion_2_letra) > 1 or len(self.atencion_3_letra) > 1 or len(self.atencion_4_letra) > 1 or len(self.atencion_5_letra) > 1 or len(self.atencion_6_letra) > 1 or len(self.atencion_7_letra) > 1 or len(self.atencion_8_letra) > 1 or len(self.atencion_9_letra) > 1 or len(self.atencion_10_letra) > 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                    return
                if len(self.atencion_1_letra) < 1 or len(self.atencion_2_letra) < 1 or len(self.atencion_3_letra) < 1 or len(self.atencion_4_letra) < 1 or len(self.atencion_5_letra) < 1 or len(self.atencion_6_letra) < 1 or len(self.atencion_7_letra) < 1 or len(self.atencion_8_letra) < 1 or len(self.atencion_9_letra) < 1 or len(self.atencion_10_letra) < 1:
                    CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                    return
                if len(self.atencion_1_nombre) < 1 or len(self.atencion_2_nombre) < 1 or len(self.atencion_3_nombre) < 1 or len(self.atencion_4_nombre) < 1 or len(self.atencion_5_nombre) < 1 or len(self.atencion_6_nombre) < 1 or len(self.atencion_7_nombre) < 1 or len(self.atencion_8_nombre) < 1 or len(self.atencion_9_nombre) < 1 or len(self.atencion_10_nombre) < 1:
                    CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                    return
                self.listado_nombres.append(self.atencion_1_nombre)
                self.listado_letras.append(self.atencion_1_letra)
                self.listado_nombres.append(self.atencion_2_nombre)
                self.listado_letras.append(self.atencion_2_letra)
                self.listado_nombres.append(self.atencion_3_nombre)
                self.listado_letras.append(self.atencion_3_letra)
                self.listado_nombres.append(self.atencion_4_nombre)
                self.listado_letras.append(self.atencion_4_letra)
                self.listado_nombres.append(self.atencion_5_nombre)
                self.listado_letras.append(self.atencion_5_letra)
                self.listado_nombres.append(self.atencion_6_nombre)
                self.listado_letras.append(self.atencion_6_letra)
                self.listado_nombres.append(self.atencion_7_nombre)
                self.listado_letras.append(self.atencion_7_letra)
                self.listado_nombres.append(self.atencion_8_nombre)
                self.listado_letras.append(self.atencion_8_letra)
                self.listado_nombres.append(self.atencion_9_nombre)
                self.listado_letras.append(self.atencion_9_letra)
                self.listado_nombres.append(self.atencion_10_nombre)
                self.listado_letras.append(self.atencion_10_letra)
                self.set_listado_nombres = set(self.listado_nombres)
                self.set_listado_letras = set(self.listado_letras)
                if len(self.set_listado_nombres) != len(self.listado_nombres) or len(self.set_listado_letras) != len(self.listado_letras):
                    CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                    return
                self.ventana_atenciones.boton_atencion_1.configure(text = self.atencion_1_nombre, command = lambda: self.llamar_turno(1, self.atencion_1_letra))
                self.ventana_atenciones.boton_atencion_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_2.configure(text = self.atencion_2_nombre, command = lambda: self.llamar_turno(2, self.atencion_2_letra))
                self.ventana_atenciones.boton_atencion_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_3.configure(text = self.atencion_3_nombre, command = lambda: self.llamar_turno(3, self.atencion_3_letra))
                self.ventana_atenciones.boton_atencion_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_4.configure(text = self.atencion_4_nombre, command = lambda: self.llamar_turno(4, self.atencion_4_letra))
                self.ventana_atenciones.boton_atencion_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_5.configure(text = self.atencion_5_nombre, command = lambda: self.llamar_turno(5, self.atencion_5_letra))
                self.ventana_atenciones.boton_atencion_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_6.configure(text = self.atencion_6_nombre, command = lambda: self.llamar_turno(6, self.atencion_6_letra))
                self.ventana_atenciones.boton_atencion_6.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_7.configure(text = self.atencion_7_nombre, command = lambda: self.llamar_turno(7, self.atencion_7_letra))
                self.ventana_atenciones.boton_atencion_7.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_8.configure(text = self.atencion_8_nombre, command = lambda: self.llamar_turno(8, self.atencion_8_letra))
                self.ventana_atenciones.boton_atencion_8.pack(fill = "x", expand = 1, padx = 5, pady = 5)
                self.ventana_atenciones.boton_atencion_9.configure(text = self.atencion_9_nombre, command = lambda: self.llamar_turno(9, self.atencion_9_letra))
                self.ventana_atenciones.boton_atencion_9.pack(fill = "x", expand = 1, padx = 5, pady = 5)   
                self.ventana_atenciones.boton_atencion_10.configure(text = self.atencion_10_nombre, command = lambda: self.llamar_turno(10, self.atencion_10_letra))
                self.ventana_atenciones.boton_atencion_10.pack(fill = "x", expand = 1, padx = 5, pady = 5)   
                


        self.mostrar_atenciones("menu")


    def llamar_turno(self, atencion, letra):
        print(f"{atencion} - {letra}")

    ####----MÉTODO PARA DESHABILITAR BOTONES CUANDO NO QUIERO QUE SEAN MANIPULADOS----####
    def nulo(self):
        pass

####----CLASE PARA CREAR EL FRAME DEL MENÚ PRINCIPAL----####   
class MenuPrincipal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_botones_inicio = ctk.CTkFrame(master=master, height= 100)
        self.frame_botones_inicio.pack(fill = "x", padx = 5)
        self.boton_configuracion = ctk.CTkButton(master=self.frame_botones_inicio, text='Configuración', command= lambda: master.mostrar_menu_config("menu"))
        self.boton_configuracion.pack(side = "left", fill = "x", expand = 1, padx = 5, pady = 5)
        self.boton_atenciones = ctk.CTkButton(master=self.frame_botones_inicio, text='Atenciones', command= lambda: master.mostrar_atenciones("menu"))
        self.boton_atenciones.pack(side = "left", fill = "x", expand = 1, padx = 5, pady = 5)
        self.boton_video = ctk.CTkButton(master=self.frame_botones_inicio, text='Video', command= lambda: master.mostrar_video("menu"))
        self.boton_video.pack(side = "left", fill = "x", expand = 1, padx = 5, pady = 5)

####----CLASE PARA CREAR EL FRAME DEL MENÚ CONFIGURACIÓN----####  
class VentanaConfig(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_botones_config = ctk.CTkFrame(master=master, height= 100)
        self.boton_config_atenciones = ctk.CTkButton(master=self.frame_botones_config, text='Atenciones', command= lambda: master.mostrar_config_atenciones("menu"))
        self.boton_config_atenciones.pack(side = "left", fill = "x", expand = 1, padx = 5, pady = 5)
        self.boton_config_server = ctk.CTkButton(master=self.frame_botones_config, text='Servidor')
        self.boton_config_server.pack(side = "left", fill = "x", expand = 1, padx = 5, pady = 5)
        self.boton_config_video = ctk.CTkButton(master=self.frame_botones_config, text='Video')
        self.boton_config_video.pack(side = "left", fill = "x", expand = 1, padx = 5, pady = 5)

####----CLASE PARA CREAR EL FRAME DEL MENÚ ATENCIONES----####  
class VentanaAtenciones(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_atenciones = ctk.CTkFrame(master=master, height= 100)
        self.frame_botones_atenciones = ctk.CTkFrame(self.frame_atenciones)
        self.frame_botones_atenciones.pack(fill = "x", side = "left", padx = 5, pady = 5, expand = 1)
        self.boton_atencion_1 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 1")
        self.boton_atencion_2 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 2")
        self.boton_atencion_3 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 3")
        self.boton_atencion_4 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 4")
        self.boton_atencion_5 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 5")
        self.boton_atencion_6 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 6")
        self.boton_atencion_7 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 7")
        self.boton_atencion_8 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 8")
        self.boton_atencion_9 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 9")
        self.boton_atencion_10 = ctk.CTkButton(self.frame_botones_atenciones, text= "Atención 10")
        self.frame_label_contadores = ctk.CTkFrame(self.frame_atenciones)
        self.frame_label_contadores.pack(fill = "x", side = "left", padx = 5, pady = 5, expand = 1)
        self.label_num_atencion_1 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_2 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_3 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_4 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_5 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_6 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_7 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_8 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_9 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_num_atencion_10 = ctk.CTkLabel(self.frame_label_contadores, text= "000")
        self.label_letra_atencion1 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion2 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion3 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion4 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion5 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion6 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion7 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion8 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion9 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        self.label_letra_atencion10 = ctk.CTkLabel(self.frame_label_contadores, text= "Letra")
        
        

####----CLASE PARA CREAR EL FRAME DEL MENÚ VIDEO----####  
class VentanaVideo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_video = ctk.CTkFrame(master=master, height= 100)
          
        
####----CLASE PARA CREAR ELFRAME DE CONFIGURACIÓN DE ATENCIONES----####
class VentanaConfigAtenciones(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_config_atenciones = ctk.CTkFrame(master=master, height= 100)
        self.etiqueta_preferencial = ctk.CTkLabel(self.frame_config_atenciones, text= "Activar Atención Preferencial: ")
        self.etiqueta_preferencial.pack(side = "left",padx = 5, pady = 5)
        self.toggle_preferencial = ctk.CTkCheckBox(self.frame_config_atenciones, text= "Off", variable= master.estado_preferencial, onvalue= "On", offvalue= "Off", command= master.activar_preferencial)
        self.toggle_preferencial.pack(side = "left",padx = 5, pady = 5)
        self.etiqueta_cant_atenciones = ctk.CTkLabel(self.frame_config_atenciones, text= "Cantidad de Atenciones Deseadas: ")
        self.etiqueta_cant_atenciones.pack(side = "left",padx = 5, pady = 5)
        self.dropmenu_cant_atenciones = ctk.CTkOptionMenu(self.frame_config_atenciones, values= ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
        self.dropmenu_cant_atenciones.pack(side = "left",padx = 5, pady = 5)
        
        

class FrameAtenciones(ctk.CTkFrame):
    def __init__(self, config, master):
        super().__init__(master)
        self.frame_creacion_atenciones = ctk.CTkFrame(master= master, height= 100)
        self.boton_definir_atenciones = ctk.CTkButton(self.frame_creacion_atenciones, text = "Definir Atenciones", command= lambda: self.definir_atenciones(master, f"{master.ventana_config_atenciones.dropmenu_cant_atenciones.get()}"))
        self.boton_definir_atenciones.pack(padx = 5, pady = 5)
        

    def definir_atenciones(self, master, num):
        self.boton_definir_atenciones.configure(command = master.nulo)
        ####----SWITCH PARA MOSTRAR LA CANTIDAD DESEADA DE ATENCIONES----####
        match num:
            case "1":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "2":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "3":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "4":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_4(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "5":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_4(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_5(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                
            case "6":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_4(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_5(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_6(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "7":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_4(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_5(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_6(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_7(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "8":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_4(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_5(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_6(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_7(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_8(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "9":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_4(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_5(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_6(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_7(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_8(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_9(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
            case "10":
                master.frame_atenciones_individuales.atencion_1(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_2(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_3(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_4(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_5(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_6(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_7(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_8(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_9(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.atencion_10(self.frame_creacion_atenciones)
                master.frame_atenciones_individuales.boton_cancelar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                master.frame_atenciones_individuales.boton_confirmar_definir_atenciones.pack(side = "right", padx = 5, pady = 5)
                 
                
                
class FrameAtencionesIndividuales(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.frame_atencion_1 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_1 = ctk.CTkLabel(self.frame_atencion_1, text= "Nombre Atención  1: ")
        self.entry_nombre_atencion_1 = ctk.CTkEntry(self.frame_atencion_1, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_1 = ctk.CTkLabel(self.frame_atencion_1, text= "Letra Atención  1: ")
        self.entry_letra_atencion_1 = ctk.CTkEntry(self.frame_atencion_1, placeholder_text= "Letra", width= 50)

        self.frame_atencion_2 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_2 = ctk.CTkLabel(self.frame_atencion_2, text= "Nombre Atención  2: ")
        self.entry_nombre_atencion_2 = ctk.CTkEntry(self.frame_atencion_2, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_2 = ctk.CTkLabel(self.frame_atencion_2, text= "Letra Atención  2: ")
        self.entry_letra_atencion_2 = ctk.CTkEntry(self.frame_atencion_2, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_3 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_3 = ctk.CTkLabel(self.frame_atencion_3, text= "Nombre Atención  3: ")
        self.entry_nombre_atencion_3 = ctk.CTkEntry(self.frame_atencion_3, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_3 = ctk.CTkLabel(self.frame_atencion_3, text= "Letra Atención  3: ")
        self.entry_letra_atencion_3 = ctk.CTkEntry(self.frame_atencion_3, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_4 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_4 = ctk.CTkLabel(self.frame_atencion_4, text= "Nombre Atención  4: ")
        self.entry_nombre_atencion_4 = ctk.CTkEntry(self.frame_atencion_4, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_4 = ctk.CTkLabel(self.frame_atencion_4, text= "Letra Atención  4: ")
        self.entry_letra_atencion_4 = ctk.CTkEntry(self.frame_atencion_4, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_5 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_5 = ctk.CTkLabel(self.frame_atencion_5, text= "Nombre Atención  5: ")
        self.entry_nombre_atencion_5 = ctk.CTkEntry(self.frame_atencion_5, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_5 = ctk.CTkLabel(self.frame_atencion_5, text= "Letra Atención  5: ")
        self.entry_letra_atencion_5 = ctk.CTkEntry(self.frame_atencion_5, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_6 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_6 = ctk.CTkLabel(self.frame_atencion_6, text= "Nombre Atención  6: ")
        self.entry_nombre_atencion_6 = ctk.CTkEntry(self.frame_atencion_6, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_6 = ctk.CTkLabel(self.frame_atencion_6, text= "Letra Atención  6: ")
        self.entry_letra_atencion_6 = ctk.CTkEntry(self.frame_atencion_6, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_7 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_7 = ctk.CTkLabel(self.frame_atencion_7, text= "Nombre Atención  7: ")
        self.entry_nombre_atencion_7 = ctk.CTkEntry(self.frame_atencion_7, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_7 = ctk.CTkLabel(self.frame_atencion_7, text= "Letra Atención  7: ")
        self.entry_letra_atencion_7 = ctk.CTkEntry(self.frame_atencion_7, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_8 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_8 = ctk.CTkLabel(self.frame_atencion_8, text= "Nombre Atención  8: ")
        self.entry_nombre_atencion_8 = ctk.CTkEntry(self.frame_atencion_8, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_8 = ctk.CTkLabel(self.frame_atencion_8, text= "Letra Atención  8: ")
        self.entry_letra_atencion_8 = ctk.CTkEntry(self.frame_atencion_8, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_9 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_9 = ctk.CTkLabel(self.frame_atencion_9, text= "Nombre Atención  9: ")
        self.entry_nombre_atencion_9 = ctk.CTkEntry(self.frame_atencion_9, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_9 = ctk.CTkLabel(self.frame_atencion_9, text= "Letra Atención  9: ")
        self.entry_letra_atencion_9 = ctk.CTkEntry(self.frame_atencion_9, placeholder_text= "Letra", width= 50)
        
        self.frame_atencion_10 = ctk.CTkFrame(master= master, height= 100)
        self.etiqueta_nombre_atencion_10 = ctk.CTkLabel(self.frame_atencion_10, text= "Nombre Atención 10:")
        self.entry_nombre_atencion_10 = ctk.CTkEntry(self.frame_atencion_10, placeholder_text= "Nombre", width= 250)
        self.etiqueta_letra_atencion_10 = ctk.CTkLabel(self.frame_atencion_10, text= "Letra Atención 10:")
        self.entry_letra_atencion_10 = ctk.CTkEntry(self.frame_atencion_10, placeholder_text= "Letra", width= 50)
        
        self.boton_cancelar_definir_atenciones = ctk.CTkButton(master, text = "Cancelar", command= app.reset_config)
        self.boton_confirmar_definir_atenciones = ctk.CTkButton(master, text = "Confirmar", command= lambda: app.crear_pantalla_atenciones(f"{app.ventana_config_atenciones.dropmenu_cant_atenciones.get()}"))
        
    

    def atencion_1(self, master):
        self.frame_atencion_1.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_1.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_1.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_1.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_1.pack(side = "left", padx = 5, pady = 5)
        
    def atencion_2(self, master):
        
        self.frame_atencion_2.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_2.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_2.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_2.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_2.pack(side = "left", padx = 5, pady = 5)

    def atencion_3(self, master):
        self.frame_atencion_3.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_3.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_3.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_3.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_3.pack(side = "left", padx = 5, pady = 5)

    def atencion_4(self, master):
        self.frame_atencion_4.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_4.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_4.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_4.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_4.pack(side = "left", padx = 5, pady = 5)

    def atencion_5(self, master):
        self.frame_atencion_5.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_5.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_5.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_5.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_5.pack(side = "left", padx = 5, pady = 5)

    def atencion_6(self, master):
        self.frame_atencion_6.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_6.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_6.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_6.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_6.pack(side = "left", padx = 5, pady = 5)

    def atencion_7(self, master):
        self.frame_atencion_7.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_7.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_7.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_7.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_7.pack(side = "left", padx = 5, pady = 5)

    def atencion_8(self, master):
        self.frame_atencion_8.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_8.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_8.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_8.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_8.pack(side = "left", padx = 5, pady = 5)

    def atencion_9(self, master):
        self.frame_atencion_9.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_9.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_9.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_9.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_9.pack(side = "left", padx = 5, pady = 5)

    def atencion_10(self, master):
        self.frame_atencion_10.pack(fill = "x", padx = 5)
        self.etiqueta_nombre_atencion_10.pack(side = "left", padx = 5, pady = 5)
        self.entry_nombre_atencion_10.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_letra_atencion_10.pack(side = "left", padx = 5, pady = 5)    
        self.entry_letra_atencion_10.pack(side = "left", padx = 5, pady = 5)






"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""
app = App()
app.mainloop()

