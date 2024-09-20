import psycopg2
from config import config

def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT * FROM usr_login')
        db_return = cur.fetchall()
        for items in db_return:
            print(items)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('db close')

connect()



"""
###CÖDIGO USADO PARA ENVIAR NOMBRES DE LAS ATENCIONES A LA BASE DE DATOS###
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
"""




