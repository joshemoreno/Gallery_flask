from db import get_db, close_db
import datetime

#Insert imagen y validar no existencia
def sql_create_image(name, description, status, path, idUser):
    time = datetime.datetime.now()
    db = get_db()
    imageCreated = db.execute('INSERT INTO Image (name, description, status, path, idUser, created_at) values (?,?,?,?,?,?)', (name, description, status, path, idUser, time))
    db.commit()
    close_db()
    return imageCreated

#Delete image by idImage
def sql_delete_image(id):
    db=get_db()
    image = db.execute('DELETE FROM Image WHERE idImage = ?', [id])
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
    close_db()
    return images

#Select user information
def sql_select_usuario_byUser(username):
    db = get_db()
    user = db.execute('SELECT * FROM User WHERE name=?',[username]).fetchone()
    close_db()
    return user

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

#Insert usuario y validar no existencia
def sql_insert_user(user, email, password):
    time = datetime.datetime.now()
    db = get_db()
    emailUser = db.execute('SELECT name, email from User where email = ? OR name = ?',[email, user]).fetchone()
    if (emailUser is None):
        newUser = db.execute('INSERT INTO User (name, email, password, created_at, status) values (?,?,?,?,?)', (user, email, password, time, 0))
        db.commit()
    close_db()
    return emailUser

#Update name, description, status
def sql_update_image(id, name, description, status):
    time = datetime.datetime.now()
    db = get_db()
    image = db.execute('UPDATE Image SET name = ?, description = ?, status = ?, updated_at = ? WHERE idImage= ?',[name, description, status, time, id])
    db.commit()
    close_db()
    return image

#Update password
def update_password(id,password):
    time = datetime.datetime.now()
    db = get_db()
    user = db.execute('SELECT * FROM User WHERE idUser= ?',[id]).fetchone()
    if user is not None:
        db.execute('UPDATE User SET password= ?, updated_at= ? WHERE idUser= ?',[password, time, id])
        db.commit()
        return user
    else:
        return user
    close_db()
    
#Select image by idImage
def sql_select_image_by_id(id):
    db = get_db()
    image = db.execute('SELECT * FROM Image WHERE idImage= ?',[id]).fetchone()
    return image
    close_db()
   
#Update votes by idImage
def update_votes(idImage,voteStatus):
    db = get_db()
    print(idImage,voteStatus)
    votes = db.execute('SELECT votes FROM Image WHERE idImage = :idImage',{"idImage":idImage}).fetchone()
    if votes is not None:
        toVote=votes[0]
        voteStatus=int(voteStatus)
        if(voteStatus == 1):
            toVote=toVote+1
            db.execute('UPDATE Image SET votes= ? WHERE idImage= ?',[toVote, idImage])
        else:
            toVote=toVote-1
            db.execute('UPDATE Image SET votes= ? WHERE idImage= ?',[toVote, idImage])
        db.commit()
        close_db()
        return toVote
    else:
        return votes
    print("update_votes")

#Select images by keywords
def sql_select_images_by_keyword(keyword):
    db = get_db()
    images = db.execute('SELECT * FROM Image WHERE (name LIKE :keyword OR description LIKE :keyword) AND status=1', {"keyword": '%'+keyword+'%'}).fetchall()
    return images
    close_db()

def sql_select_usuario_byEmail(email):
    db = get_db()
    user = db.execute('SELECT * FROM User WHERE email=?',[email]).fetchone()
    close_db()
    return user

def sql_activate_count(user):
    db = get_db()
    db.execute('UPDATE User SET status=1 WHERE name=?',[user])
    db.commit()
    close_db()