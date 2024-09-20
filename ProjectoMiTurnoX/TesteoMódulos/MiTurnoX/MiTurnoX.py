import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from config import config
from collections import deque
import psycopg2
import socket

        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ####----SETEO BASE DE VENTANA PRINCIPAL----####
        #self.minsize(700, 560)
        self.title("Mi Turno X - V 0.0.10")
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
        self.status_config_usuarios = False
        ####----CREACIÓN DE MENÚ PRINCIPAL----####
        self.menu_principal = MenuPrincipal(self)
        ####----WIDGETS----####
        self.ventana_atenciones = VentanaAtenciones(self)
        self.ventana_config = VentanaConfig(self)
        self.ventana_video = VentanaVideo(self)
        self.ventana_config_atenciones = VentanaConfigAtenciones(self)
        self.ventana_config_usuarios = VentanaConfigUsuarios(self)
        self.main_frame_creacion_usuarios = FrameCreacionUsuarios(self.ventana_config_usuarios.main_frame_usuarios, self)
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
            if self.status_config_usuarios == True:
                self.esconder_config_usuarios()
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
            self.ventana_config.boton_config_atenciones.configure(command = self.esconder_config_atenciones)

    def esconder_config_atenciones(self):
        self.ventana_config_atenciones.frame_config_atenciones.pack_forget()
        self.frame_nombrar_atenciones.frame_creacion_atenciones.pack_forget()
        self.status_config_atenciones = False
        self.ventana_config.boton_config_atenciones.configure(command = lambda : self.mostrar_config_atenciones("menu"))

    def mostrar_config_usuarios(self):
        self.ventana_config_usuarios.main_frame_usuarios.pack(fill = "x", padx = 5)
        self.status_config_usuarios = True
        self.ventana_config.boton_config_usuarios.configure(command = self.esconder_config_usuarios)

    def esconder_config_usuarios(self):
        self.ventana_config_usuarios.main_frame_usuarios.pack_forget()
        self.status_config_usuarios = False
        self.ventana_config.boton_config_usuarios.configure(command = self.mostrar_config_usuarios)

    def mostrar_crear_usuario(self):
        self.ventana_config_usuarios.boton_crear_usuarios.configure(command = self.esconder_crear_usuario)
        self.main_frame_creacion_usuarios.frame_creacion_usuarios.pack(fill = "x", expand = 1, padx = 5, pady = 5)
    
    def esconder_crear_usuario(self):
        self.ventana_config_usuarios.boton_crear_usuarios.configure(command = self.mostrar_crear_usuario)
        self.main_frame_creacion_usuarios.cancelar_creacion_usuario()

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
    def crear_pantalla_atenciones(self, num, estado):
        self.num = num
        self.estado = estado
        self.db_num_atn = []
        self.listado_nombres = []
        self.listado_letras = []
        self.estados = []
        self.db_atenciones = ()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
                for x in range(0, int(num)):
                    if self.estado == "On" and x == 0:
                        self.estados.append("TRUE")
                    else:
                        self.estados.append("FALSE")
                self.db_num_atn = [i for i in range(1, int(num) + 1)]
                self.db_atenciones = list(zip(self.db_num_atn, self.listado_nombres, self.listado_letras, self.estados))
                db_conn = None
                try:
                    params = config()
                    db_conn = psycopg2.connect(**params)
                    cur = db_conn.cursor()
                    cur.execute('''DELETE FROM atn_table''')
                    db_conn.commit()
                    for atenciones in self.db_atenciones:
                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter, atn_pref) VALUES(%s, %s, %s, %s)", atenciones)
                        db_conn.commit()
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if db_conn is not None:
                        db_conn.close()
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
        self.boton_config_usuarios = ctk.CTkButton(master=self.frame_botones_config, text='Usuarios', command= master.mostrar_config_usuarios)
        self.boton_config_usuarios.pack(side = "left", fill = "x", expand = 1, padx = 5, pady = 5)

####----PASAR CÓDIGO A MÓDULO DE PANTALLA----AJUSTAR---CLASE PARA CREAR EL FRAME DEL MENÚ ATENCIONES----####  
class VentanaAtenciones(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.listado_atn_arranque = []
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT atn_id, atn_name, atn_letter FROM atn_table')
            db_return = cur.fetchall()
            for id, name, letter in db_return:
                self.listado_atn_arranque.append((id, name, letter))
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        if not id:
            pass
        else:
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
            self.cantidad_atn_arranque = len(self.listado_atn_arranque)
            self.atn_arranque(master, self.cantidad_atn_arranque)
    #### REVISAR CÓDIGO PARA SEPARARLO HACIA EL MÓDULO DE PANTALLA####
    def atn_arranque(self, master, num):
        if num == 2:
            self.boton_atencion_2.configure(text = f"{self.listado_atn_arranque[1][1]}", command = lambda atn = self.listado_atn_arranque[1][0], letra = self.listado_atn_arranque[1][2] : master.llamar_turno(atn, letra))
            self.boton_atencion_2.pack()
            self.label_num_atencion_2.pack()
            self.label_letra_atencion2.pack()
    '''PSEUDO CÓDIGO PARA LA CREACIÓN Y LAS ATENCIONES CON RECURSIVIDAD, AJUSTAR EN MÓDULO DE PANTALLA SI ES NECESARIO
    funcion(num)
	si num = 10:
		funcion(num - 1)
		objs10 = indice 9
		objs10.pack
	elif num = 9:
		funcion(num - 1)
		objs9 = indice 8
		objs9.pack
	.
	.
	.
	elif num = 2:
		funcion(num - 1)
		objs2 = indice 1
		objs2.pack
	else:
		objs1 = indice 0
		objs1.pack
    '''



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
        self.boton_confirmar_definir_atenciones = ctk.CTkButton(master, text = "Confirmar", command= lambda: app.crear_pantalla_atenciones(f"{app.ventana_config_atenciones.dropmenu_cant_atenciones.get()}", f"{app.ventana_config_atenciones.toggle_preferencial.get()}"))
        
    

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


class VentanaConfigUsuarios(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.main_frame_usuarios = ctk.CTkFrame(master)
        self.frame_botones_usuarios = ctk.CTkFrame(self.main_frame_usuarios)
        self.frame_botones_usuarios.pack(fill = "x", padx = 5, pady = 5)
        self.boton_crear_usuarios = ctk.CTkButton(self.frame_botones_usuarios, text= "Crear Usuario", command= master.mostrar_crear_usuario)
        self.boton_crear_usuarios.pack(side = "left",  fill = "x", expand = 1, padx= 5, pady = 5)
        self.boton_eliminar_usuario = ctk.CTkButton(self.frame_botones_usuarios, text= "Eliminar Usuario")
        self.boton_eliminar_usuario.pack(side = "left",  fill = "x", expand = 1, padx= 5, pady = 5)
        self.boton_editar_usuario = ctk.CTkButton(self.frame_botones_usuarios, text= "Editar Usuario")
        self.boton_editar_usuario.pack(side = "left", fill = "x", expand = 1, padx= 5, pady = 5)

class FrameCreacionUsuarios(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        ###---VARIABLES Y DATOS IMPORTADOS DE BASE DE DATOS NECESARIOS PARA EL LLENADO---###
        self.listado_tipo_atenciones = ('Atención Simple', 'Atención Múltiple 1-1', 'Atención Múltiple 2-1', 'Atención Rebalse', 'Atención Libre')
        self.tipo_1_status = False
        self.tipo_2_status = False
        self.tipo_3_status = False
        self.tipo_4_status = False
        self.tipo_5_status = False
        self.listado_temp_atenciones = []
        self.listado_atenciones = []
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT atn_name FROM atn_table')
            db_return = cur.fetchall()
            for item in db_return:
                self.listado_temp_atenciones.append(item)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        for i in range (0, len(self.listado_temp_atenciones)):
            self.listado_atenciones.append(self.listado_temp_atenciones[i][0])
        ###---FRAME CONTENEDOR FORM PARA CREACIÓN DE USUARIO---###
        self.frame_creacion_usuarios = ctk.CTkFrame(master)
        ###---FRAME CONTENEDORES DE VALUE PAIRS---###
        self.frame_modulo_ejecutivo = ctk.CTkFrame(self.frame_creacion_usuarios)
        self.frame_modulo_ejecutivo.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.frame_nombre_ejecutivo = ctk.CTkFrame(self.frame_creacion_usuarios)
        self.frame_nombre_ejecutivo.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.frame_login_user = ctk.CTkFrame(self.frame_creacion_usuarios)
        self.frame_login_user.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.frame_user_pass = ctk.CTkFrame(self.frame_creacion_usuarios)
        self.frame_user_pass.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.frame_user_pass_confirm = ctk.CTkFrame(self.frame_creacion_usuarios)
        self.frame_user_pass_confirm.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.frame_tipo_atencion = ctk.CTkFrame(self.frame_creacion_usuarios)
        self.frame_tipo_atencion.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        ###
        self.etiqueta_modulo_ejecutivo = ctk.CTkLabel(self.frame_modulo_ejecutivo, text= "Número de Módulo: ")
        self.etiqueta_modulo_ejecutivo.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_nombre_ejecutivo = ctk.CTkLabel(self.frame_nombre_ejecutivo, text= "Nombre de Ejecutivo :")
        self.etiqueta_nombre_ejecutivo.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_login_user = ctk.CTkLabel(self.frame_login_user, text= "Login User :")
        self.etiqueta_login_user.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_user_pass = ctk.CTkLabel(self.frame_user_pass, text= "Contraseña :")
        self.etiqueta_user_pass.pack(side = "left", padx = 5, pady = 5)
        self.etiqueta_user_pass_confirm = ctk.CTkLabel(self.frame_user_pass_confirm, text= "Confirmar Contraseña :")
        self.etiqueta_user_pass_confirm.pack(side = "left", padx = 5, pady = 5)
        ###
        self.entry_modulo_ejecutivo = ctk.CTkEntry(self.frame_modulo_ejecutivo, placeholder_text= "#")
        self.entry_modulo_ejecutivo.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        self.entry_nombre_ejecutivo = ctk.CTkEntry(self.frame_nombre_ejecutivo, placeholder_text= "Nombre")
        self.entry_nombre_ejecutivo.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        self.entry_login_user = ctk.CTkEntry(self.frame_login_user, placeholder_text= "Usuario")
        self.entry_login_user.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        self.entry_user_pass = ctk.CTkEntry(self.frame_user_pass, placeholder_text= "Contraseña", show = "*")
        self.entry_user_pass.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        self.entry_user_pass_confirm = ctk.CTkEntry(self.frame_user_pass_confirm, placeholder_text= "Repetir Contraseña", show = "*")
        self.entry_user_pass_confirm.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        ###
        self.tipo_atencion = ctk.CTkOptionMenu(self.frame_tipo_atencion, values= self.listado_tipo_atenciones)
        self.tipo_atencion.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        self.boton_asignar_tipo = ctk.CTkButton(self.frame_tipo_atencion, text= "Asignar Tipo", command= lambda: self.actualizar_listado_atenciones(app))
        self.boton_asignar_tipo.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        self.boton_cancelar_asignar_tipo = ctk.CTkButton(self.frame_tipo_atencion, text= "Cancelar", command = self.cancelar_creacion_usuario)
        self.boton_cancelar_asignar_tipo.pack(fill = "x", expand = 1,side = "left", padx = 5, pady = 5)
        ###
        self.frame_asignar_tipo_1 = ctk.CTkFrame(app.ventana_config_usuarios.main_frame_usuarios)
        self.frame_asignar_tipo_1_1 = ctk.CTkFrame(self.frame_asignar_tipo_1)
        self.frame_asignar_tipo_1_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_1 = ctk.CTkLabel(self.frame_asignar_tipo_1_1, text= "Atención :  ")
        self.etiqueta_tipo_atencion_1.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_1 = ctk.CTkOptionMenu(self.frame_asignar_tipo_1_1, values= self.listado_atenciones)
        self.listado_tipo_atencion_1.pack(side = "left", padx = 5, pady = 5)
        self.boton_guardar_tipo_1 = ctk.CTkButton(self.frame_asignar_tipo_1, text= "Guardar", command= self.guardar_usr_simple)
        self.boton_guardar_tipo_1.pack(side = "left", padx = 5, pady = 5)
        ###
        self.frame_asignar_tipo_2_izq = ctk.CTkFrame(app.ventana_config_usuarios.main_frame_usuarios)
        self.frame_asignar_tipo_2_der = ctk.CTkFrame(app.ventana_config_usuarios.main_frame_usuarios)
        self.frame_asignar_tipo_2_1 = ctk.CTkFrame(self.frame_asignar_tipo_2_izq)
        self.frame_asignar_tipo_2_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_1 = ctk.CTkLabel(self.frame_asignar_tipo_2_1, text= "Atención 1 :  ")
        self.etiqueta_tipo_atencion_2_1.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_1 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_1, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_1.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_2 = ctk.CTkFrame(self.frame_asignar_tipo_2_izq)
        self.frame_asignar_tipo_2_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_2 = ctk.CTkLabel(self.frame_asignar_tipo_2_2, text= "Atención 2 :  ")
        self.etiqueta_tipo_atencion_2_2.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_2 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_2, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_2.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_3 = ctk.CTkFrame(self.frame_asignar_tipo_2_izq)
        self.frame_asignar_tipo_2_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_3 = ctk.CTkLabel(self.frame_asignar_tipo_2_3, text= "Atención 3 :  ")
        self.etiqueta_tipo_atencion_2_3.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_3 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_3, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_3.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_4 = ctk.CTkFrame(self.frame_asignar_tipo_2_izq)
        self.frame_asignar_tipo_2_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_4 = ctk.CTkLabel(self.frame_asignar_tipo_2_4, text= "Atención 4 :  ")
        self.etiqueta_tipo_atencion_2_4.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_4 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_4, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_4.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_5 = ctk.CTkFrame(self.frame_asignar_tipo_2_izq)
        self.frame_asignar_tipo_2_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_5 = ctk.CTkLabel(self.frame_asignar_tipo_2_5, text= "Atención 5 :  ")
        self.etiqueta_tipo_atencion_2_5.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_5 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_5, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_5.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_6 = ctk.CTkFrame(self.frame_asignar_tipo_2_der, height = 20)
        self.frame_asignar_tipo_2_6.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_6 = ctk.CTkLabel(self.frame_asignar_tipo_2_6, text= "Atención 6 :  ")
        self.etiqueta_tipo_atencion_2_6.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_6 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_6, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_6.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_7 = ctk.CTkFrame(self.frame_asignar_tipo_2_der)
        self.frame_asignar_tipo_2_7.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_7 = ctk.CTkLabel(self.frame_asignar_tipo_2_7, text= "Atención 7 :  ")
        self.etiqueta_tipo_atencion_2_7.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_7 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_7, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_7.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_8 = ctk.CTkFrame(self.frame_asignar_tipo_2_der)
        self.frame_asignar_tipo_2_8.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_8 = ctk.CTkLabel(self.frame_asignar_tipo_2_8, text= "Atención 8 :  ")
        self.etiqueta_tipo_atencion_2_8.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_8 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_8, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_8.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_9 = ctk.CTkFrame(self.frame_asignar_tipo_2_der)
        self.frame_asignar_tipo_2_9.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_9 = ctk.CTkLabel(self.frame_asignar_tipo_2_9, text= "Atención 9 :  ")
        self.etiqueta_tipo_atencion_2_9.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_9 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_9, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_9.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_2_10 = ctk.CTkFrame(self.frame_asignar_tipo_2_der)
        self.frame_asignar_tipo_2_10.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_2_10 = ctk.CTkLabel(self.frame_asignar_tipo_2_10, text= "Atención 10 :")
        self.etiqueta_tipo_atencion_2_10.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_2_10 = ctk.CTkOptionMenu(self.frame_asignar_tipo_2_10, values= self.listado_atenciones)
        self.listado_tipo_atencion_2_10.pack(side = "left", padx = 5, pady = 5)
        self.boton_guardar_tipo_2 = ctk.CTkButton(self.frame_asignar_tipo_2_izq, text= "Guardar")
        self.boton_guardar_tipo_2.pack(side = "left", padx = 5, pady = 5)
        ###
        self.frame_asignar_tipo_3 = ctk.CTkFrame(app.ventana_config_usuarios.main_frame_usuarios)
        self.frame_asignar_tipo_3_1 = ctk.CTkFrame(self.frame_asignar_tipo_3)
        self.frame_asignar_tipo_3_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_3_1 = ctk.CTkLabel(self.frame_asignar_tipo_3_1, text= "Atención 1 :  ")
        self.etiqueta_tipo_atencion_3_1.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_3_1 = ctk.CTkOptionMenu(self.frame_asignar_tipo_3_1, values= self.listado_atenciones)
        self.listado_tipo_atencion_3_1.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_3_2 = ctk.CTkFrame(self.frame_asignar_tipo_3)
        self.frame_asignar_tipo_3_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_3_2 = ctk.CTkLabel(self.frame_asignar_tipo_3_2, text= "Atención 2 :  ")
        self.etiqueta_tipo_atencion_3_2.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_3_2 = ctk.CTkOptionMenu(self.frame_asignar_tipo_3_2, values= self.listado_atenciones)
        self.listado_tipo_atencion_3_2.pack(side = "left", padx = 5, pady = 5)
        self.boton_guardar_tipo_3 = ctk.CTkButton(self.frame_asignar_tipo_3, text= "Guardar")
        self.boton_guardar_tipo_3.pack(side = "left", padx = 5, pady = 5)
        ###
        self.frame_asignar_tipo_4_izq = ctk.CTkFrame(app.ventana_config_usuarios.main_frame_usuarios)
        self.frame_asignar_tipo_4_der = ctk.CTkFrame(app.ventana_config_usuarios.main_frame_usuarios)
        self.frame_asignar_tipo_4_1 = ctk.CTkFrame(self.frame_asignar_tipo_4_izq)
        self.frame_asignar_tipo_4_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_1 = ctk.CTkLabel(self.frame_asignar_tipo_4_1, text= "Atención 1 :  ")
        self.etiqueta_tipo_atencion_4_1.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_1 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_1, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_1.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_2 = ctk.CTkFrame(self.frame_asignar_tipo_4_izq)
        self.frame_asignar_tipo_4_2.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_2 = ctk.CTkLabel(self.frame_asignar_tipo_4_2, text= "Atención 2 :  ")
        self.etiqueta_tipo_atencion_4_2.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_2 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_2, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_2.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_3 = ctk.CTkFrame(self.frame_asignar_tipo_4_izq)
        self.frame_asignar_tipo_4_3.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_3 = ctk.CTkLabel(self.frame_asignar_tipo_4_3, text= "Atención 3 :  ")
        self.etiqueta_tipo_atencion_4_3.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_3 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_3, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_3.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_4 = ctk.CTkFrame(self.frame_asignar_tipo_4_izq)
        self.frame_asignar_tipo_4_4.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_4 = ctk.CTkLabel(self.frame_asignar_tipo_4_4, text= "Atención 4 :  ")
        self.etiqueta_tipo_atencion_4_4.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_4 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_4, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_4.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_5 = ctk.CTkFrame(self.frame_asignar_tipo_4_izq)
        self.frame_asignar_tipo_4_5.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_5 = ctk.CTkLabel(self.frame_asignar_tipo_4_5, text= "Atención 5 :  ")
        self.etiqueta_tipo_atencion_4_5.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_5 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_5, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_5.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_6 = ctk.CTkFrame(self.frame_asignar_tipo_4_der)
        self.frame_asignar_tipo_4_6.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_6 = ctk.CTkLabel(self.frame_asignar_tipo_4_6, text= "Atención 6 :  ")
        self.etiqueta_tipo_atencion_4_6.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_6 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_6, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_6.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_7 = ctk.CTkFrame(self.frame_asignar_tipo_4_der)
        self.frame_asignar_tipo_4_7.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_7 = ctk.CTkLabel(self.frame_asignar_tipo_4_7, text= "Atención 7 :  ")
        self.etiqueta_tipo_atencion_4_7.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_7 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_7, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_7.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_8 = ctk.CTkFrame(self.frame_asignar_tipo_4_der)
        self.frame_asignar_tipo_4_8.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_8 = ctk.CTkLabel(self.frame_asignar_tipo_4_8, text= "Atención 8 :  ")
        self.etiqueta_tipo_atencion_4_8.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_8 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_8, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_8.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_9 = ctk.CTkFrame(self.frame_asignar_tipo_4_der)
        self.frame_asignar_tipo_4_9.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_9 = ctk.CTkLabel(self.frame_asignar_tipo_4_9, text= "Atención 9 :  ")
        self.etiqueta_tipo_atencion_4_9.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_9 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_9, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_9.pack(side = "left", padx = 5, pady = 5)
        self.frame_asignar_tipo_4_10 = ctk.CTkFrame(self.frame_asignar_tipo_4_der)
        self.frame_asignar_tipo_4_10.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_4_10 = ctk.CTkLabel(self.frame_asignar_tipo_4_10, text= "Atención 10 :")
        self.etiqueta_tipo_atencion_4_10.pack(side = "left", padx = 5, pady = 5)
        self.listado_tipo_atencion_4_10 = ctk.CTkOptionMenu(self.frame_asignar_tipo_4_10, values= self.listado_atenciones)
        self.listado_tipo_atencion_4_10.pack(side = "left", padx = 5, pady = 5)
        self.boton_guardar_tipo_4 = ctk.CTkButton(self.frame_asignar_tipo_4_izq, text= "Guardar")
        self.boton_guardar_tipo_4.pack(side = "left", padx = 5, pady = 5)
        ###
        self.frame_asignar_tipo_5 = ctk.CTkFrame(app.ventana_config_usuarios.main_frame_usuarios)
        self.frame_asignar_tipo_5_1 = ctk.CTkFrame(self.frame_asignar_tipo_5)
        self.frame_asignar_tipo_5_1.pack(fill = "x", expand = 1, padx = 5, pady = 5)
        self.etiqueta_tipo_atencion_5 = ctk.CTkLabel(self.frame_asignar_tipo_5_1, text= "Llamado Libre Asignado.")
        self.etiqueta_tipo_atencion_5.pack(side = "left", padx = 5, pady = 5)
        self.boton_guardar_tipo_5 = ctk.CTkButton(self.frame_asignar_tipo_5, text= "Guardar")
        self.boton_guardar_tipo_5.pack(side = "left", padx = 5, pady = 5)
                
    def cancelar_creacion_usuario(self):
        self.frame_creacion_usuarios.pack_forget()
        self.entry_modulo_ejecutivo.delete(0, 'end')
        self.entry_nombre_ejecutivo.delete(0, 'end')
        self.entry_login_user.delete(0, 'end')
        self.entry_user_pass.delete(0, 'end')
        self.entry_user_pass_confirm.delete(0, 'end')
        self.frame_asignar_tipo_1.pack_forget()
        self.frame_asignar_tipo_2_izq.pack_forget()
        self.frame_asignar_tipo_2_der.pack_forget()
        self.frame_asignar_tipo_3.pack_forget()
        self.frame_asignar_tipo_4_izq.pack_forget()
        self.frame_asignar_tipo_4_der.pack_forget()
        self.frame_asignar_tipo_5.pack_forget()
        self.tipo_1_status = False
        self.tipo_2_status = False
        self.tipo_3_status = False
        self.tipo_4_status = False
        self.tipo_5_status = False
        app.ventana_config_usuarios.boton_crear_usuarios.configure(command = app.mostrar_crear_usuario)

    def mostrar_seleccionar_atenciones(self):
        self.tipo = self.tipo_atencion.get()
        self.cantidad_atenciones = len(self.listado_atenciones)
        match self.tipo:
            case "Atención Simple":
                if self.tipo_1_status == True:
                    return
                if self.tipo_2_status == True:
                    self.frame_asignar_tipo_2_izq.pack_forget()
                    self.frame_asignar_tipo_2_der.pack_forget()
                    self.tipo_2_status = False
                if self.tipo_3_status == True:
                    self.frame_asignar_tipo_3.pack_forget()
                    self.tipo_3_status = False
                if self.tipo_4_status == True:
                    self.frame_asignar_tipo_4_izq.pack_forget()
                    self.frame_asignar_tipo_4_der.pack_forget()
                    self.tipo_4_status = False
                if self.tipo_5_status == True:
                    self.frame_asignar_tipo_5.pack_forget()
                    self.tipo_5_status = False
                self.frame_asignar_tipo_1.pack(side = "left", fill = "x", expand = 1)
                self.tipo_1_status = True
            case "Atención Múltiple 1-1":
                if self.cantidad_atenciones == 1:
                    CTkMessagebox(title= "Error, solo existe una atención", message= "Seleccionar 'Atención simple' o 'Atención Libre'")
                    return
                if self.tipo_2_status == True:
                    return
                if self.tipo_1_status == True:
                    self.frame_asignar_tipo_1.pack_forget()
                    self.tipo_1_status = False
                if self.tipo_3_status == True:
                    self.frame_asignar_tipo_3.pack_forget()
                    self.tipo_3_status = False
                if self.tipo_4_status == True:
                    self.frame_asignar_tipo_4_izq.pack_forget()
                    self.frame_asignar_tipo_4_der.pack_forget()
                    self.tipo_4_status = False
                if self.tipo_5_status == True:
                    self.frame_asignar_tipo_5.pack_forget()
                    self.tipo_5_status = False
                if self.cantidad_atenciones > 5:
                    self.frame_asignar_tipo_2_izq.pack(side = "left", fill = "x", expand = 1)
                    self.frame_asignar_tipo_2_der.pack(side = "left", fill = "x", expand = 1, anchor = "n")
                else:
                    self.frame_asignar_tipo_2_izq.pack(side = "left", fill = "x", expand = 1)
                self.tipo_2_status = True
            case "Atención Múltiple 2-1":
                if self.tipo_3_status == True:
                    return
                if self.tipo_1_status == True:
                    self.frame_asignar_tipo_1.pack_forget()
                    self.tipo_1_status = False
                if self.tipo_2_status == True:
                    self.frame_asignar_tipo_2_izq.pack_forget()
                    self.frame_asignar_tipo_2_der.pack_forget()
                    self.tipo_2_status = False
                if self.tipo_4_status == True:
                    self.frame_asignar_tipo_4_izq.pack_forget()
                    self.frame_asignar_tipo_4_der.pack_forget()
                    self.tipo_4_status = False
                if self.tipo_5_status == True:
                    self.frame_asignar_tipo_5.pack_forget()
                    self.tipo_5_status = False
                self.frame_asignar_tipo_3.pack(side = "left", fill = "x", expand = 1)
                self.tipo_3_status = True
            case "Atención Rebalse":
                if self.cantidad_atenciones == 1:
                    CTkMessagebox(title= "Error, solo existe una atención", message= "Seleccionar 'Atención simple' o 'Atención Libre'")
                    return
                if self.tipo_4_status == True:
                    return
                if self.tipo_1_status == True:
                    self.frame_asignar_tipo_1.pack_forget()
                    self.tipo_1_status = False
                if self.tipo_2_status == True:
                    self.frame_asignar_tipo_2_izq.pack_forget()
                    self.frame_asignar_tipo_2_der.pack_forget()
                    self.tipo_2_status = False
                if self.tipo_3_status == True:
                    self.frame_asignar_tipo_3.pack_forget()
                    self.tipo_3_status = False
                if self.tipo_5_status == True:
                    self.frame_asignar_tipo_5.pack_forget()
                    self.tipo_5_status = False
                if self.cantidad_atenciones > 5:
                    self.frame_asignar_tipo_4_izq.pack(side = "left", fill = "x", expand = 1)
                    self.frame_asignar_tipo_4_der.pack(side = "left", fill = "x", expand = 1, anchor = "n")
                else:
                    self.frame_asignar_tipo_4_izq.pack(side = "left", fill = "x", expand = 1)
                self.tipo_4_status = True
            case "Atención Libre":
                if self.tipo_5_status == True:
                    return
                if self.tipo_1_status == True:
                    self.frame_asignar_tipo_1.pack_forget()
                    self.tipo_1_status = False
                if self.tipo_2_status == True:
                    self.frame_asignar_tipo_2_izq.pack_forget()
                    self.frame_asignar_tipo_2_der.pack_forget()
                    self.tipo_2_status = False
                if self.tipo_3_status == True:
                    self.frame_asignar_tipo_3.pack_forget()
                    self.tipo_3_status = False
                if self.tipo_4_status == True:
                    self.frame_asignar_tipo_4_izq.pack_forget()
                    self.frame_asignar_tipo_4_der.pack_forget()
                    self.tipo_4_status = False
                self.frame_asignar_tipo_5.pack(side = "left", fill = "x", expand = 1)
                self.tipo_5_status = True
                
    def actualizar_cantidad_atenciones(self, num):
        if num < 10:
            if num == 9:
                self.frame_asignar_tipo_2_10.pack_forget()
                self.frame_asignar_tipo_4_10.pack_forget()
                self.mostrar_seleccionar_atenciones()
            elif num == 8:
                self.frame_asignar_tipo_2_9.pack_forget()
                self.frame_asignar_tipo_4_9.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
            elif num == 7:
                self.frame_asignar_tipo_2_8.pack_forget()
                self.frame_asignar_tipo_4_8.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
            elif num == 6:
                self.frame_asignar_tipo_2_7.pack_forget()
                self.frame_asignar_tipo_4_7.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
            elif num == 5:
                self.frame_asignar_tipo_2_6.pack_forget()
                self.frame_asignar_tipo_4_6.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
            elif num == 4:
                self.frame_asignar_tipo_2_5.pack_forget()
                self.frame_asignar_tipo_4_5.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
            elif num == 3:
                self.frame_asignar_tipo_2_4.pack_forget()
                self.frame_asignar_tipo_4_4.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
            elif num == 2:
                self.frame_asignar_tipo_2_3.pack_forget()
                self.frame_asignar_tipo_4_3.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
            else:
                self.frame_asignar_tipo_2_2.pack_forget()
                self.frame_asignar_tipo_4_2.pack_forget()
                self.actualizar_cantidad_atenciones(num + 1)
        else:
            self.mostrar_seleccionar_atenciones()
            
    def actualizar_listado_atenciones(self, app):
        self.listado_temp_atenciones = []
        self.listado_atenciones = []
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT atn_name FROM atn_table')
            db_return = cur.fetchall()
            for item in db_return:
                self.listado_temp_atenciones.append(item)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        for i in range (0, len(self.listado_temp_atenciones)):
            self.listado_atenciones.append(self.listado_temp_atenciones[i][0])
        self.listado_tipo_atencion_1.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_1.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_2.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_3.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_4.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_5.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_6.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_7.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_8.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_9.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_2_10.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_3_1.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_3_2.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_1.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_2.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_3.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_4.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_5.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_6.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_7.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_8.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_9.configure(values = self.listado_atenciones)
        self.listado_tipo_atencion_4_10.configure(values = self.listado_atenciones)
        self.cantidad_actualizar_atenciones = len(self.listado_atenciones)
        self.actualizar_cantidad_atenciones(self.cantidad_actualizar_atenciones)
    
    def guardar_usr_simple(self):
        print(self.listado_tipo_atencion_1.get())
"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""
app = App()
app.mainloop()