import customtkinter as ctk
import os
from PIL import Image
import asyncio

class Pantalla(ctk.CTk):
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
            self.iniciar_slide()
            self.label.pack()
            self.siguiente_imagen()

    def iniciar_slide(self):
        self.ruta_imagenes_pantalla = rf"{os.getcwd()}\Recursos\Imagenes\Slide"
        self.listado_imagenes = os.listdir(self.ruta_imagenes_pantalla)
        self.imagen = [(ctk.CTkImage(dark_image = Image.open(rf"{self.ruta_imagenes_pantalla}\{x}"), size= (500,500))) for x in self.listado_imagenes]
        self.label = ctk.CTkLabel(self, text= "")
        self.label.imagen = self.imagen
        self.label.counter = 0
        
    def siguiente_imagen(self):
        self.label.configure(image = self.label.imagen[self.label.counter%len(self.label.imagen)])
        self.label.after(3000, self.siguiente_imagen)
        self.label.counter += 1
                  

App = Pantalla()
App.mainloop()