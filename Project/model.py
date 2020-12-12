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
def sql_create_image(name, description, status, path, idUser):
    query = f"""INSERT INTO Image (name, description, status, path, idUser)
    values ('{name}','{description}',{status},'{path}',{idUser});"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    print("Create Image")

#Delete image by idImage
def sql_delete_image(idImage):
    query = f"""DELETE * FROM Image WHERE idImage = {idImage};"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    print('Delete Image')

#Select image by idUser
def sql_select_images_byUser(idUser):
    query = f"""SELECT * FROM Image WHERE idUser = {idUser};"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    images = cursor.fetchall()
    conexion.close()
    return images

#Select images from repository by keywords
def sql_select_images_from_repository_by_keyword(keyword, idUser):
    query = f"""SELECT * FROM Image WHERE name LIKE '"%{keyword}%"' OR description LIKE '"%{keyword}%"' AND idUser = {idUser};"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    images = cursor.fetchall()
    conexion.close()
    return images
#fin laura


#luis
#Select user information
#Select images by status
#Update downloads by idImage
#Delete image by idImage
#fin luis


#ivan
#Insert usuario y validar no existencia
#Update name, description, status, path
#Select for idImage
#fin ivan


#jose
#Update password
#Select image by idImage
#Update votes by idImage
#Select images by keywords
#fin jose