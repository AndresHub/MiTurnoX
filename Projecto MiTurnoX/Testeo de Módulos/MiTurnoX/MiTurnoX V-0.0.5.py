import customtkinter as ctk
import tkinter as tk
from CTkMessagebox import CTkMessagebox
from collections import deque
import socket
from _thread import *
import threading



def mostrar(evento):
    if evento == "1":
        frame_configuracion.grid(
            column = 0,
            row = 1,
            padx = 5,
            pady = 5
        )
        frame_atenciones.grid_remove()
        frame_video.grid_remove()
    elif evento == "2":
        frame_configuracion.grid_remove()
        frame_atenciones.grid(
            column = 0,
            row = 1,
            padx = 5,
            pady = 5
        )
        frame_video.grid_remove()
    else:
        frame_configuracion.grid_remove()
        frame_atenciones.grid_remove()
        frame_video.grid(
            column = 0,
            row = 1,
            padx = 5,
            pady = 5
        )


def activacion_preferencial():
    boton_submenu_config_preferencial.configure(text = estado_preferencial.get())
    if boton_submenu_config_preferencial.get() == "on":
        var_nombre_atencion_1.set("Preferencial")
        var_letra_atencion_1.set("P")
        if dropmenu_config_num_atenciones.get() != "1":
            dropmenu_config_num_atenciones.configure(values= ["2", "3", "4", "5", "6", "7", "8", "9", "10"])
        else:
            dropmenu_config_num_atenciones.set("2")
            dropmenu_config_num_atenciones.configure(values= ["2", "3", "4", "5", "6", "7", "8", "9", "10"])
    else:
        dropmenu_config_num_atenciones.configure(values= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        if var_nombre_atencion_1.get() == "Preferencial" and var_letra_atencion_1.get() == "P":
            var_nombre_atencion_1.set("")
            var_letra_atencion_1.set("")


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


def nombres_y_letras_atenciones():
    if boton_submenu_config_preferencial.get() == "on":
        label_atencion_1.grid(
            column = 0,
            row = 2,
            padx = 5,
            pady = 5
            )
        label_atencion_1_letra.grid(
            column = 2,
            row = 2,
            padx = 5,
            pady = 5
            )
        nombre_atencion_1.grid(
            column = 1,
            row = 2,
            padx = 5,
            pady = 5
            )
        letra_atencion_1.grid(
            column = 3,
            row = 2,
            padx = 5,
            pady = 5
            )
        nombre_atencion_2.focus_set()
        if dropmenu_config_num_atenciones.get() == "2":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "3":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "4":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "5":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "6":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "7":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
        elif dropmenu_config_num_atenciones.get() == "8":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_8.grid(
                column = 0,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_8_letra.grid(
                column = 2,
                row = 9,
                padx = 5,
                pady = 5
                )
            nombre_atencion_8.grid(
                column = 1,
                row = 9,
                padx = 5,
                pady = 5
                )
            letra_atencion_8.grid(
                column = 3,
                row = 9,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "9":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_8.grid(
                column = 0,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_8_letra.grid(
                column = 2,
                row = 9,
                padx = 5,
                pady = 5
                )
            nombre_atencion_8.grid(
                column = 1,
                row = 9,
                padx = 5,
                pady = 5
                )
            letra_atencion_8.grid(
                column = 3,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_9.grid(
                column = 0,
                row = 10,
                padx = 5,
                pady = 5
                )
            label_atencion_9_letra.grid(
                column = 2,
                row = 10,
                padx = 5,
                pady = 5
                )
            nombre_atencion_9.grid(
                column = 1,
                row = 10,
                padx = 5,
                pady = 5
                )
            letra_atencion_9.grid(
                column = 3,
                row = 10,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "10":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_8.grid(
                column = 0,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_8_letra.grid(
                column = 2,
                row = 9,
                padx = 5,
                pady = 5
                )
            nombre_atencion_8.grid(
                column = 1,
                row = 9,
                padx = 5,
                pady = 5
                )
            letra_atencion_8.grid(
                column = 3,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_9.grid(
                column = 0,
                row = 10,
                padx = 5,
                pady = 5
                )
            label_atencion_9_letra.grid(
                column = 2,
                row = 10,
                padx = 5,
                pady = 5
                )
            nombre_atencion_9.grid(
                column = 1,
                row = 10,
                padx = 5,
                pady = 5
                )
            letra_atencion_9.grid(
                column = 3,
                row = 10,
                padx = 5,
                pady = 5
                )
            label_atencion_10.grid(
                column = 0,
                row = 11,
                padx = 5,
                pady = 5
                )
            label_atencion_10_letra.grid(
                column = 2,
                row = 11,
                padx = 5,
                pady = 5
                )
            nombre_atencion_10.grid(
                column = 1,
                row = 11,
                padx = 5,
                pady = 5
                )
            letra_atencion_10.grid(
                column = 3,
                row = 11,
                padx = 5,
                pady = 5
                )
    elif boton_submenu_config_preferencial.get() == "off":
        nombre_atencion_1.focus_set()
        label_atencion_1.grid(
            column = 0,
            row = 2,
            padx = 5,
            pady = 5
            )
        label_atencion_1_letra.grid(
            column = 2,
            row = 2,
            padx = 5,
            pady = 5
            )
        nombre_atencion_1.grid(
            column = 1,
            row = 2,
            padx = 5,
            pady = 5
            )
        letra_atencion_1.grid(
            column = 3,
            row = 2,
            padx = 5,
            pady = 5
            )
        if dropmenu_config_num_atenciones.get() == "2":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "3":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "4":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "5":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "6":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "7":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
        elif dropmenu_config_num_atenciones.get() == "8":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_8.grid(
                column = 0,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_8_letra.grid(
                column = 2,
                row = 9,
                padx = 5,
                pady = 5
                )
            nombre_atencion_8.grid(
                column = 1,
                row = 9,
                padx = 5,
                pady = 5
                )
            letra_atencion_8.grid(
                column = 3,
                row = 9,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "9":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_8.grid(
                column = 0,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_8_letra.grid(
                column = 2,
                row = 9,
                padx = 5,
                pady = 5
                )
            nombre_atencion_8.grid(
                column = 1,
                row = 9,
                padx = 5,
                pady = 5
                )
            letra_atencion_8.grid(
                column = 3,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_9.grid(
                column = 0,
                row = 10,
                padx = 5,
                pady = 5
                )
            label_atencion_9_letra.grid(
                column = 2,
                row = 10,
                padx = 5,
                pady = 5
                )
            nombre_atencion_9.grid(
                column = 1,
                row = 10,
                padx = 5,
                pady = 5
                )
            letra_atencion_9.grid(
                column = 3,
                row = 10,
                padx = 5,
                pady = 5
                )
        elif dropmenu_config_num_atenciones.get() == "10":
            label_atencion_2.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_2_letra.grid(
                column = 2,
                row = 3,
                padx = 5,
                pady = 5
                )
            nombre_atencion_2.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            letra_atencion_2.grid(
                column = 3,
                row = 3,
                padx = 5,
                pady = 5
                )
            label_atencion_3.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_3_letra.grid(
                column = 2,
                row = 4,
                padx = 5,
                pady = 5
                )
            nombre_atencion_3.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            letra_atencion_3.grid(
                column = 3,
                row = 4,
                padx = 5,
                pady = 5
                )
            label_atencion_4.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_4_letra.grid(
                column = 2,
                row = 5,
                padx = 5,
                pady = 5
                )
            nombre_atencion_4.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            letra_atencion_4.grid(
                column = 3,
                row = 5,
                padx = 5,
                pady = 5
                )
            label_atencion_5.grid(
                column = 0,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_5_letra.grid(
                column = 2,
                row = 6,
                padx = 5,
                pady = 5
                )
            nombre_atencion_5.grid(
                column = 1,
                row = 6,
                padx = 5,
                pady = 5
                )
            letra_atencion_5.grid(
                column = 3,
                row = 6,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6_letra.grid(
                column = 2,
                row = 7,
                padx = 5,
                pady = 5
                )
            nombre_atencion_6.grid(
                column = 1,
                row = 7,
                padx = 5,
                pady = 5
                )
            letra_atencion_6.grid(
                column = 3,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_6.grid(
                column = 0,
                row = 7,
                padx = 5,
                pady = 5
                )
            label_atencion_7_letra.grid(
                column = 2,
                row = 8,
                padx = 5,
                pady = 5
                )
            nombre_atencion_7.grid(
                column = 1,
                row = 8,
                padx = 5,
                pady = 5
                )
            letra_atencion_7.grid(
                column = 3,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_7.grid(
                column = 0,
                row = 8,
                padx = 5,
                pady = 5
            )
            label_atencion_8.grid(
                column = 0,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_8_letra.grid(
                column = 2,
                row = 9,
                padx = 5,
                pady = 5
                )
            nombre_atencion_8.grid(
                column = 1,
                row = 9,
                padx = 5,
                pady = 5
                )
            letra_atencion_8.grid(
                column = 3,
                row = 9,
                padx = 5,
                pady = 5
                )
            label_atencion_9.grid(
                column = 0,
                row = 10,
                padx = 5,
                pady = 5
                )
            label_atencion_9_letra.grid(
                column = 2,
                row = 10,
                padx = 5,
                pady = 5
                )
            nombre_atencion_9.grid(
                column = 1,
                row = 10,
                padx = 5,
                pady = 5
                )
            letra_atencion_9.grid(
                column = 3,
                row = 10,
                padx = 5,
                pady = 5
                )
            label_atencion_10.grid(
                column = 0,
                row = 11,
                padx = 5,
                pady = 5
                )
            label_atencion_10_letra.grid(
                column = 2,
                row = 11,
                padx = 5,
                pady = 5
                )
            nombre_atencion_10.grid(
                column = 1,
                row = 11,
                padx = 5,
                pady = 5
                )
            letra_atencion_10.grid(
                column = 3,
                row = 11,
                padx = 5,
                pady = 5
                )
    boton_confirmar_creacion_atenciones.grid(
    column = 3,
    row = 12,
    padx = 5,
    pady = 5
    )


def borrar_y_ocultar_atenciones():
    var_nombre_atencion_1.set("")
    var_nombre_atencion_2.set("")
    var_nombre_atencion_3.set("")
    var_nombre_atencion_4.set("")
    var_nombre_atencion_5.set("")
    var_nombre_atencion_6.set("")
    var_nombre_atencion_7.set("")
    var_nombre_atencion_8.set("")
    var_nombre_atencion_9.set("")
    var_nombre_atencion_10.set("")
    var_letra_atencion_1.set("")
    var_letra_atencion_2.set("")
    var_letra_atencion_3.set("")
    var_letra_atencion_4.set("")
    var_letra_atencion_5.set("")
    var_letra_atencion_6.set("")
    var_letra_atencion_7.set("")
    var_letra_atencion_8.set("")
    var_letra_atencion_9.set("")
    var_letra_atencion_10.set("")
    label_atencion_1.grid_remove()
    label_atencion_1_letra.grid_remove()
    nombre_atencion_1.grid_remove()
    letra_atencion_1.grid_remove()
    label_atencion_2.grid_remove()
    label_atencion_2_letra.grid_remove()
    nombre_atencion_2.grid_remove()
    letra_atencion_2.grid_remove()
    label_atencion_3.grid_remove()
    label_atencion_3_letra.grid_remove()
    nombre_atencion_3.grid_remove()
    letra_atencion_3.grid_remove()
    label_atencion_4.grid_remove()
    label_atencion_4_letra.grid_remove()
    nombre_atencion_4.grid_remove()
    letra_atencion_4.grid_remove()
    label_atencion_5.grid_remove()
    label_atencion_5_letra.grid_remove()
    nombre_atencion_5.grid_remove()
    letra_atencion_5.grid_remove()
    label_atencion_6.grid_remove()
    label_atencion_6_letra.grid_remove()
    nombre_atencion_6.grid_remove()
    letra_atencion_6.grid_remove()
    label_atencion_7.grid_remove()
    label_atencion_7_letra.grid_remove()
    nombre_atencion_7.grid_remove()
    letra_atencion_7.grid_remove()
    label_atencion_8.grid_remove()
    label_atencion_8_letra.grid_remove()
    nombre_atencion_8.grid_remove()
    letra_atencion_8.grid_remove()
    label_atencion_9.grid_remove()
    label_atencion_9_letra.grid_remove()
    nombre_atencion_9.grid_remove()
    letra_atencion_9.grid_remove()
    label_atencion_10.grid_remove()
    label_atencion_10_letra.grid_remove()
    nombre_atencion_10.grid_remove()
    letra_atencion_10.grid_remove()
    estado_preferencial.set("off")
    dropmenu_config_num_atenciones.configure(values= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    dropmenu_config_num_atenciones.set("1")
    boton_confirmar_creacion_atenciones.grid_remove()


def crear_atenciones_verificadas():
    cantidad_de_atenciones_creadas = dropmenu_config_num_atenciones.get()
    match cantidad_de_atenciones_creadas:
        case "1":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
        case "2":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
        case "3":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
        case "4":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_4 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_4.get()).upper()}",
                command= lambda: llamar(4, f"{(letra_atencion_4.get()).upper()}")
                )
            boton_atencion_4.grid(
                column = 1,
                row = 2,
                padx = 5,
                pady = 5
                )
        case "5":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_4 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_4.get()).upper()}",
                command= lambda: llamar(4, f"{(letra_atencion_4.get()).upper()}")
                )
            boton_atencion_4.grid(
                column = 1,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_5 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_5.get()).upper()}",
                command= lambda: llamar(5, f"{(letra_atencion_5.get()).upper()}")
                )
            boton_atencion_5.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
        case "6":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_4 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_4.get()).upper()}",
                command= lambda: llamar(4, f"{(letra_atencion_4.get()).upper()}")
                )
            boton_atencion_4.grid(
                column = 1,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_5 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_5.get()).upper()}",
                command= lambda: llamar(5, f"{(letra_atencion_5.get()).upper()}")
                )
            boton_atencion_5.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_6 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_6.get()).upper()}",
                command= lambda: llamar(6, f"{(letra_atencion_6.get()).upper()}")
                )
            boton_atencion_6.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
        case "7":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_4 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_4.get()).upper()}",
                command= lambda: llamar(4, f"{(letra_atencion_4.get()).upper()}")
                )
            boton_atencion_4.grid(
                column = 1,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_5 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_5.get()).upper()}",
                command= lambda: llamar(5, f"{(letra_atencion_5.get()).upper()}")
                )
            boton_atencion_5.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_6 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_6.get()).upper()}",
                command= lambda: llamar(6, f"{(letra_atencion_6.get()).upper()}")
                )
            boton_atencion_6.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_7 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_7.get()).upper()}",
                command= lambda: llamar(7, f"{(letra_atencion_7.get()).upper()}")
                )
            boton_atencion_7.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
        case "8":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_4 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_4.get()).upper()}",
                command= lambda: llamar(4, f"{(letra_atencion_4.get()).upper()}")
                )
            boton_atencion_4.grid(
                column = 1,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_5 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_5.get()).upper()}",
                command= lambda: llamar(5, f"{(letra_atencion_5.get()).upper()}")
                )
            boton_atencion_5.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_6 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_6.get()).upper()}",
                command= lambda: llamar(6, f"{(letra_atencion_6.get()).upper()}")
                )
            boton_atencion_6.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_7 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_7.get()).upper()}",
                command= lambda: llamar(7, f"{(letra_atencion_7.get()).upper()}")
                )
            boton_atencion_7.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            boton_atencion_8 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_8.get()).upper()}",
                command= lambda: llamar(8, f"{(letra_atencion_8.get()).upper()}")
                )
            boton_atencion_8.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
        case "9":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_4 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_4.get()).upper()}",
                command= lambda: llamar(4, f"{(letra_atencion_4.get()).upper()}")
                )
            boton_atencion_4.grid(
                column = 1,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_5 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_5.get()).upper()}",
                command= lambda: llamar(5, f"{(letra_atencion_5.get()).upper()}")
                )
            boton_atencion_5.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_6 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_6.get()).upper()}",
                command= lambda: llamar(6, f"{(letra_atencion_6.get()).upper()}")
                )
            boton_atencion_6.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_7 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_7.get()).upper()}",
                command= lambda: llamar(7, f"{(letra_atencion_7.get()).upper()}")
                )
            boton_atencion_7.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            boton_atencion_8 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_8.get()).upper()}",
                command= lambda: llamar(8, f"{(letra_atencion_8.get()).upper()}")
                )
            boton_atencion_8.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            boton_atencion_9 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_9.get()).upper()}",
                command= lambda: llamar(9, f"{(letra_atencion_9.get()).upper()}")
                )
            boton_atencion_9.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
        case "10":
            boton_atencion_1 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_1.get()).upper()}",
                command= lambda: llamar(1, f"{(letra_atencion_1.get()).upper()}")
                )
            boton_atencion_1.grid(
                column = 0,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_2 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_2.get()).upper()}",
                command= lambda: llamar(2, f"{(letra_atencion_2.get()).upper()}")
                )
            boton_atencion_2.grid(
                column = 1,
                row = 1,
                padx = 5,
                pady = 5
                )
            boton_atencion_3 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_3.get()).upper()}",
                command= lambda: llamar(3, f"{(letra_atencion_3.get()).upper()}")
                )
            boton_atencion_3.grid(
                column = 0,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_4 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_4.get()).upper()}",
                command= lambda: llamar(4, f"{(letra_atencion_4.get()).upper()}")
                )
            boton_atencion_4.grid(
                column = 1,
                row = 2,
                padx = 5,
                pady = 5
                )
            boton_atencion_5 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_5.get()).upper()}",
                command= lambda: llamar(5, f"{(letra_atencion_5.get()).upper()}")
                )
            boton_atencion_5.grid(
                column = 0,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_6 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_6.get()).upper()}",
                command= lambda: llamar(6, f"{(letra_atencion_6.get()).upper()}")
                )
            boton_atencion_6.grid(
                column = 1,
                row = 3,
                padx = 5,
                pady = 5
                )
            boton_atencion_7 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_7.get()).upper()}",
                command= lambda: llamar(7, f"{(letra_atencion_7.get()).upper()}")
                )
            boton_atencion_7.grid(
                column = 0,
                row = 4,
                padx = 5,
                pady = 5
                )
            boton_atencion_8 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_8.get()).upper()}",
                command= lambda: llamar(8, f"{(letra_atencion_8.get()).upper()}")
                )
            boton_atencion_8.grid(
                column = 1,
                row = 4,
                padx = 5,
                pady = 5
                )
            boton_atencion_9 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_9.get()).upper()}",
                command= lambda: llamar(9, f"{(letra_atencion_9.get()).upper()}")
                )
            boton_atencion_9.grid(
                column = 0,
                row = 5,
                padx = 5,
                pady = 5
                )
            boton_atencion_10 = ctk.CTkButton(
                frame_botones_atencion,
                text=f"{(nombre_atencion_10.get()).upper()}",
                command= lambda: llamar(10, f"{(letra_atencion_10.get()).upper()}")
                )
            boton_atencion_10.grid(
                column = 1,
                row = 5,
                padx = 5,
                pady = 5
                )
            

    CTkMessagebox(title= "Creación de atenciones", message= "Atenciones creadas con éxito")
    return


###VERIFICA QUE: 1-LETRAS Y NOMBRES NO SE REPITAN, 2-QUE SOLO SEA UN CARACTER POR LETRA, 3- QUE NO QUEDEN CAMPOS VACÍOS
def verificar_nombres_y_letras():
    ##CREO LISTAS PARA ABSORVER LOS ELEMENTOS DE CADA CAMPO LLENADO
    listado_nombres = []
    listado_letras = []
    listado_nombres_upper = []
    listado_letras_upper = []
    #TRAIGO LA CANTIDAD DE ATENCIONES SELECCIONADAS PARA SEPARAR POR CASOS LA VERIFICACIÓN
    cantidad_de_atenciones_creadas = dropmenu_config_num_atenciones.get()
    #DE ACUERDO AL CASO REVISO LOS CAMPOS QUE DEBEN ESTAR LLENOS, Y EVITO ERRORES POR CAMPOS VACÍOS INVISIBLES
    match cantidad_de_atenciones_creadas:
        case "1":
            if len(var_letra_atencion_1.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "2":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "3":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "4":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1 or len(var_letra_atencion_4.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1 or len(var_letra_atencion_4.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1 or len(var_nombre_atencion_4.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            listado_nombres.append(var_nombre_atencion_4.get())
            listado_letras.append(var_letra_atencion_4.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "5":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1 or len(var_letra_atencion_4.get()) > 1 or len(var_letra_atencion_5.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1 or len(var_letra_atencion_4.get()) < 1 or len(var_letra_atencion_5.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1 or len(var_nombre_atencion_4.get()) < 1 or len(var_nombre_atencion_5.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            listado_nombres.append(var_nombre_atencion_4.get())
            listado_letras.append(var_letra_atencion_4.get())
            listado_nombres.append(var_nombre_atencion_5.get())
            listado_letras.append(var_letra_atencion_5.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "6":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1 or len(var_letra_atencion_4.get()) > 1 or len(var_letra_atencion_5.get()) > 1 or len(var_letra_atencion_6.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1 or len(var_letra_atencion_4.get()) < 1 or len(var_letra_atencion_5.get()) < 1 or len(var_letra_atencion_6.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1 or len(var_nombre_atencion_4.get()) < 1 or len(var_nombre_atencion_5.get()) < 1 or len(var_nombre_atencion_6.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            listado_nombres.append(var_nombre_atencion_4.get())
            listado_letras.append(var_letra_atencion_4.get())
            listado_nombres.append(var_nombre_atencion_5.get())
            listado_letras.append(var_letra_atencion_5.get())
            listado_nombres.append(var_nombre_atencion_6.get())
            listado_letras.append(var_letra_atencion_6.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "7":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1 or len(var_letra_atencion_4.get()) > 1 or len(var_letra_atencion_5.get()) > 1 or len(var_letra_atencion_6.get()) > 1 or len(var_letra_atencion_7.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1 or len(var_letra_atencion_4.get()) < 1 or len(var_letra_atencion_5.get()) < 1 or len(var_letra_atencion_6.get()) < 1 or len(var_letra_atencion_7.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1 or len(var_nombre_atencion_4.get()) < 1 or len(var_nombre_atencion_5.get()) < 1 or len(var_nombre_atencion_6.get()) < 1 or len(var_nombre_atencion_7.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            listado_nombres.append(var_nombre_atencion_4.get())
            listado_letras.append(var_letra_atencion_4.get())
            listado_nombres.append(var_nombre_atencion_5.get())
            listado_letras.append(var_letra_atencion_5.get())
            listado_nombres.append(var_nombre_atencion_6.get())
            listado_letras.append(var_letra_atencion_6.get())
            listado_nombres.append(var_nombre_atencion_7.get())
            listado_letras.append(var_letra_atencion_7.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "8":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1 or len(var_letra_atencion_4.get()) > 1 or len(var_letra_atencion_5.get()) > 1 or len(var_letra_atencion_6.get()) > 1 or len(var_letra_atencion_7.get()) > 1 or len(var_letra_atencion_8.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1 or len(var_letra_atencion_4.get()) < 1 or len(var_letra_atencion_5.get()) < 1 or len(var_letra_atencion_6.get()) < 1 or len(var_letra_atencion_7.get()) < 1 or len(var_letra_atencion_8.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1 or len(var_nombre_atencion_4.get()) < 1 or len(var_nombre_atencion_5.get()) < 1 or len(var_nombre_atencion_6.get()) < 1 or len(var_nombre_atencion_7.get()) < 1 or len(var_nombre_atencion_8.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            listado_nombres.append(var_nombre_atencion_4.get())
            listado_letras.append(var_letra_atencion_4.get())
            listado_nombres.append(var_nombre_atencion_5.get())
            listado_letras.append(var_letra_atencion_5.get())
            listado_nombres.append(var_nombre_atencion_6.get())
            listado_letras.append(var_letra_atencion_6.get())
            listado_nombres.append(var_nombre_atencion_7.get())
            listado_letras.append(var_letra_atencion_7.get())
            listado_nombres.append(var_nombre_atencion_8.get())
            listado_letras.append(var_letra_atencion_8.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "9":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1 or len(var_letra_atencion_4.get()) > 1 or len(var_letra_atencion_5.get()) > 1 or len(var_letra_atencion_6.get()) > 1 or len(var_letra_atencion_7.get()) > 1 or len(var_letra_atencion_8.get()) > 1 or len(var_letra_atencion_9.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1 or len(var_letra_atencion_4.get()) < 1 or len(var_letra_atencion_5.get()) < 1 or len(var_letra_atencion_6.get()) < 1 or len(var_letra_atencion_7.get()) < 1 or len(var_letra_atencion_8.get()) < 1 or len(var_letra_atencion_9.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1 or len(var_nombre_atencion_4.get()) < 1 or len(var_nombre_atencion_5.get()) < 1 or len(var_nombre_atencion_6.get()) < 1 or len(var_nombre_atencion_7.get()) < 1 or len(var_nombre_atencion_8.get()) < 1 or len(var_nombre_atencion_9.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            listado_nombres.append(var_nombre_atencion_4.get())
            listado_letras.append(var_letra_atencion_4.get())
            listado_nombres.append(var_nombre_atencion_5.get())
            listado_letras.append(var_letra_atencion_5.get())
            listado_nombres.append(var_nombre_atencion_6.get())
            listado_letras.append(var_letra_atencion_6.get())
            listado_nombres.append(var_nombre_atencion_7.get())
            listado_letras.append(var_letra_atencion_7.get())
            listado_nombres.append(var_nombre_atencion_8.get())
            listado_letras.append(var_letra_atencion_8.get())
            listado_nombres.append(var_nombre_atencion_9.get())
            listado_letras.append(var_letra_atencion_9.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
        case "10":
            if len(var_letra_atencion_1.get()) > 1 or len(var_letra_atencion_2.get()) > 1 or len(var_letra_atencion_3.get()) > 1 or len(var_letra_atencion_4.get()) > 1 or len(var_letra_atencion_5.get()) > 1 or len(var_letra_atencion_6.get()) > 1 or len(var_letra_atencion_7.get()) > 1 or len(var_letra_atencion_8.get()) > 1 or len(var_letra_atencion_9.get()) > 1 or len(var_letra_atencion_10.get()) > 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un solo caracter en el campo de letra")
                return
            if len(var_letra_atencion_1.get()) < 1 or len(var_letra_atencion_2.get()) < 1 or len(var_letra_atencion_3.get()) < 1 or len(var_letra_atencion_4.get()) < 1 or len(var_letra_atencion_5.get()) < 1 or len(var_letra_atencion_6.get()) < 1 or len(var_letra_atencion_7.get()) < 1 or len(var_letra_atencion_8.get()) < 1 or len(var_letra_atencion_9.get()) < 1 or len(var_letra_atencion_10.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Letra", message= "Ingrese un caracter en el campo de letra")
                return
            if len(var_nombre_atencion_1.get()) < 1 or len(var_nombre_atencion_2.get()) < 1 or len(var_nombre_atencion_3.get()) < 1 or len(var_nombre_atencion_4.get()) < 1 or len(var_nombre_atencion_5.get()) < 1 or len(var_nombre_atencion_6.get()) < 1 or len(var_nombre_atencion_7.get()) < 1 or len(var_nombre_atencion_8.get()) < 1 or len(var_nombre_atencion_9.get()) < 1 or len(var_nombre_atencion_10.get()) < 1:
                CTkMessagebox(title= "Error en Campo de Nombre", message= "Ingrese un nombre de atención en el campo de nombre")
                return
            listado_nombres.append(var_nombre_atencion_1.get())
            listado_letras.append(var_letra_atencion_1.get())
            listado_nombres.append(var_nombre_atencion_2.get())
            listado_letras.append(var_letra_atencion_2.get())
            listado_nombres.append(var_nombre_atencion_3.get())
            listado_letras.append(var_letra_atencion_3.get())
            listado_nombres.append(var_nombre_atencion_4.get())
            listado_letras.append(var_letra_atencion_4.get())
            listado_nombres.append(var_nombre_atencion_5.get())
            listado_letras.append(var_letra_atencion_5.get())
            listado_nombres.append(var_nombre_atencion_6.get())
            listado_letras.append(var_letra_atencion_6.get())
            listado_nombres.append(var_nombre_atencion_7.get())
            listado_letras.append(var_letra_atencion_7.get())
            listado_nombres.append(var_nombre_atencion_8.get())
            listado_letras.append(var_letra_atencion_8.get())
            listado_nombres.append(var_nombre_atencion_9.get())
            listado_letras.append(var_letra_atencion_9.get())
            listado_nombres.append(var_nombre_atencion_10.get())
            listado_letras.append(var_letra_atencion_10.get())
            for x in listado_nombres:
                listado_nombres_upper.append(x.upper())
            for x in listado_letras:
                listado_letras_upper.append(x.upper())
            listado_set_nombres = set(listado_nombres_upper)
            listado_set_letras = set(listado_letras_upper)
            if len(listado_set_nombres) != len(listado_nombres_upper) or len(listado_set_letras) != len(listado_letras_upper):
                CTkMessagebox(title= "Error de duplicación", message= "No repetir Nombres o letras")
                return
    crear_atenciones_verificadas()
            

def llamar(num, letra):
    
    global queue_contador_1
    global queue_contador_2
    if num == 1:
        if queue_contador_1[0] == "" and contador_1.get() == "000":
            queue_contador_1.append(0)
            contador_1 = 0
            contador_atencion_1.configure(text = f"{contador_1}" )
            letra_contador_1.configure(text = f"{letra}")
        else:
            contador_1 = queue_contador_1[-1] + 1
            queue_contador_1.append(contador_1)
            contador_atencion_1.configure(text = f"{contador_1}" )
            letra_contador_1.configure(text = f"{letra}")
    elif num == 2:
        if queue_contador_2[0] == "" and contador_2.get() == "000":
            queue_contador_2.append(0)
            contador_2 = 0
            contador_atencion_2.configure(text = f"{contador_2}" )
            letra_contador_2.configure(text = f"{letra}")
        else:
            contador_2 = queue_contador_2[-1] + 1
            queue_contador_2.append(contador_2)
            contador_atencion_2.configure(text = f"{contador_2}" )
            letra_contador_2.configure(text = f"{letra}")
    elif num == 3:
        if queue_contador_3[0] == "" and contador_3.get() == "000":
            queue_contador_3.append(0)
            contador_3 = 0
            contador_atencion_3.configure(text = f"{contador_3}" )
            letra_contador_3.configure(text = f"{letra}")
        else:
            contador_3 = queue_contador_3[-1] + 1
            queue_contador_3.append(contador_3)
            contador_atencion_3.configure(text = f"{contador_3}" )
            letra_contador_3.configure(text = f"{letra}")
    elif num == 4:
        if queue_contador_4[0] == "" and contador_4.get() == "000":
            queue_contador_4.append(0)
            contador_4 = 0
            contador_atencion_4.configure(text = f"{contador_4}" )
            letra_contador_4.configure(text = f"{letra}")
        else:
            contador_4 = queue_contador_4[-1] + 1
            queue_contador_4.append(contador_4)
            contador_atencion_4.configure(text = f"{contador_4}" )
            letra_contador_4.configure(text = f"{letra}")
    elif num == 5:
        if queue_contador_5[0] == "" and contador_5.get() == "000":
            queue_contador_5.append(0)
            contador_5 = 0
            contador_atencion_5.configure(text = f"{contador_5}" )
            letra_contador_5.configure(text = f"{letra}")
        else:
            contador_5 = queue_contador_5[-1] + 1
            queue_contador_5.append(contador_5)
            contador_atencion_5.configure(text = f"{contador_5}" )
            letra_contador_5.configure(text = f"{letra}")
    elif num == 6:
        if queue_contador_6[0] == "" and contador_6.get() == "000":
            queue_contador_6.append(0)
            contador_6 = 0
            contador_atencion_6.configure(text = f"{contador_6}" )
            letra_contador_6.configure(text = f"{letra}")
        else:
            contador_6 = queue_contador_6[-1] + 1
            queue_contador_6.append(contador_6)
            contador_atencion_6.configure(text = f"{contador_6}" )
            letra_contador_6.configure(text = f"{letra}")
    elif num == 7:
        if queue_contador_7[0] == "" and contador_7.get() == "000":
            queue_contador_7.append(0)
            contador_7 = 0
            contador_atencion_7.configure(text = f"{contador_7}" )
            letra_contador_7.configure(text = f"{letra}")
        else:
            contador_7 = queue_contador_7[-1] + 1
            queue_contador_7.append(contador_7)
            contador_atencion_7.configure(text = f"{contador_7}" )
            letra_contador_7.configure(text = f"{letra}")
    elif num == 8:
        if queue_contador_8[0] == "" and contador_8.get() == "000":
            queue_contador_8.append(0)
            contador_8 = 0
            contador_atencion_8.configure(text = f"{contador_8}" )
            letra_contador_8.configure(text = f"{letra}")
        else:
            contador_8 = queue_contador_8[-1] + 1
            queue_contador_8.append(contador_8)
            contador_atencion_8.configure(text = f"{contador_8}" )
            letra_contador_8.configure(text = f"{letra}")
    elif num == 9:
        if queue_contador_9[0] == "" and contador_9.get() == "000":
            queue_contador_9.append(0)
            contador_9 = 0
            contador_atencion_9.configure(text = f"{contador_9}" )
            letra_contador_9.configure(text = f"{letra}")
        else:
            contador_9 = queue_contador_9[-1] + 1
            queue_contador_9.append(contador_9)
            contador_atencion_9.configure(text = f"{contador_9}" )
            letra_contador_9.configure(text = f"{letra}")
    elif num == 10:
        if queue_contador_10[0] == "" and contador_10.get() == "000":
            queue_contador_10.append(0)
            contador_10 = 0
            contador_atencion_10.configure(text = f"{contador_10}" )
            letra_contador_10.configure(text = f"{letra}")
        else:
            contador_10 = queue_contador_10[-1] + 1
            queue_contador_10.append(contador_10)
            contador_atencion_10.configure(text = f"{contador_10}" )
            letra_contador_10.configure(text = f"{letra}")


"""
def procesar_data(data):
    # This is a placeholder function; you can replace it with your own logic
    print(f"Processing data: {data['message']}")
    # Extract additional parameters
    if 'task' in data:
        print(f"Task: {data['task']}")



###MANEJO DE LAS DIFERENTES CONEXIONES DE CLIENTES
def manejar_cliente(socket_cliente):
    ###LOOP HASTA DEJAR DE RECIBIR DATA
    while True:
        ### LÍMITE DE DATA QUE PUEDO RECIBIR DEL CLIENTE 1024 bytes
        data = socket_cliente.recv(1024)
        ###SI DIJA DE RECIBIR DATA, HACE UN BREAK
        if not data:
            ##SI NO RECIBE DATA ES XQ EL CLIENTE SE DESCONECTÓ
            break
        ###DECODIFICACIÓN DE LA DATA RECIBIDA COMO JSON
        data_decodificada = data.decode('utf-8')
        ###CONVIERTO EL STRING JSON A UN DICCIONARIO DE PYTHON
        ###BUSCAR UNA LIBRERIA DE JSON QUE HAGA MEJOR EL TRABAJO
        diccionario_data = eval(data_decodificada)
        ###PASO LA DATA A UNA FUNCIÓN PARA MANIPULARLA
        procesar_data(diccionario_data)
        ###RESPONDO AL CLIENTE POR LA DATA RECIBIDA
        socket_cliente.send("RECIVIDO".encode('utf-8'))
    ###CIERRO LA CONEXIÓN CON EL CLIENTE CUANDO TERMINA EL LOOP
    socket_cliente.close()



def iniciar_servidor():
    ###CREO UN SOCKET CON IPV4 (AF_INET), Y TCP/IP (SOCK_STREAM)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ##VINCULO EL SOCKET A UN IP Y UN PUERTO ESPECÍFICOS
    servidor.bind(('0.0.0.0', 8888))
    ###COLOCO EL SERVER EN ESCUCHA, Y LE DETERMINO EL MÁXIMO DE CONEXIONES QUE ESPERO
    servidor.listen(10)
    ###ME ASEGURO QUE FUNCIONE HACIENDO UN PRINT, DEBO REEMPLAZAR ESTO POR MÉTODOS MÁS SEGUROS COMO "TRY"
    print("[*] Listening on 0.0.0.0:8888")
    ###INICIO UN LOOP INFINITO DE CONEXIÓN
    while True:
        ##ACEPTO CONEXIÓN DE LOS CLIENTES
        cliente, dir = servidor.accept()
        ###PRINT PARA REVISAR ÉXITO, REEMPLAZAR CON TRY Y MSGBOX O ATRAPAR ERRORES
        print(f"[*] Accepted connection from: {dir[0]}:{dir[1]}")

        ##CREO UN NUEVO HILO PARA MANEJAR LA COMUNICACIÓN DEL CLIENTE
        manejo_cliente = threading.Thread(target=manejar_cliente, args=(cliente,))
        manejo_cliente.start()      
"""

def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print_lock.release()
            break
        data = data[::-1]
        c.send(data)
    c.close()

def server_on():
    host = ""
    port = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded a", port)
    s.listen(5)
    print("socket escuchando")
    while True:
        c, addr = s.accept()
        print_lock.acquire()
        print("conectado a", addr[0], " ", addr[1])
        start_new_thread(threaded, (c,))
    s.close()

def server_thread():
    print_lock1.acquire()
    hilo_server = threading.Thread(target=server_on)
    hilo_server.start()
    


#ventana principal
app = ctk.CTk()
#seteo de modo oscuro
ctk.set_appearance_mode("dark")
#seteo de títutlo de ventana principal
app.title("Mi Turno X v0.0.4")
#mostrar ventana maximizada
app.after(
    0, 
    lambda: app.wm_state('zoomed')
    )

###VARIABLES
##VARIABLE ESTADO PREFERENCIAL
estado_preferencial = tk.StringVar(value="off")
print_lock = threading.Lock()
print_lock1 = threading.Lock()
##VARIABLES NOMBRE DE ATENCIONES
var_nombre_atencion_1 = ctk.StringVar(app, "")
var_nombre_atencion_2 = ctk.StringVar(app, "")
var_nombre_atencion_3 = ctk.StringVar(app, "")
var_nombre_atencion_4 = ctk.StringVar(app, "")
var_nombre_atencion_5 = ctk.StringVar(app, "")
var_nombre_atencion_6 = ctk.StringVar(app, "")
var_nombre_atencion_7 = ctk.StringVar(app, "")
var_nombre_atencion_8 = ctk.StringVar(app, "")
var_nombre_atencion_9 = ctk.StringVar(app, "")
var_nombre_atencion_10 = ctk.StringVar(app, "")
##VARIABLES LETRA DE ATENCONES
var_letra_atencion_1 = ctk.StringVar(app, "")
var_letra_atencion_2 = ctk.StringVar(app, "")
var_letra_atencion_3 = ctk.StringVar(app, "")
var_letra_atencion_4 = ctk.StringVar(app, "")
var_letra_atencion_5 = ctk.StringVar(app, "")
var_letra_atencion_6 = ctk.StringVar(app, "")
var_letra_atencion_7 = ctk.StringVar(app, "")
var_letra_atencion_8 = ctk.StringVar(app, "")
var_letra_atencion_9 = ctk.StringVar(app, "")
var_letra_atencion_10 = ctk.StringVar(app, "")
##VARIABLES LISTAS EN ESPERA
contador_1 = ctk.StringVar(app, "000")
queue_contador_1 = deque([0])
contador_2 = ctk.StringVar(app, "000")
queue_contador_2 = deque([0])
contador_3 = ctk.StringVar(app, "000")
queue_contador_3 = deque([0])
contador_4 = ctk.StringVar(app, "000")
queue_contador_4 = deque([0])
contador_5 = ctk.StringVar(app, "000")
queue_contador_5 = deque([0])
contador_6 = ctk.StringVar(app, "000")
queue_contador_6 = deque([0])
contador_7 = ctk.StringVar(app, "000")
queue_contador_7 = deque([0])
contador_8 = ctk.StringVar(app, "000")
queue_contador_8 = deque([0])
contador_9 = ctk.StringVar(app, "000")
queue_contador_9 = deque([0])
contador_10 = ctk.StringVar(app, "000")
queue_contador_10 = deque([0])
###FRAMES

###FRAME BOTONES MENÚ PRINCIPAL
menu_principal = ctk.CTkFrame(
    app,
    height= 50
    )
menu_principal.grid(
    column = 0,
    row = 0,
    padx = 5,
    pady = 5
    )

###BOTONES DEL MENÚ PRINCIPAL

#BOTÓN CONFIGURACIÓN DEL MENÚ PRINCIPAL
boton_configuracion = ctk.CTkButton(
    menu_principal, text="Configuración",
    command= lambda: mostrar("1"),
    font=("verdana", 15)
    )
boton_configuracion.grid(
    column = 0,
    row = 0,
    padx = 5,
    pady = 5
    )

#BOTÓN ATENCIONES DEL MENÚ PRINCIPAL
boton_atenciones = ctk.CTkButton(
    menu_principal, text="Atenciones",
    command= lambda: mostrar("2"),
    font=("verdana", 15)
    )
boton_atenciones.grid(
    column = 2,
    row = 0,
    padx = 5,
    pady = 5
    )

#BOTÓN VIDEO DEL MENÚ PRINCIPAL
boton_video = ctk.CTkButton(
    menu_principal, text="Video",
    command= lambda: mostrar("3"),
    font=("verdana", 15)
    )
boton_video.grid(
    column = 3,
    row = 0,
    padx = 5,
    pady = 5
    )

##FRAME DE CONFIGURACION
frame_configuracion = ctk.CTkFrame(app)

#ETIQUETA DE TÍTULO DEL MENÚ CONFIGURACIÓN
label_configuracion = ctk.CTkLabel(
    frame_configuracion,
    text="Configuración",
    font=("verdana", 18)
    )
label_configuracion.grid(
    column = 0,
    row = 1
    )

##FRAME DE ATENCIONES
frame_atenciones = ctk.CTkFrame(app)

##FRAME CON BOTONES
frame_botones_atencion = ctk.CTkFrame(
    frame_atenciones
    )
frame_botones_atencion.grid(
    column = 0,
    row = 1,
    padx = 5,
    pady = 5
    )
##FRAME CON CONTADORES
frame_contadores_atencion = ctk.CTkFrame(
    frame_atenciones
    )
frame_contadores_atencion.grid(
    column = 1,
    row = 1,
    padx = 5,
    pady = 5
    )
##ETIQUETAS CONTADORES ATENCIONES
contador_atencion_1 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_1.grid(
    column = 0,
    row = 0,
    padx = 5,
    pady = 5
    )
contador_atencion_2 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_2.grid(
    column = 0,
    row = 1,
    padx = 5,
    pady = 5
    )
letra_contador_1 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_1.grid(
    column = 1,
    row = 0,
    padx = 5,
    pady = 5
    )
letra_contador_2 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_2.grid(
    column = 1,
    row = 1,
    padx = 5,
    pady = 5
    )
contador_atencion_3 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_3.grid(
    column = 0,
    row = 2,
    padx = 5,
    pady = 5
    )
letra_contador_3 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_3.grid(
    column = 1,
    row = 2,
    padx = 5,
    pady = 5
    )
contador_atencion_4 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_4.grid(
    column = 0,
    row = 3,
    padx = 5,
    pady = 5
    )
letra_contador_4 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_4.grid(
    column = 1,
    row = 3,
    padx = 5,
    pady = 5
    )
contador_atencion_5 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_5.grid(
    column = 0,
    row = 4,
    padx = 5,
    pady = 5
    )
letra_contador_5 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_5.grid(
    column = 1,
    row = 4,
    padx = 5,
    pady = 5
    )
contador_atencion_6 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_6.grid(
    column = 0,
    row = 5,
    padx = 5,
    pady = 5
    )
letra_contador_6 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_6.grid(
    column = 1,
    row = 5,
    padx = 5,
    pady = 5
    )
contador_atencion_7 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_7.grid(
    column = 0,
    row = 6,
    padx = 5,
    pady = 5
    )
letra_contador_7 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_7.grid(
    column = 1,
    row = 6,
    padx = 5,
    pady = 5
    )
contador_atencion_8 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_8.grid(
    column = 0,
    row = 7,
    padx = 5,
    pady = 5
    )
letra_contador_8 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_8.grid(
    column = 1,
    row = 7,
    padx = 5,
    pady = 5
    )
contador_atencion_9 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_9.grid(
    column = 0,
    row = 8,
    padx = 5,
    pady = 5
    )
letra_contador_9 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_9.grid(
    column = 1,
    row = 8,
    padx = 5,
    pady = 5
    )
contador_atencion_10 = ctk.CTkLabel(
    frame_contadores_atencion,
    font= ("verdana", 30, "bold"),
    text="000",
    width= 100
    )
contador_atencion_10.grid(
    column = 0,
    row = 9,
    padx = 5,
    pady = 5
    )
letra_contador_10 = ctk.CTkLabel(
    frame_contadores_atencion,
    text = "X",
    font= ("verdana", 30, "bold")
    )
letra_contador_10.grid(
    column = 1,
    row = 9,
    padx = 5,
    pady = 5
    )


#ETIQUETA DE TÍTULO MENÚ ATENCIONES
label_atenciones = ctk.CTkLabel(
    frame_atenciones,
    text="Atenciones",
    font=("verdana", 18)
    )
label_atenciones.grid(
    column = 1,
    row = 0,
    padx = 5,
    pady = 5
    )

##FRAME DE VIDEO
frame_video = ctk.CTkFrame(app)

#ETIQUETA DE TÍTULO MENÚ VIDEO
label_video = ctk.CTkLabel(
    frame_video,
    text="Video",
    font=("verdana", 18)
    )
label_video.grid(
    column = 0,
    row = 1,
    padx = 5,
    pady = 5
    )

##FRAME CON BOTONES DE CONFIGURACIÓN
frame_submenu_configuracion = ctk.CTkFrame(frame_configuracion)
frame_submenu_configuracion.grid(
    column = 0,
    row = 2,
    padx = 5,
    pady = 5
    )

###BOTONES DEL MENÚ CONFIGURACIÓN

#BOTÓN CONFIGURAR ATENCIONES
boton_submenu_config_atenciones = ctk.CTkButton(
    frame_submenu_configuracion,
    text= "Configurar Atenciones",
    command = lambda: mostrar_frame_submenu_config("1")
    )
boton_submenu_config_atenciones.grid(
    column = 0,
    row = 0,
    padx = 5,
    pady = 5
    )

#BOTÓN CONFIGURAR SERVIDOR
boton_submenu_config_server = ctk.CTkButton(
    frame_submenu_configuracion,
    text= "Configurar Server",
    command = lambda: mostrar_frame_submenu_config("2")
    )
boton_submenu_config_server.grid(
    column = 1,
    row = 0,
    padx = 5,
    pady = 5
    )
#BOTON CONFIGURAR VIDEO
boton_submenu_config_video = ctk.CTkButton(
    frame_submenu_configuracion,
    text= "Configurar Video",
    command = lambda: mostrar_frame_submenu_config("3")
    )
boton_submenu_config_video.grid(
    column = 2,
    row = 0,
    padx = 5,
    pady = 5
    )


#FRAME CONFIGURACIÓN DE ATENCIONES
frame_submenu_configuracion_atenciones = ctk.CTkFrame(frame_configuracion)



###ETIQUETAS CONFIGURACIÓN DE ATENCIONES

##ETIQUETA DE PREFERENCIAL
label_submenu_config_preferencial = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text= "Preferencial", anchor= "w",
    width= 150
    )
label_submenu_config_preferencial.grid(
    column = 0,
    row = 0,
    padx = 5,
    pady = 5
    )
##ETIQUETA DE CANTIDAD DE ATENCIONES DESEADAS
label_submenu_config_num_atenciones = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text= "Cantidad de Atenciones",
    anchor="w",
    width= 150
    )
label_submenu_config_num_atenciones.grid(
    column = 0,
    row = 1,
    padx = 5,
    pady = 5
    )

#ETIQUETAS DEFINIR NOMBRE DE ATENCIONES

#NOMBRE ATENCIONES 1 al 10
label_atencion_1 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 1:"
    )
label_atencion_2 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 2:"
    )
label_atencion_3 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 3:"
    )
label_atencion_4 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 4:"
    )
label_atencion_5 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 5:"
    )
label_atencion_6 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 6:"
    )
label_atencion_7 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 7:"
    )
label_atencion_8 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 8:"
    )
label_atencion_9 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 9:"
    )
label_atencion_10 = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Atención 10:"
    )

#LETRA ATENCIONES 1 al 10
label_atencion_1_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_2_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_3_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_4_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_5_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_6_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_7_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_8_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_9_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )
label_atencion_10_letra = ctk.CTkLabel(
    frame_submenu_configuracion_atenciones,
    text="Letra:"
    )

###ENTRYS NOMBRE DE ATENCIONES
nombre_atencion_1 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_1
)
nombre_atencion_2 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_2
)
nombre_atencion_3 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_3
)
nombre_atencion_4 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_4
)
nombre_atencion_5 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_5
)
nombre_atencion_6 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_6
)
nombre_atencion_7 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_7
)
nombre_atencion_8 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_8
)
nombre_atencion_9 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_9
)
nombre_atencion_10 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Nombre",
    textvariable = var_nombre_atencion_10
)

###ENTRYS LETRA DE ATENCIONES
letra_atencion_1 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_1
)
letra_atencion_2 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_2
)
letra_atencion_3 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_3
)
letra_atencion_4 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_4
)
letra_atencion_5 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_5
)
letra_atencion_6 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_6
)
letra_atencion_7 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_7
)
letra_atencion_8 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_8
)
letra_atencion_9 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_9
)
letra_atencion_10 = ctk.CTkEntry(
    frame_submenu_configuracion_atenciones,
    placeholder_text="Letra",
    width = 45,
    textvariable = var_letra_atencion_10
)

###BOTONES CONFIGURACIÓN DE ATENCIONES

#BOTÓN ON/OFF STATUS PREFERENCIAL
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
    padx = 5
    )

#BOTÓN SELECIÓN DE CANTIDAD DE ATENCIONES
dropmenu_config_num_atenciones = ctk.CTkOptionMenu(
    frame_submenu_configuracion_atenciones,
    values= ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    )
dropmenu_config_num_atenciones.grid(
    column = 1,
    row = 1,
    padx = 5
    )
dropmenu_config_num_atenciones.set("1")

#BOTÓN PARA PROCEDER A DEFINIR TEXTO Y LETRA DE LA CANTIDAD DE ATENCIONES DESEADAS
boton_definir_num_atenciones = ctk.CTkButton(
    frame_submenu_configuracion_atenciones,
    text= "Definir Atenciones",
    command= nombres_y_letras_atenciones
    )
boton_definir_num_atenciones.grid(
    column = 2,
    row = 1,
    padx = 5,
    pady = 5
    )

#BOTÓN CANCELAR ROTULADO DE ATENCIONES
boton_cancelar_num_atenciones = ctk.CTkButton(
    frame_submenu_configuracion_atenciones,
    text= "Cancelar",
    command= borrar_y_ocultar_atenciones
    )
boton_cancelar_num_atenciones.grid(
    column = 3,
    row = 1,
    padx = 5,
    pady = 5
    )


#BOTÓN DE CONFIRMACIÓN PARA CREACIÓN DE ATENCIONES
boton_confirmar_creacion_atenciones = ctk.CTkButton(
    frame_submenu_configuracion_atenciones,
    text= "Ok",
    command= verificar_nombres_y_letras
    )


#FRAME CONFIGURACIÓN DE SERVIDOR
frame_submenu_configuracion_servidor = ctk.CTkFrame(frame_configuracion)
###BOTÓN INICIAR SERVIDOR
boton_inicio_servidor = ctk.CTkButton(
    frame_submenu_configuracion_servidor,
    text= "Iniciar Servidor",
    command= server_thread
)
boton_inicio_servidor.grid(
    column = 0,
    row = 1,
    padx = 5,
    pady = 5
)

#FRAME CONFIGURACIÓN DE VIDEO
frame_submenu_configuracion_video = ctk.CTkFrame(frame_configuracion)







app.mainloop()