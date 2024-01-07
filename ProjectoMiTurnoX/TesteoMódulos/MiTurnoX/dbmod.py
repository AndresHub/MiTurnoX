import sqlite3

con = sqlite3.Connection('data/MiTurnoX.db')
cur = con.cursor()
tuple = ("Andres", "pass", "Usr")
cur.execute("INSERT INTO login_info(user_name, password, level) VALUES(?,?,?)", (tuple))
con.commit()
con.close()