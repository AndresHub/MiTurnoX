import customtkinter as ctk
lista1 = ["1", "2", "3"]

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.minsize(500, 500)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack()
        self.frame_1 = frame1(self)

class frame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame1 = ctk.CTkFrame(master.main_frame)
        self.frame1.pack()
        self.menu1 = ctk.CTkOptionMenu(self.frame1, values= lista1 )
        self.menu1.pack()



if __name__ == "__main__":
    app = App()
    app.mainloop()