import customtkinter as ctk

app = ctk.CTk()
app.title("Prueba Custom Tkinter")
ctk.set_appearance_mode("dark")
app.geometry("500x500")
frame = ctk.CTkFrame(app)
frame.grid(column = 0, row = 0)
frame.configure(fill = "x")
boton = ctk.CTkButton(app)
boton.grid(column = 0, row = 1)
boton = ctk.CTkButton(app)
boton.grid(column = 1, row = 1)

app.mainloop()