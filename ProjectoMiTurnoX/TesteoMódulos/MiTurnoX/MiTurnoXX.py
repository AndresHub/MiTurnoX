import customtkinter as ctk
from customtkinter import StringVar
import os
from PIL import Image
from CTkMessagebox import CTkMessagebox
from config2 import *
from collections import deque
import psycopg2
import configparser

class MiTurnoX(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mi Turno X - Serdecom")
        ctk.set_appearance_mode("dark")
        self.MiTurnoX_win_height = 700
        self.MiTurnox_win_width = 1000
        self.screen_height = self.winfo_screenheight()
        self.screen_width = self.winfo_screenwidth()
        self.MiTurnoX_y_axis = int((self.screen_height/2) - (self.MiTurnoX_win_height/2))
        self.MiTurnoX_x_axis = int((self.screen_width/2) - (self.MiTurnox_win_width/2))
        self.geometry(f"{self.MiTurnox_win_width}x{self.MiTurnoX_win_height}+{self.MiTurnoX_x_axis}+{self.MiTurnoX_y_axis}")
        self.monitor_ventana_abierta = ""

    def botones_menu_principal(self, boton):
        self.etiqueta_miturnoX.forget()
        self.cerrar_ventana_anterior()
        match boton:
            case "atenciones":
                self.monitor_ventana_abierta = "atenciones"
                self.importar_listado_atenciones_db()
                self.etiqueta_espaciadora_2.configure(text = "Atenciones", font= ("CtkFont", 20))
                self.boton_editar.forget()
                self.boton_nuevo.forget()
                self.boton_borrar.forget()
                self.boton_nuevo.pack(side= "left", pady = 2, padx = 2)
                self.boton_editar.pack(side= "left", pady = 2, padx = 2)
                self.boton_borrar.pack(side= "left", pady = 2, padx = 2)
                self.boton_nuevo.configure(command = lambda: self.nuevo("atenciones"))
                self.boton_editar.configure(command = lambda: self.editar("atenciones"))
                self.boton_borrar.configure(command = lambda: self.borrar("atenciones"))
                self.frame_config_atenciones.pack(fill = "both", expand = 1,pady = 5, padx = 5)
            case "reglas":
                self.monitor_ventana_abierta = "reglas"
                self.importar_lista_reglas()
                self.etiqueta_espaciadora_2.configure(text = "Reglas de Atención", font= ("CtkFont", 20))
                self.boton_editar.forget()
                self.boton_nuevo.forget()
                self.boton_borrar.forget()
                self.boton_nuevo.pack(side= "left", pady = 2, padx = 2)
                self.boton_editar.pack(side= "left", pady = 2, padx = 2)
                self.boton_borrar.pack(side= "left", pady = 2, padx = 2)
                self.boton_nuevo.configure(command = lambda: self.nuevo("reglas"))
                self.boton_editar.configure(command = lambda: self.editar("reglas"))
                self.boton_borrar.configure(command = lambda: self.borrar("reglas"))
                self.frame_config_reglas.pack(fill = "both", expand = 1,pady = 5, padx = 5)
            case "pantalla":
                self.monitor_ventana_abierta = "pantalla"
                self.etiqueta_espaciadora_2.configure(text = "Pantalla", font= ("CtkFont", 20))
                self.boton_editar.forget()
                self.boton_nuevo.forget()
                self.boton_borrar.forget()
                self.frame_config_pantalla.pack(fill = "both", expand = 1, pady = 5, padx = 5)
            case "usuarios":
                self.monitor_ventana_abierta = "usuarios"
                self.etiqueta_espaciadora_2.configure(text = "Usuarios", font= ("CtkFont", 20))
                self.boton_editar.forget()
                self.boton_nuevo.forget()
                self.boton_borrar.forget()
                self.boton_nuevo.pack(side= "left", pady = 2, padx = 2)
                self.boton_editar.pack(side= "left", pady = 2, padx = 2)
                self.boton_borrar.pack(side= "left", pady = 2, padx = 2)
                self.boton_nuevo.configure(command = lambda: self.nuevo("usuarios"))
                self.boton_editar.configure(command = lambda: self.editar("usuarios"))
                self.boton_borrar.configure(command = lambda: self.borrar("usuarios"))
                self.frame_config_usuarios.pack(fill = "both", expand = 1, pady = 5, padx = 5)
            case "servidor":
                self.monitor_ventana_abierta = "servidor"
                self.etiqueta_espaciadora_2.configure(text = "Servidor", font= ("CtkFont", 20))
                self.boton_editar.forget()
                self.boton_nuevo.forget()
                self.boton_borrar.forget()
                self.boton_guardar.pack(side= "left", pady = 2, padx = 2)
                self.boton_guardar.configure(command = lambda: self.guardar("servidor"))
            case "impresora":
                self.monitor_ventana_abierta = "impresora"
                self.etiqueta_espaciadora_2.configure(text = "Impresora", font= ("CtkFont", 20))
                self.boton_editar.forget()
                self.boton_nuevo.forget()
                self.boton_borrar.forget()
                self.boton_guardar.pack(side= "left", pady = 2, padx = 2)
                self.boton_guardar.configure(command = lambda: self.guardar("impresora"))
            

    def cerrar_ventana_anterior(self):
        match self.monitor_ventana_abierta:
            case "":
                pass
            case "atenciones":
                self.frame_config_atenciones.destroy()
                self.menu_config_atenciones()
            case "reglas":
                self.frame_config_reglas.destroy()
                self.menu_config_reglas()
            case "pantalla":
                self.frame_config_pantalla.destroy()
                self.menu_config_pantalla()
            case "usuarios":
                self.frame_config_usuarios.destroy()
                self.menu_config_usuarios()
            case "servidor":
                pass
            case "impresora":
                pass



    def nuevo(self, boton):
        match boton:
            case "":
                pass
            case "atenciones":
                self.crear_frame_atencion("nueva_atencion", 0)
            case "usuarios":
                print("usuarios")
    
    def editar(self, boton):
        match boton:
            case "":
                pass
            case "atenciones":
                self.atencion_en_edicion = self.listado_atenciones.get()
                if self.atencion_en_edicion == "Atenciones":
                    CTkMessagebox(title= "Estimado Usuario :", message= "Seleccione la atención que desea editar, en el menú ´Atenciones´.")
                    return
                self.filtro_id_atencion()
                self.secuencia_editar = 0    
                self.listado_importar_atenciones = []
                conn = None
                try:
                    params = config()
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                    cur.execute('SELECT atn_id, atn_name, atn_letter FROM atn_table')
                    db_return = cur.fetchall()
                    for item in db_return:
                        self.listado_importar_atenciones.append(item)
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()
                for i in range (0, len(self.listado_importar_atenciones)):
                    if f"{self.listado_importar_atenciones[i][0]}" == f"{self.id_atencion_captura}":
                        self.crear_frame_atencion("editar_atencion", i)
                        break
    
    def borrar(self, boton):
        match boton:
            case "":
                pass
            case "atenciones":
                self.atencion_por_borrar = self.listado_atenciones.get()
                self.secuencia_borrar = 0
                for char in f"{self.atencion_por_borrar}":
                    if char == ' ':
                        break
                    elif char == '':
                        break
                    else:
                        self.secuencia_borrar +=1
                if self.listado_atenciones.get() == "Atenciones":
                    CTkMessagebox(title= "Estimado Usuario :", message= "Seleccione la atención que desea editar, en el menú ´Atenciones´.")
                    return
                if self.secuencia_borrar == 1:
                    self.id_atencion_borrar = f"{self.atencion_por_borrar[0]}"
                elif self.secuencia_borrar == 2:
                    self.id_atencion_borrar = f"{self.atencion_por_borrar[0]}{self.atencion_por_borrar[1]}"
                elif self.secuencia_borrar == 3:
                    self.id_atencion_borrar = f"{self.atencion_por_borrar[0]}{self.atencion_por_borrar[1]}{self.atencion_por_borrar[2]}"
                conn = None
                try:
                        params = config()
                        conn = psycopg2.connect(**params)
                        cur = conn.cursor()
                        cur.execute('DELETE FROM atn_table WHERE atn_id = %s', (self.id_atencion_borrar, ))
                        conn.commit()
                        cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        CTkMessagebox(title= "Mensaje de sistema :", message= "Falla al borrar elemento.")
                        return
                finally:
                    if conn is not None:
                        conn.close()
                self.importar_listado_atenciones_db()
                CTkMessagebox(title= "Mensaje de sistema :", message= "La atención se ha eliminado exitosamente.")

    def guardar(self, boton):
        match boton:
            case "":
                pass
            case "atenciones_nuevo":
                self.listado_temp_atenciones = []
                conn = None
                try:
                        params = config()
                        conn = psycopg2.connect(**params)
                        cur = conn.cursor()
                        cur.execute('SELECT atn_id, atn_name, atn_letter FROM atn_table')
                        db_return = cur.fetchall()
                        for item in db_return:
                            self.listado_temp_atenciones.append(item)
                        cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                finally:
                    if conn is not None:
                        conn.close()
                self.iteracion_completa = 1
                if self.listado_temp_atenciones == []:
                    conn = None
                    try:
                        params = config()
                        conn = psycopg2.connect(**params)
                        cur = conn.cursor()
                        if self.entry_num_atencion.get() == "" or f"{self.entry_nombre_atencion.get().upper()}" == "" or f"{self.entry_letra_atencion.get().upper()}" == "":
                            CTkMessagebox(title= "Mensaje de sistema :", message= "Falta llenar campos.")
                            return
                        else:
                            self.listado_atenciones_enviar = [int(self.entry_num_atencion.get()), f"{self.entry_nombre_atencion.get().upper()}", f"{self.entry_letra_atencion.get().upper()}" ]
                            cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter) VALUES(%s, %s, %s)", self.listado_atenciones_enviar)
                            conn.commit()
                            cur.close()
                    except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                    finally:
                        if conn is not None:
                            conn.close()
                    self.importar_listado_atenciones_db()
                    self.cancel("atenciones")
                    CTkMessagebox(title= "Mensaje de sistema :", message= "La atención se ha guardado exitosamente.")
                    self.boton_nuevo.configure(command = lambda: self.nuevo("atenciones"))
                else:
                    for i in range (0, len(self.listado_temp_atenciones)):
                        if f"{self.listado_temp_atenciones[i][0]}" == f"{self.entry_num_atencion.get()}" or self.listado_temp_atenciones[i][1] == f"{self.entry_nombre_atencion.get().upper()}" or self.listado_temp_atenciones[i][2] == f"{self.entry_letra_atencion.get().upper()}":
                            CTkMessagebox(title= "Estimado Usuario :", message= "No se pueden repetir valores ya existentes.")
                            break
                        else:
                            if self.iteracion_completa == len(self.listado_temp_atenciones):
                                conn = None
                                try:
                                    params = config()
                                    conn = psycopg2.connect(**params)
                                    cur = conn.cursor()
                                    if self.entry_num_atencion.get() == "" or f"{self.entry_nombre_atencion.get().upper()}" == "" or f"{self.entry_letra_atencion.get().upper()}" == "":
                                        CTkMessagebox(title= "Mensaje de sistema :", message= "Falta llenar campos.")
                                        return
                                    else:
                                        self.listado_atenciones_enviar = [int(self.entry_num_atencion.get()), f"{self.entry_nombre_atencion.get().upper()}", f"{self.entry_letra_atencion.get().upper()}" ]
                                        cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter) VALUES(%s, %s, %s)", self.listado_atenciones_enviar)
                                        conn.commit()
                                        cur.close()
                                except (Exception, psycopg2.DatabaseError) as error:
                                    print(error)
                                finally:
                                    if conn is not None:
                                        conn.close()
                                self.importar_listado_atenciones_db()
                                self.cancel("atenciones")
                                CTkMessagebox(title= "Mensaje de sistema :", message= "La atención se ha guardado exitosamente.")
                                self.boton_nuevo.configure(command = lambda: self.nuevo("atenciones"))
                            else:
                                self.iteracion_completa += 1
            case "atenciones_editar":
                self.id_atencion_saliente = self.id_atencion_captura
                conn = None            
                try:
                        params = config()
                        conn = psycopg2.connect(**params)
                        cur = conn.cursor()
                        cur.execute('DELETE FROM atn_table WHERE atn_id = %s', self.id_atencion_saliente)
                        conn.commit()
                        cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                finally:
                    if conn is not None:
                        conn.close()
                self.importar_listado_atenciones_db()
                self.iteracion_completa = 1
                self.nida = ""
                self.nnda = ""
                self.nlda = ""
                for i in range (0, len(self.listado_atenciones_db)):
                    if f"{self.listado_atenciones_db[i][0]}" == f"{self.entry_num_atencion.get()}" or f"{self.listado_atenciones_db[i][1]}" == f"{self.entry_nombre_atencion.get().upper()}" or f"{self.listado_atenciones_db[i][2]}" == f"{self.entry_letra_atencion.get().upper()}":
                        CTkMessagebox(title= "Estimado Usuario :", message= "No se pueden repetir valores ya existentes.")
                        break
                    else:
                        if self.iteracion_completa == len(self.listado_atenciones_db):
                            if f"{self.entry_num_atencion.get()}" == "":
                                self.nida = self.auto_id_atencion
                            else:
                                self.nida = self.entry_num_atencion.get().upper()
                            if f"{self.entry_nombre_atencion.get()}" == "":
                                self.nnda = self.auto_nombre_atencion
                            else:
                                self.nnda = self.entry_nombre_atencion.get().upper()
                            if f"{self.entry_letra_atencion.get()}" == "":
                                self.nlda = self.auto_letra_atencion
                            else:
                                self.nlda = self.entry_letra_atencion.get().upper()
                            conn = None
                            try:
                                params = config()
                                conn = psycopg2.connect(**params)
                                cur = conn.cursor()
                                self.listado_atenciones_enviar = [self.nida, self.nnda, self.nlda]
                                cur.execute("INSERT INTO atn_table(atn_id, atn_name, atn_letter) VALUES(%s, %s, %s)", self.listado_atenciones_enviar)
                                conn.commit()
                                cur.close()
                            except (Exception, psycopg2.DatabaseError) as error:
                                    print(error)
                            finally:
                                if conn is not None:
                                    conn.close()
                            self.importar_listado_atenciones_db()
                            self.cancel("atenciones")
                            CTkMessagebox(title= "Mensaje de sistema :", message= "La atención se ha guardado exitosamente.")
                            self.boton_editar.configure(command = lambda: self.editar("atenciones"))
                        else:
                            self.iteracion_completa += 1
            case "pantalla":
                self.nombre_ini = r'data/database2.ini'
                self.edit_config = configparser.ConfigParser()
                self.edit_config.read(self.nombre_ini)
                if f"{self.entry_ip_pantalla.get()}" == "" or f"{self.entry_puerto_pantalla.get()}" == "" or self.entry_msg_pantalla_1.get("1.0", "1.end") == "" or self.entry_msg_pantalla_2.get("1.0", "1.end") == "" or self.entry_msg_pantalla_3.get("1.0", "1.end") == "":
                    CTkMessagebox(title= "Estimado Usuario :", message= "No se pueden dejar campos en blanco.")
                else:
                    self.edit_config['pantalla']['host'] = f"{self.entry_ip_pantalla.get()}"
                    self.edit_config['pantalla']['port'] = f"{self.entry_puerto_pantalla.get()}"
                    self.edit_config['pantalla']['msg1'] = f"{self.entry_msg_pantalla_1.get("1.0", "1.end")}"
                    self.edit_config['pantalla']['msg2'] = f"{self.entry_msg_pantalla_2.get("1.0", "1.end")}"
                    self.edit_config['pantalla']['msg3'] = f"{self.entry_msg_pantalla_3.get("1.0", "1.end")}"
                    with open(self.nombre_ini, 'w') as configfile:
                        self.edit_config.write(configfile)
            case "usuarios":
                print("usuarios")
            case "servidor":
                print("servidor")
            case "impresora":
                print("impresora")
            
    def menu(self):
        self.frame_menu_principal = ctk.CTkFrame(self, width=200, height= self.MiTurnoX_win_height, corner_radius= 0)
        self.frame_menu_principal.pack(side = "left", anchor = "n", pady = 2, padx = 2)
        self.logo_serdecom = ctk.CTkImage(dark_image= Image.open(rf"{os.getcwd()}\Recursos\Imagenes\Serdecom_logo.png"), size = (180, 80))
        self.label_logo_serdecom = ctk.CTkLabel(self.frame_menu_principal, image= self.logo_serdecom, text="")
        self.label_logo_serdecom.pack(anchor = "n", pady = 2, padx = 2)
        self.config_atenciones = ctk.CTkButton(self.frame_menu_principal, width=180, height=30, text= "Atenciones", command= lambda: self.botones_menu_principal("atenciones"))
        self.config_atenciones.pack(anchor = "n", pady = 2, padx = 2)
        self.config_reglas_atencion = ctk.CTkButton(self.frame_menu_principal, width=180, height=30, text= "Reglas de Atención", command= lambda: self.botones_menu_principal("reglas"))
        self.config_reglas_atencion.pack(anchor = "n", pady = 2, padx = 2)
        self.config_pantalla = ctk.CTkButton(self.frame_menu_principal, width=180, height=30, text= "Pantalla", command= lambda: self.botones_menu_principal("pantalla"))
        self.config_pantalla.pack(anchor = "n", pady = 2, padx = 2)
        self.config_usuarios = ctk.CTkButton(self.frame_menu_principal, width=180, height=30, text= "Usuarios", command= lambda: self.botones_menu_principal("usuarios"))
        self.config_usuarios.pack(anchor = "n", pady = 2, padx = 2)
        self.config_servidor = ctk.CTkButton(self.frame_menu_principal, width=180, height=30, text= "Servidor", command= lambda: self.botones_menu_principal("servidor"))
        self.config_servidor.pack(anchor = "n", pady = 2, padx = 2)
        self.config_impresora = ctk.CTkButton(self.frame_menu_principal, width=180, height=30, text= "Impresora", command= lambda: self.botones_menu_principal("impresora"))
        self.config_impresora.pack(anchor = "n", pady = 2, padx = 2)

    def submenu(self):
        self.frame_submenu = ctk.CTkFrame(self, width=800, height= self.MiTurnoX_win_height, corner_radius= 5)
        self.frame_submenu.pack(side = "left", anchor = "n", pady = 2, padx = 2)
        self.frame_submenu_botones = ctk.CTkFrame(self.frame_submenu, height= 40, width= 800)
        self.frame_submenu_botones.pack(anchor = "n", pady = 5, padx = 5)
        self.frame_submenu_opciones = ctk.CTkFrame(self.frame_submenu, height= 650, width= 800)
        self.frame_submenu_opciones.pack(expand = 1, fill = "both", anchor = "n", pady = 5, padx = 5)
        self.etiqueta_miturnoX = ctk.CTkLabel(self.frame_submenu_opciones, width= 800, height= 650, text= "Mi Turno X", font= ("CtkFont", 150))
        self.etiqueta_miturnoX.pack()
        self.boton_nuevo = ctk.CTkButton(self.frame_submenu_botones, width=90, height=30, text= "Nuevo")
        self.boton_editar = ctk.CTkButton(self.frame_submenu_botones, width=90, height=30, text= "Editar")
        self.boton_borrar = ctk.CTkButton(self.frame_submenu_botones, width=90, height=30, text= "Borrar")
        self.etiqueta_opciones = ctk.CTkLabel(self.frame_submenu_opciones, width=180, height=30, text= "")
        self.lista_opciones = ctk.CTkOptionMenu(self.frame_submenu_opciones, width=180, height=30)
        self.etiqueta_espaciadora_1 = ctk.CTkLabel(self.frame_submenu, width= 800, height= (1/16), text= "")
        self.etiqueta_espaciadora_1.pack()
        self.etiqueta_espaciadora_2 = ctk.CTkLabel(self.frame_submenu_botones, width= 800, height= (1/16), text= "")
        self.etiqueta_espaciadora_2.pack()

    def menu_config_atenciones(self):
        self.frame_config_atenciones = ctk.CTkFrame(self.frame_submenu_opciones, height= 630, width= 780)
        self.listado_atenciones = ctk.CTkOptionMenu(self.frame_config_atenciones)
        self.listado_atenciones.set(value= "Atenciones")
        self.listado_atenciones.pack(anchor = "nw")
        self.etiqueta_numero_atencion = ctk.CTkLabel(self.frame_config_atenciones, text= "Total atenciones :")
        self.etiqueta_numero_atencion.pack(anchor = "w", padx = 5, pady = 5)
        self.seteo_etiqueta_numero_atencion()

    def menu_config_reglas(self):
        self.var_reglas = StringVar(value= 'Reglas')
        self.frame_config_reglas = ctk.CTkFrame(self.frame_submenu_opciones, height= 630, width= 780)
        self.lista_reglas = ctk.CTkOptionMenu(self.frame_config_reglas, variable= self.var_reglas)
        self.lista_reglas.pack(anchor = "nw")
        
    
    def menu_config_pantalla(self):
        self.info_pantalla = config3()
        self.var_ip_pantalla = StringVar(master= self, value= f"{self.info_pantalla['host']}")
        self.var_puerto_pantalla = StringVar(master= self, value= f"{self.info_pantalla['port']}")
        self.frame_config_pantalla = ctk.CTkFrame(self.frame_submenu_opciones, height= 630, width= 780)
        self.frame_ip_pantalla = ctk.CTkFrame(self.frame_config_pantalla) 
        self.frame_ip_pantalla.pack(expand = 1, fill = "y", anchor = "w")
        self.etiqueta_ip_pantalla = ctk.CTkLabel(self.frame_ip_pantalla, text= "IP de Pantalla :")
        self.etiqueta_ip_pantalla.pack(side = "left", padx = 2, pady = 2)
        self.entry_ip_pantalla = ctk.CTkEntry(self.frame_ip_pantalla, textvariable= self.var_ip_pantalla)
        self.entry_ip_pantalla.pack(side = "left", padx = 2, pady = 2)
        self.frame_puerto_pantalla = ctk.CTkFrame(self.frame_config_pantalla) 
        self.frame_puerto_pantalla.pack(expand = 1, fill = "y", anchor = "w")
        self.etiqueta_puerto_pantalla = ctk.CTkLabel(self.frame_puerto_pantalla, text= "Puerto de Pantalla :")
        self.etiqueta_puerto_pantalla.pack(side = "left", padx = 2, pady = 2)
        self.entry_puerto_pantalla = ctk.CTkEntry(self.frame_puerto_pantalla, textvariable= self.var_puerto_pantalla)
        self.entry_puerto_pantalla.pack(side = "left", padx = 2, pady = 2)
        self.frame_msg_pantalla_1 = ctk.CTkFrame(self.frame_config_pantalla) 
        self.frame_msg_pantalla_1.pack(expand = 1, fill = "y", anchor = "w")
        self.etiqueta_msg_pantalla_1 = ctk.CTkLabel(self.frame_msg_pantalla_1, text= "Mensaje de Pantalla 1 :")
        self.etiqueta_msg_pantalla_1.pack(side = "left", padx = 2, pady = 2)
        self.entry_msg_pantalla_1 = ctk.CTkTextbox(self.frame_msg_pantalla_1, wrap = ctk.WORD, width= 550, height= 100, font= ("helvetica", 15))
        self.entry_msg_pantalla_1.insert("1.0", text= f"{self.info_pantalla['msg1']}")
        self.entry_msg_pantalla_1.pack(side = "left", padx  = 2, pady = 2)
        self.frame_msg_pantalla_2 = ctk.CTkFrame(self.frame_config_pantalla) 
        self.frame_msg_pantalla_2.pack(expand = 1, fill = "y", anchor = "w")
        self.etiqueta_msg_pantalla_2 = ctk.CTkLabel(self.frame_msg_pantalla_2, text= "Mensaje de Pantalla 2 :")
        self.etiqueta_msg_pantalla_2.pack(side = "left", padx = 2, pady = 2)
        self.entry_msg_pantalla_2 = ctk.CTkTextbox(self.frame_msg_pantalla_2, wrap = ctk.WORD, width= 550, height= 100, font= ("helvetica", 15))
        self.entry_msg_pantalla_2.insert("1.0", text= f"{self.info_pantalla['msg2']}")
        self.entry_msg_pantalla_2.pack(side = "left", padx  = 2, pady = 2)
        self.frame_msg_pantalla_3 = ctk.CTkFrame(self.frame_config_pantalla) 
        self.frame_msg_pantalla_3.pack(expand = 1, fill = "y", anchor = "w")
        self.etiqueta_msg_pantalla_3 = ctk.CTkLabel(self.frame_msg_pantalla_3, text= "Mensaje de Pantalla 3 :")
        self.etiqueta_msg_pantalla_3.pack(side = "left", padx = 2, pady = 2)
        self.entry_msg_pantalla_3 = ctk.CTkTextbox(self.frame_msg_pantalla_3, wrap = ctk.WORD, width= 550, height= 100, font= ("helvetica", 15))
        self.entry_msg_pantalla_3.insert("1.0", text= f"{self.info_pantalla['msg3']}")
        self.entry_msg_pantalla_3.pack(side = "left", padx  = 2, pady = 2)
        #***(indice1, indice2) = ("linea.char"), (linea,fin de linea)***#
        #***self.captura_msg_1 = self.entry_msg_pantalla.get("1.0", "1.end")***#
        self.boton_guardar = ctk.CTkButton(self.frame_config_pantalla, width=90, height=30, text= "Guardar", command = lambda: self.guardar("pantalla"))
        self.boton_guardar.pack(side = "left", pady = 2, padx = 2)
        self.boton_cancel= ctk.CTkButton(self.frame_config_pantalla, width=90, height=30, text= "Cancelar", command= lambda: self.cancel("pantalla"))
        self.boton_cancel.pack(side = "left", pady = 2, padx = 2)      

    def menu_config_usuarios(self):
        self.frame_config_usuarios = ctk.CTkFrame(self.frame_submenu_opciones, height= 630, width= 780)
        self.lista_admin = ctk.CTkOptionMenu(self.frame_config_usuarios)
        self.lista_admin.set(value= "Administradores")
        self.lista_admin.pack(side = "left", anchor = "nw", pady = 2, padx = 2)
        self.lista_ejecutivos = ctk.CTkOptionMenu(self.frame_config_usuarios)
        self.lista_ejecutivos.set(value= "Ejecutivos")
        self.lista_ejecutivos.pack(side = "left", anchor = "nw", pady = 2, padx = 2)
        self.etiqueta_espaciadora_3 = ctk.CTkLabel(self.frame_config_usuarios, width= 800, height= (1/16), text= "")
        self.etiqueta_espaciadora_3.pack()
        self.frame_seleccion_tipo_usuario = ctk.CTkFrame(self.frame_config_usuarios, height = 40, width= 780)
        self.frame_seleccion_tipo_usuario.pack(expand = 1, fill = "x", anchor = "n", pady = 5, padx = 5)
        self.boton_nuevo_admin = ctk.CTkButton(self.frame_seleccion_tipo_usuario, width=90, height=30, text= "Administrador")
        self.boton_nuevo_admin.pack(side = "left", pady = 2, padx = 2)
        self.boton_nuevo_ejecutivo = ctk.CTkButton(self.frame_seleccion_tipo_usuario, width=90, height=30, text= "Ejecutivo")
        self.boton_nuevo_ejecutivo.pack(side = "left", pady = 2, padx = 2)
        self.boton_cancelar_nuevo_user = ctk.CTkButton(self.frame_seleccion_tipo_usuario, width=90, height=30, text= "Cancelar")
        self.boton_cancelar_nuevo_user.pack(side = "left", pady = 2, padx = 2)
        self.importar_listado_admin()

    def crear_frame_atencion(self, task, num):
        match task:
            case "nueva_atencion":
                self.frame_num_atencion = ctk.CTkFrame(self.frame_config_atenciones)
                self.frame_num_atencion.pack(expand = 1, fill = "y", anchor = "w")
                self.etiqueta_num_atencion = ctk.CTkLabel(self.frame_num_atencion, text = "Número de Atención :", width = 250)
                self.etiqueta_num_atencion.pack(side = "left", anchor = "w", padx = 2, pady = 2)
                self.entry_num_atencion = ctk.CTkEntry(self.frame_num_atencion, placeholder_text= "...")
                self.entry_num_atencion.pack(padx = 2, pady = 2)
                self.frame_nombre_atencion = ctk.CTkFrame(self.frame_config_atenciones)
                self.frame_nombre_atencion.pack(expand = 1, fill = "y", anchor = "w")
                self.etiqueta_nombre_atencion = ctk.CTkLabel(self.frame_nombre_atencion, text = "Nombre de Atención :", width = 250)
                self.etiqueta_nombre_atencion.pack(side = "left", anchor = "w", padx = 2, pady = 2)
                self.entry_nombre_atencion = ctk.CTkEntry(self.frame_nombre_atencion, placeholder_text= "...", width = 250)
                self.entry_nombre_atencion.pack(side = "left", padx = 2, pady = 2)
                self.frame_letra_atencion = ctk.CTkFrame(self.frame_config_atenciones)
                self.frame_letra_atencion.pack(expand = 1, fill = "y", anchor = "w")
                self.etiqueta_letra_atencion = ctk.CTkLabel(self.frame_letra_atencion, text = "Letra de Atención  :", width = 250,)
                self.etiqueta_letra_atencion.pack(side = "left", anchor = "w", padx = 2, pady = 2)
                self.entry_letra_atencion = ctk.CTkEntry(self.frame_letra_atencion, placeholder_text= "...", width = 250)
                self.entry_letra_atencion.pack(side = "left", padx = 2, pady = 2)
                self.boton_guardar = ctk.CTkButton(self.frame_config_atenciones, width=90, height=30, text= "Guardar", command = lambda: self.guardar("atenciones_nuevo"))
                self.boton_guardar.pack(side = "left", pady = 2, padx = 2)
                self.boton_cancel= ctk.CTkButton(self.frame_config_atenciones, width=90, height=30, text= "Cancelar", command= lambda: self.cancel("atenciones"))
                self.boton_cancel.pack(side = "left", pady = 2, padx = 2)
                self.etiqueta_numero_atencion.configure(text = "")
                self.boton_editar.configure(command = lambda: self.editar(""))
                self.boton_nuevo.configure(command = lambda: self.nuevo(""))
                self.boton_borrar.configure(command = lambda: self.borrar(""))
            case "editar_atencion":
                self.frame_num_atencion = ctk.CTkFrame(self.frame_config_atenciones)
                self.frame_num_atencion.pack(expand = 1, fill = "y", anchor = "w")
                self.etiqueta_num_atencion = ctk.CTkLabel(self.frame_num_atencion, text = "Número de Atención :", width = 250)
                self.etiqueta_num_atencion.pack(side = "left", anchor = "w", padx = 2, pady = 2)
                self.entry_num_atencion = ctk.CTkEntry(self.frame_num_atencion, placeholder_text= f"{self.listado_importar_atenciones[num][0]}")
                self.entry_num_atencion.pack(padx = 2, pady = 2)
                self.frame_nombre_atencion = ctk.CTkFrame(self.frame_config_atenciones)
                self.frame_nombre_atencion.pack(expand = 1, fill = "y", anchor = "w")
                self.etiqueta_nombre_atencion = ctk.CTkLabel(self.frame_nombre_atencion, text = "Nombre de Atención :", width = 250)
                self.etiqueta_nombre_atencion.pack(side = "left", anchor = "w", padx = 2, pady = 2)
                self.entry_nombre_atencion = ctk.CTkEntry(self.frame_nombre_atencion, placeholder_text= f"{self.listado_importar_atenciones[num][1]}", width = 250)
                self.entry_nombre_atencion.pack(side = "left", padx = 2, pady = 2)
                self.frame_letra_atencion = ctk.CTkFrame(self.frame_config_atenciones)
                self.frame_letra_atencion.pack(expand = 1, fill = "y", anchor = "w")
                self.etiqueta_letra_atencion = ctk.CTkLabel(self.frame_letra_atencion, text = "Letra de Atención  :", width = 250,)
                self.etiqueta_letra_atencion.pack(side = "left", anchor = "w", padx = 2, pady = 2)
                self.entry_letra_atencion = ctk.CTkEntry(self.frame_letra_atencion, placeholder_text= f"{self.listado_importar_atenciones[num][2]}", width = 250)
                self.entry_letra_atencion.pack(side = "left", padx = 2, pady = 2)
                self.boton_guardar = ctk.CTkButton(self.frame_config_atenciones, width=90, height=30, text= "Guardar", command = lambda: self.guardar("atenciones_editar"))
                self.boton_guardar.pack(side = "left", pady = 2, padx = 2)
                self.boton_cancel = ctk.CTkButton(self.frame_config_atenciones, width=90, height=30, text= "Cancelar", command= lambda: self.cancel("atenciones"))
                self.boton_cancel.pack(side = "left", pady = 2, padx = 2)
                self.etiqueta_numero_atencion.configure(text = "")
                self.boton_editar.configure(command = lambda: self.editar(""))
                self.boton_nuevo.configure(command = lambda: self.nuevo(""))
                self.boton_borrar.configure(command = lambda: self.borrar(""))
    def crear_frame_reglas(self):
        pass
    def cancel(self, boton):
        match boton:
            case "atenciones":
                self.frame_num_atencion.destroy()
                self.etiqueta_num_atencion.destroy()
                self.entry_num_atencion.destroy()
                self.frame_nombre_atencion.destroy()
                self.etiqueta_nombre_atencion.destroy()
                self.entry_nombre_atencion.destroy()
                self.frame_letra_atencion.destroy()
                self.etiqueta_letra_atencion.destroy()
                self.entry_letra_atencion.destroy()
                self.boton_cancel.destroy()
                self.boton_guardar.destroy()
                self.importar_listado_atenciones_db()
                self.seteo_etiqueta_numero_atencion()
                self.boton_nuevo.configure(command = lambda: self.nuevo("atenciones"))
                self.boton_editar.configure(command = lambda: self.editar("atenciones"))
                self.boton_borrar.configure(command = lambda: self.borrar("atenciones"))
            case "pantalla":
                self.frame_config_pantalla.destroy()
                self.menu_config_pantalla()
                self.frame_config_pantalla.pack(fill = "both", expand = 1, pady = 5, padx = 5)
            
    def seteo_etiqueta_numero_atencion(self):
        self.conteo_atenciones = []
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT atn_id FROM atn_table')
            db_return = cur.fetchall()
            for item in db_return:
                self.conteo_atenciones.append(item)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        self.total_atenciones = len(self.conteo_atenciones)
        self.etiqueta_numero_atencion.configure(text = f"Total atenciones: {self.total_atenciones}")

    def importar_listado_atenciones_db(self):
        ### esta función trae de la tabla atn_table lo siguiente: atn_id, atn_name y atn_letter, carga los datos a un drop menu, y me crea listas para trabajar con esos datos.
        ### atn_id : es la ID asignada a la atención.
        ### atn_name : es el nombre asignado a la atención.
        ### atn_letter : es la letra asignada a la atención.
        ### self.listado_atenciones_db : lista con las atenciones guardadas en la tabla, sin orden.
        ### self.listado_temp_orden : es una lista, ordenada, que contiene los valores de cada atención en sublistas de 3 elementos. ejemplo: self.listado_temp_orden = [[1, ATENCIÓN, A], [2, EJEMPLO, E]].
        ### self.listado_atenciones_orden_id : Es una lista, ordenada, cuyos elementos son strings con la data de cada atención. ejemlplo self.listado_atenciones_orden_id = ["1 - ATENCIÓN - A", "2 - EJEMPLO - E" ].
        self.listado_atenciones_db = []
        self.listado_temp_orden = []
        self.listado_atenciones_orden_id = []
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT atn_id, atn_name, atn_letter FROM atn_table')
            db_return = cur.fetchall()
            for id, name, letter in db_return:
                self.listado_atenciones_db.append([id, name, letter])
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            CTkMessagebox(title= "Mensaje de sistema :", message = "Error al importar la tabla de atenciones.")
            return
        finally:
            if conn is not None:
                conn.close()
        self.listado_temp_orden = self.listado_atenciones_db
        self.listado_temp_orden.sort()
        for i in range (0, len(self.listado_temp_orden)):
            self.listado_atenciones_orden_id.append(f"{self.listado_temp_orden[i][0]} - {self.listado_temp_orden[i][1]} - {self.listado_temp_orden[i][2]}")
        self.listado_atenciones.configure(values = self.listado_atenciones_orden_id)
        self.listado_atenciones.set(value = "Atenciones")
        self.seteo_etiqueta_numero_atencion()

    def importar_listado_admin(self):
        self.listado_admins_db = []
        self.listado_temp_orden_admins = []
        self.listado_admins_orden_id = []
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT id_admin, user_admin FROM admin_table')
            db_return = cur.fetchall()
            for id, name in db_return:
                self.listado_admins_db.append([id, name])
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            CTkMessagebox(title= "Mensaje de sistema :", message = "Error al importar la tabla de administradores.")
            return
        finally:
            if conn is not None:
                conn.close()
        self.listado_temp_orden_admins = self.listado_admins_db
        self.listado_temp_orden_admins.sort()
        for i in range (0, len(self.listado_temp_orden_admins)):
            self.listado_admins_orden_id.append(f"{self.listado_temp_orden_admins[i][0]} - {self.listado_temp_orden_admins[i][1]}")
        self.lista_admin.configure(values = self.listado_admins_orden_id)
        self.lista_admin.set(value = "Administradores")
    
    def importar_lista_reglas(self):
        self.tipo_reglas = {1:'Simple', 2:'Múltiple', 3:'Rebalse', 4:'Libre'}
        self.listado_reglas_db = []
        self.listado_temp_orden_reglas = []
        self.listado_reglas_orden_id = []
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute('SELECT * FROM reglas_table')
            db_return = cur.fetchall()
            for id, tipo in db_return:
                self.listado_reglas_db.append([id, self.tipo_reglas[tipo]])
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            CTkMessagebox(title= "Mensaje de sistema :", message = "Error al importar la tabla de reglas.")
            return
        finally:
            if conn is not None:
                conn.close()
        self.listado_temp_orden_reglas = self.listado_reglas_db
        self.listado_temp_orden_reglas.sort()
        for i in range (0, len(self.listado_temp_orden_reglas)):
            self.listado_reglas_orden_id.append(f"{self.listado_temp_orden_reglas[i][0]} - {self.listado_temp_orden_reglas[i][1]}")
        self.lista_reglas.configure(values = self.listado_reglas_orden_id)
        

    def filtro_id_atencion(self):
        self.atencion_seleccionada = self.listado_atenciones.get()
        self.secuencia_captura = 0
        for char in f"{self.atencion_seleccionada}":
            if char == ' ':
                break
            elif char == '':
                break
            else:
                self.secuencia_captura +=1
        if self.secuencia_captura == 1:
            self.id_atencion_captura = f"{self.atencion_seleccionada[0]}"
        elif self.secuencia_captura == 2:
            self.id_atencion_captura = f"{self.atencion_seleccionada[0]}{self.atencion_seleccionada[1]}"
        elif self.secuencia_captura == 3:
            self.id_atencion_captura = f"{self.atencion_seleccionada[0]}{self.atencion_seleccionada[1]}{self.atencion_seleccionada[2]}"
        else:
            CTkMessagebox(title= "Mensaje de sistema :", message= "Error de lectura, el ID ingresado no es válido.")
            return
        self.importar_listado_atenciones_db()
        for (id, name, letter) in self.listado_atenciones_db:
            if f"{self.id_atencion_captura}" == f"{id}":
                self.auto_id_atencion = id
                self.auto_nombre_atencion = name
                self.auto_letra_atencion = letter

App = MiTurnoX()
App.menu()
App.submenu()
App.menu_config_atenciones()
App.menu_config_reglas()
App.menu_config_pantalla()
App.menu_config_usuarios()
App.mainloop()

"""
GLOSARIO SIGNIFICADOS
tipo_regla de la tabla reglas_table
1 - Simple
2 - Multiple
3 - Rebalse
4 - Libre
"""