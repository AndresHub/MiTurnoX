from typing import Tuple
from config2 import *
import customtkinter as ctk
from customtkinter import filedialog
import psycopg2
import datetime
import time

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pruebas Generales de código")
        self.geometry("1000x600")
        self.lista_frames = []

    def frame_within_frame(self):
        self.frame1 = ctk.CTkFrame(self, width= 1000, height= 500)
        self.frame1.pack()
        self.label1 = ctk.CTkLabel(self.frame1, text = "prueba destroy recursivo con winfo_children frame1")
        self.label1.pack()
        self.frame2 = ctk.CTkFrame(self.frame1, width= 800, height= 400)
        self.frame2.pack()
        self.label2 = ctk.CTkLabel(self.frame2, text = "prueba destroy recursivo con winfo_children frame 2")
        self.label2.pack()
        self.frame3 = ctk.CTkFrame(self.frame2, width= 600, height= 300)
        self.frame3.pack()
        self.label3 = ctk.CTkLabel(self.frame3, text = "prueba destroy recursivo con winfo_children frame 3")
        self.label3.pack()
        self.nivel = self.frame1

    def destroy_recursivo(self, obj):
        print(self.frame1.cget(all))
        for objeto in obj.winfo_children():
            if type(objeto).__name__ == "CTkFrame":
                self.lista_frames.append(f"{objeto}")
                self.destroy_recursivo(objeto)
            else:
                objeto.destroy()
        print(self.lista_frames)

    def build(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack()
        self.boton1 = ctk.CTkButton(self.main_frame, command = self.frame_within_frame)
        self.boton1.pack()
        self.boton2 = ctk.CTkButton(self.main_frame, command = lambda: self.destroy_recursivo(self.nivel))
        self.boton2.pack()
        #self.boton3 = ctk.CTkButton(self, command= self.bajar_nivel)
        #self.boton3.pack()

Test = App()
Test.build()
Test.mainloop()


#filedialog para conseguir DIR o Archivo. Usado para colgar imagen de logo, y para dar ruta a los videos.
"""
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pruebas Generales de código")
        self.geometry("500x500")

    def selfile(self):
        self.filename = filedialog.askopenfilename()
        print(self.filename)
    def build(self):
        self.frame = ctk.CTkFrame(self)
        self.frame.pack()
        self.boton = ctk.CTkButton(self, command = self.selfile)
        self.boton.pack()

Test = App()
Test.build()
Test.mainloop()
"""

#TIME STAMPS E IMPORTACION DE DATOS DE .INI
"""
values = config2()
start = datetime.datetime.now()
print(start)
print(values["host"])
print(values["port"])
time.sleep(2)
finish = datetime.datetime.now()
print(finish)
print(finish - start)
"""

#BORRAR ELEMENTO DE ATN_TABLE CON EL ID DESIGNADO
"""
conn = None            
try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('DELETE FROM atn_table WHERE atn_id = 4000')
        conn.commit()
        cur.close()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if conn is not None:
        conn.close()
"""