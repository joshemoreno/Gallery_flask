from db import get_db, close_db

#Laura
#Insert imagen y validar no existencia
def sql_create_image(name, description, status, path, idUser):
    db = get_db()
    imageCreated = db.execute('INSERT INTO Image (name, description, status, path, idUser) values (?,?,?,?,?)', (name, description, status, path, idUser))
    db.commit()
    close_db()
    return imageCreated

#Delete image by idImage
def sql_delete_image(id):
    db=get_db()
    image = db.execute('DELETE FROM Image WHERE idImage = ?', (id))
    db.commit()
    close_db()
    return image

#Select image by idUser
def sql_select_images_byUser(id):
    db = get_db()
    images = db.execute('SELECT * FROM Image WHERE idUser = ?', [id]).fetchall()
    db.commit()
    close_db()
    return images

#Select images from repository by keywords
def sql_select_repository_images(keyword, id):
    db = get_db()
    images = db.execute('SELECT * FROM Image WHERE (name LIKE :keyword OR description LIKE :keyword) AND idUser = :idUser', {"keyword": '%'+keyword+'%', "idUser":id}).fetchall()
    db.commit()
    close_db()
    return images
#fin laura


#luis
#Select user information
def sql_select_usuario_byUser(idUser):
    query = f"""SELECT * FROM User WHERE idUser = {idUser};"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    usuario = cursor.fetchall()
    conexion.close()
    return usuario
#Select images by status=1
def sql_select_images_from_repository_by_status(status):
    query = f"""SELECT * FROM Image WHERE status = {status};"""
    conexion = sql_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    images = cursor.fetchall()
    conexion.close()
    return images
#Update downloads by idImage
def update_downloads(id,downloadStatus):
    querySelect = """SELECT downloads FROM Image WHERE idImage={id};"""
    conexion = sql_connection()
    cursorSelect = conexion.cursorSelect()
    cursorSelect.execute(querySelect)
    downloads = cursor.fetchone()
    if(downloadStatus == 1):
        downloads+=1
        query = """UPDATE Image SET downloads='{votes}' WHERE idImage={id};"""
    else:
        downloads-=1
        query = """UPDATE Image SET downloads='{votes}' WHERE idImage={id};"""
    cursor = conexion.cursor()
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    print("update_downloads")
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
    db = get_db()
    images = db.execute('SELECT * FROM Image WHERE (name LIKE :keyword OR description LIKE :keyword) AND status=1', {"keyword": '%'+keyword+'%'}).fetchall()
    return images
    close_db()
#fin jose