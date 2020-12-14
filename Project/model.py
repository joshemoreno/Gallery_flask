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
#Select images by status=1
#Update downloads by idImage
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