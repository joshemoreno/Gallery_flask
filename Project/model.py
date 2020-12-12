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
#Select images by status=1
#Update downloads by idImage
#fin luis


#ivan
#Insert usuario y validar no existencia
#Update name, description, status, path
#Select for idImage
#fin ivan


#jose
#Update password
def update_password(id,password):
    query = """UPDATE User SET password='{password}' WHERE idUser={id};"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    print("update_password")


#Select image by idImage
def sql_select_image_by_id(id):
    query = """SELECT * FROM Image WHERE idImage={id};"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    image = cursor.fetchone()
    conexion.close()
    return image


#Update votes by idImage
def update_votes(id,voteStatus):
    querySelect = """SELECT votes FROM Image WHERE idImage={id};"""
    conexion = sql_connection()
    cursorSelect = conexion.cursorSelect()
    cursorSelect.execute(querySelect)
    votes = cursor.fetchone()
    if(voteStatus == 1):
        votes+=1
        query = """UPDATE Image SET votes='{votes}' WHERE idImage={id};"""
    else:
        votes-=1
        query = """UPDATE Image SET votes='{votes}' WHERE idImage={id};"""
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    print("update_votes")


#Select images by keywords
def sql_select_images_by_keyword(keyword):
    query = """SELECT * FROM Image WHERE name LIKE '"%{keyword}%"' OR description LIKE '"%{keyword}%"' AND status = 1;"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    images = cursor.fetchall()
    conexion.close()
    return images
#fin jose