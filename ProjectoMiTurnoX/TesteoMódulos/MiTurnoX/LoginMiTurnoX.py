import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import psycopg2
from psycopg import sql
import os
from config import config

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mi Turno X - V 0.0.6")
        ctk.set_appearance_mode("dark")
        self.resizable(False, False)
        self.win_height = 200
        self.win_width = 350
        self.desk_height = self.winfo_screenheight()
        self.desk_width = self.winfo_screenwidth()
        self.x_axis = int((self.desk_width/2) - (self.win_width/2))
        self.y_axis = int((self.desk_height/2) - (self.win_height/2))
        self.geometry("{}x{}+{}+{}".format(self.win_width, self.win_height, self.x_axis, self.y_axis))
        """
        con = sqlite3.Connection('data/MiTurnoX.db')
        cur = con.cursor()
        cur.execute("
                    CREATE TABLE IF NOT EXISTS login_info(
                    id INTEGER PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    password TEXT NOT NULL,
                    level TEXT NOT NULL)
                    "
                    )
        con.commit()
        con.close()
        """
        self.main_frame = MainFrame(self)

    def check_cred(self):
            '''
            con = sqlite3.Connection('data/MiTurnoX.db')
            cur = con.cursor()
            ''' 

            try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                user = self.main_frame.entry_user.get()
                password = self.main_frame.entry_pass.get()
                #cur.execute('SELECT * FROM usr_login')
                #db_return = cur.fetchall()
                #for items in db_return:
                    #print(items)
                #cur.close()
                '''
                query = sql.SQL("SELECT {name}, {password}, {cred} FROM {table} WHERE {name} = %s AND {password} = %s").format(
                    name=sql.Identifier('usr_name'),
                    password = sql.Identifier('usr_pass'),
                    cred = sql.Identifier('usr_cred'),
                    table = sql.Identifier('usr_login')
                )
                '''
                cur.execute("SELECT usr_name, usr_pass, usr_cred FROM usr_login WHERE usr_name = %s AND usr_pass = %s", (user, password,))
                row = cur.fetchone()
                if row:
                    if row[2] == "ADMIN":
                        print('Verified Admin')
                        self.win_close()
                        os.system('python MiTurnoX.py')
                    elif row[2] == "MODULO":
                        print('Verified User')
                        self.win_close()
                        os.system('python ModuloMiTurnoX.py')
                else:
                    print('Denied')
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print('db close')


    def win_close(self):
        self.destroy()
               


class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_contenedor = ctk.CTkFrame(master)
        self.frame_contenedor.pack(fill = "both", expand = 1, padx= 5, pady= 5)
        self.frame_user = ctk.CTkFrame(self.frame_contenedor)
        self.frame_user.pack(fill = "x", padx= 5, pady = 5)
        self.frame_pass = ctk.CTkFrame(self.frame_contenedor)
        self.frame_pass.pack(fill = "x", padx= 5, pady = 5)
        self.etiqueta_user = ctk.CTkLabel(self.frame_user, text= "Usuario:        ")
        self.etiqueta_user.pack(side = "left", padx= 5, pady = 5)
        self.etiqueta_pass = ctk.CTkLabel(self.frame_pass, text= "Contraseña: ")
        self.etiqueta_pass.pack(side = "left", padx= 5, pady = 5)
        self.entry_user = ctk.CTkEntry(self.frame_user, placeholder_text= "Nombre de Usuario", width= 250)
        self.entry_user.pack(side = "left", padx= 5, pady = 5)
        self.entry_pass = ctk.CTkEntry(self.frame_pass, placeholder_text= "Contraseña", width= 250)
        self.entry_pass.pack(side = "left", padx= 5, pady = 5)
        self.boton_confirmar = ctk.CTkButton(self.frame_contenedor, text= "Confirmar", command= master.check_cred)
        self.boton_confirmar.pack(side = "right", padx= 5, pady= 5)


login = Login()
login.protocol("WM_DELETE_WINDOW", login.win_close)
login.mainloop()
