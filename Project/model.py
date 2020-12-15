from db import get_db, close_db

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


#Select images by status=1
def sql_select_images_by_status():
    db = get_db()
    images = db.execute('SELECT * FROM Image WHERE status= 1').fetchall()
    close_db()
    return images
#Update downloads by idImage
def update_downloads(id):
    db = get_db()   
    download = db.execute('SELECT downloads FROM Image WHERE idImage = ?',[id]).fetchone()
    downloads = download[0]
    downloads +=1
    db.execute('UPDATE Image SET downloads= ? WHERE idImage= ?',[downloads, id])
    db.commit()
    close_db()
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
def update_password(id,password):
    db = get_db()
    user = db.execute('SELECT * FROM User WHERE idUser= ?',[id]).fetchone()
    if user is not None:
        db.execute('UPDATE User SET password= ? WHERE idUser= ?',[password, id])
        db.commit()
        return user
        # print("update_password")
    else:
        return user
        # print("El usuario no existe")
    close_db()
    

#Select image by idImage
def sql_select_image_by_id(id):
    db = get_db()
    image = db.execute('SELECT * FROM Image WHERE idImage= ?',[id]).fetchone()
    return image
    close_db()
   


#Update votes by idImage
def update_votes(id,voteStatus):
    db = get_db()
    votes = db.execute('SELECT votes FROM Image WHERE idImage = ?',[id]).fetchone()
    if votes is not None:
        if(voteStatus == 1):
            votes+=1
        else:
            votes-=1
        db.execute('UPDATE Image SET votes= ? WHERE idImage= ?',[votes, id])
        db.commit()
        close_db()
        return votes
    else:
        return votes
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