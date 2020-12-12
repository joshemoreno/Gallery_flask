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
#Update name, description, status, path
#Select for idImage
#fin ivan


#jose
#Update password
#Select image by idImage
#Update votes by idImage
#Select images by keywords
#fin jose