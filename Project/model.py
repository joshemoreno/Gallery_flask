import sqlite3
from sqlite3 import Error

def sql_connection():
        try:
            conexion = sqlite3.connect('photos.db')
            return conexion
        except Error:
            print(Error)


#Laura
#Insert imagen y validar no existencia
#Select for idImage
#Select image by idUser
#fin laura


#luis
#Select user information
#Select images by status
#Update downloads by idImage
#Delete image by idImage
#fin luis


#ivan
#Insert usuario y validar no existencia
def sql_insert_user(name, email, password):
    conexion = sql_connection()
    cursor = conexion.cursor()
    query = f"""select email from User where email = '{email}';"""
    cursor.execute(query)
    emailUser = cursor.fetchone()

    if (emailUser == None):
        query = f"""insert into User (name, email, password)
        values ('{name}','{email}','{password}');"""
        cursor.execute(query)
        conexion.commit()

    conexion.close()
    return emailUser


#Update name, description, status, path
def sql_update_image(id, name, description, status, path):
    conexion = sql_connection()
    cursor = conexion.cursor()
    query = f"""update Image set name = '{name}', description = '{description}', status = '{status}', path = '{path}' where idImage = {id};"""
    cursor.execute(query)
    conexion.commit()
    conexion.close()

#fin ivan


#jose
#Update password
#Select image by idImage
#Update votes by idImage
#Select images by keywords
#fin jose