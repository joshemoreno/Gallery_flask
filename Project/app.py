# imports
import yagmail
from flask import Flask, render_template, flash, request, redirect, url_for, session, logging, g
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, BooleanField, SubmitField, FileField
from werkzeug.utils import secure_filename
from passlib.hash import sha256_crypt
from functools import wraps
import utils
import os
import model


# End imports

# varibles
yag = yagmail.SMTP('misiontic2022grupo11@gmail.com', '2022Grupo11')
UPLOAD_FOLDER = os.path.abspath("./uploader")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# EndVaribles

# init
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# EndInit

# Classes of Login
class LoginForm(Form):
    user = StringField('Usuario', [
        validators.Length(
            min=5, max=15, message=('El nombre del usuario debe tener 5 a 15 caracteres')
            ),
        validators.DataRequired('El nombre del usuario es obligatorio')
    ])

    password = PasswordField('Contraseña', [
        validators.DataRequired('La contraseña es obligatoria')
    ])

# End Classes of Login

# Login Route


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.user.data
        password_candidate = form.password.data
        user = model.sql_select_usuario_byUser(username)
        if user is not None:
            if user[6] != 0:
                password = user[3]
                if sha256_crypt.verify(password_candidate, password):
                    session['logged_in'] = True
                    session['username'] = username
                    session['id'] = user[0]
                    flash('You are logged in', 'success')
                    app.logger.info('PASSWORD MATCHED')
                    return redirect(url_for('in_session'))
                else:
                    app.logger.info('PASSWORD NO MATCHED')
                    error = 'sesión inválida'
                    return render_template('Login/login.html', form=form, error=error)
            else:
                app.logger.info('Activa tu cuenta')
                error = 'Activa tu cuenta'
                return render_template('Login/login.html', form=form, error=error)
        else:
            app.logger.info('PASSWORD NO MATCHED')
            error = 'sesión inválida'
            return render_template('Login/login.html', form=form, error=error)
    return render_template('Login/login.html', form=form)
# End Login route

# InSession Route

def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Plese login', 'danger')
			return redirect(url_for('login'))
	return wrap

@app.route('/insession')
@is_logged_in
def in_session():
        id_User = session['id']
        images = model.sql_select_images_byUser(id_User)
        if images is not None:
            if len(images)==0:
                return render_template('InSession/inSession.html')
            return render_template('InSession/inSession.html', images=images)
        else:
            error = 'Error buscar las imágenes de usuario en sesión, intenta de nuevo'
            flash(error)
            return render_template('InSession/inSession.html')
        return render_template('InSession/inSession.html')
# End InSession Route

# Logout Route

@app.route('/logout')
def log_out():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('index'))
# End Logout Route

# Update Route


@app.route('/update')
@is_logged_in
def update():
    return render_template('UpdateView/update.html')
# End Update Route

# DeleteImage Route


@app.route('/update/delete/<string:id>', methods=["POST"])
@is_logged_in
def image_delete(id):
    if request.method == 'POST':
        id_image = request.form['id_image']

        if not id_image:
            error = 'Debes seleccionar una imagen para ser eliminada'
            flash(error)
            return redirect(url_for('update'))

        image = model.sql_delete_image(id_image)
        if image is not None:
            success_message = 'Imagen eliminada exitosamente'
            flash(success_message)
            return redirect(url_for('update'))
        else:
            error = 'Error al eliminar la imagen, intenta de nuevo'
            flash(error)
            return redirect(url_for('update'))
    return redirect(url_for('update'))
# End DeleteImage Route

# End Class Search


class SearchForm(Form):
    text = StringField('Texto', [
        validators.DataRequired()
    ])
# End Class Search

# Search Route


@app.route('/search',  methods=['GET', 'POST'])
def search_image():
    images=[]
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        keyword= request.form['text']
        images = model.sql_select_images_by_keyword(keyword)
        print(images)
        if len(images)==0:
            return render_template('Search/searchImage.html', form=form)
        return render_template('Search/searchImage.html', form=form, images=images)
    print(images)
    return render_template('Search/searchImage.html', form=form)
    # return render_template('LandingPage/main.html')
# End Search Route

# ShowImage Route


@app.route('/showImage/<string:id>')
def showImage(id):
    image = model.sql_select_image_by_id(id)
    if image is not None:
        print(image)
        return render_template('ShowImage/showImage.html', image=image)
    else:
        print(image)
        return render_template('LandingPage/main.html')
    
# End ShowImage Route

# MostVoted Route


@app.route('/mostVoted')
def most_voted():
    return render_template('LandingPage/main.html')
# End MostVoted Route

# MostDownloaded Route


@app.route('/mostDownloaded')
def most_downloaded():
    return render_template('LandingPage/main.html')
# End Vote MostDownloaded Route

# Vote Route


@app.route('/vote', methods=["POST"])
def vote():
    # save vote
    if request.method == 'POST':
        jsonData = request.json
        idImage = jsonData['idImage']
        voteStatus = jsonData['voteStatus']
        model.update_votes(idImage,voteStatus)
        status = "ok"
        return status

# End Vote Route

# Download Route


@app.route('/download/<string:id>', methods=["POST"])
def download(id):
    # buscar imagen en directorio
    status = "ok"
    return status
# End Download Route

# MainRoute


@app.route('/')
def index():
    return render_template('LandingPage/main.html')
# End MainRoute

# Class registerForm


class RegisterForm(Form):
    user = StringField('Usuario', [
        validators.Length(
            min=5, max=15, message='El nombre del usuario debe tener 5 a 15 caracteres'), validators.DataRequired()
    ])
    email = StringField('Correo', [
        validators.Length(
            min=6, max=30, message='El el correo debe tener 6 a 30 caracteres'), validators.DataRequired()
    ])
    password = PasswordField('Contraseña', [
        validators.Length(
            min=7, max=15, message='La contraseña debe tener entre 7 a 15 caracteres'),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Las contraseñas no coinciden')
    ])
    confirm = PasswordField('Confirma contraseña')
# End Class registerForm

# RegisterRoute


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.user.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        usuario = model.sql_insert_user(user, email, password)
        print(usuario)
        if usuario is None:
            yag.send(email, 'Activa tu cuenta',
                    ''' <h1> Bienvenid@ a nuestra comunidad </h1>
                <h3><b>Hola, '''+user+'''</b></h3><br><p>Este correo es para informarte que te has registrado en PHOTOS<p>
                <a href="http://localhost:5000/activate/'''+user+'''">Activa tu cuenta</a>
                <p>Si usted no realizo este registro por favor ignore este mensaje, gracias!</p>
                ''')
            return redirect(url_for('index'))
        else:
            return render_template('SingIn/singIn.html', form=form)
            # flash('Ya te has registrado revisa tu correo y activa tu cuenta', 'correcto')
    return render_template('SingIn/singIn.html', form=form)

# End RegisterRoute

@app.route('/activate/<string:user>', methods=['GET', 'POST'])
def activate(user):
    model.sql_activate_count(user)
    return redirect(url_for('login'))



# Class resetForm


class ResetForm(Form):
    password = PasswordField('Contraseña', [
        validators.Length(
            min=7, max=15, message='La contraseña debe tener entre 7 a 15 caracteres'),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Las contraseñas no coinciden')
    ])
    confirm = PasswordField('Confirma contraseña', [validators.DataRequired()])
# End Class resetForm

# Reset Route


@app.route('/resetpassword/<string:id>', methods=['GET', 'POST'])
def reset(id):
    form = ResetForm(request.form)
    if request.method == 'POST' and form.validate():
        password = sha256_crypt.encrypt(str(form.password.data))
        user = model.update_password(id,password)
        if user is not None:
            # print(user)
            return redirect(url_for('index'))
        else:
            print(user)
            return render_template('Reset/resetPassword.html', form=form)

    return render_template('Reset/resetPassword.html', form=form)
# End ResetRoute

# Class uploadForm


class UploadForm(Form):
    title = StringField('Nombre', [
        validators.Length(
            min=5, max=20, message='El nombre de la imagen debe tener de 5 a 20 caracteres'), validators.DataRequired()
    ])
    description = TextAreaField('Descripción', [
        validators.Length(
            min=15, max=250, message='El nombre de la descripción de la imagen debe tener de 15 a 250 caracteres'), validators.DataRequired()
    ])
    status = BooleanField()
# End Class uploadForm

# validator


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# End validator

# upload Route


@app.route('/upload', methods=['GET', 'POST'])
@is_logged_in
def upload():
    form = UploadForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        description = form.description.data
        status = form.status.data
        image = request.files['file']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        if not title:
            error = 'Debes ingresar un título'
            flash(error)
            return render_template('UploadView/upload.html', form=form)
        
        if not description:
            error = 'Debes ingresar una descripción'
            flash(error)
            return render_template('UploadView/upload.html', form=form)
        
        if not status:
            status = 0
        
        if not image.filename:
            error = 'Debes adjuntar una imagen'
            flash(error)
            return render_template('UploadView/upload.html', form=form)
        
        imageCreated = model.sql_create_image(title, description, status, image.filename,session['id'])
        if imageCreated is not None:
            success_message = 'Imagen creada exitosamente'
            flash(success_message)
            return render_template('inSession/inSession.html', form=form)
        else:
            error = 'Error al crear la imagen, intenta de nuevo'
            flash(error)
            return render_template('UploadView/upload.html', form=form)
    return render_template('UploadView/upload.html', form=form)
# End upload Route

# Class updateForm


class UpdateForm(Form):
    title = StringField('Nombre', [
        validators.Length(
            min=5, max=20, message='El nombre de la imagen debe tener de 5 a 20 caracteres')
    ])
    description = TextAreaField('Descripción', [
        validators.Length(
            min=15, max=250, message='El nombre de la descripción de la imagen debe tener de 15 a 250 caracteres')
    ])
    status = BooleanField()
# End Class updateForm

# update Route


@app.route('/updateform/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def updateform(id):
    form = UpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        description = form.description.data
        status = form.status.data
        # path = form.description.path
        model.sql_update_image(id, title, description, status)
    return render_template('UpdateForm/updateForm.html', form=form)
# End update Route

# class search


class InSessionSearchForm(Form):
    texto = StringField('Texto', [
        validators.DataRequired()
    ])
# End search

# updateSearch Route


@app.route('/update/search', methods=["POST"])
@is_logged_in
def update_search():
    form = InSessionSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        idUser = session['id']
        texto = request.form['texto']
        images = model.sql_select_repository_images(texto, idUser)
        if not texto:
            error = 'Debes escribir alguna palabra de búsqueda'
            flash(error)
            return render_template('updateView/update.html', form=form)
      
        if len(images) == 0:
                return render_template('updateView/update.html', form=form)
        else:
            return render_template('updateView/update.html', form=form, images=images)
    return render_template('Updateview/update.html', form=form)


@app.route('/insession/search', methods=["POST"])
@is_logged_in
def inSession_search():
    form = InSessionSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        idUser = session['id']
        texto = request.form['texto']
        images = model.sql_select_repository_images(texto, idUser)
        if not texto:
            error = 'Debes escribir alguna palabra de búsqueda'
            flash(error)
            return render_template('inSession/inSession.html')
        
        if len(images) == 0:
            return render_template('InSession/inSession.html')
        else:
            return render_template('InSession/inSession.html', images=images)
    return render_template('inSession/inSession.html')
# End updateSearch Route

# Class ResetRequestForm


class ResetRequestForm(Form):
    email = StringField('Correo', [
        validators.Length(
            min=6, max=30, message='El nombre del usuario debe tener de 6 a 30 caracteres'), validators.DataRequired()
    ])
# End Class ResetRequestForm

# reset_request


@app.route('/resetRequest', methods=['GET', 'POST'])
def resetRequest():
    form = ResetRequestForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        user = model.sql_select_usuario_byEmail(email)
        if user is not None:
            idUser=str(user[0])
            yag.send(email, 'Reestablecer contraseña de PHOTOS',
                    ''' <h1>¿HAS OLVIDADO TU CONTRASEÑA? </h1>
                <h3><b>Hola, '''+user[1]+'''</b></h3><br><p>Esta es una solicitud para restablecer tu contraseña</p>
                Haz clic en el siguiente enlace para restablecer tu contraseña
                <a href="http://localhost:5000/resetpassword/'''+idUser+'''">Restablece tu contraseña</a>
                <p>Si no has solicitado una nueva contraseña, por favor ignore este mensaje, gracias!</p>
                ''')
            return redirect(url_for('login'))
        else:
            return render_template('Reset/resetRequest.html', form=form)
    return render_template('Reset/resetRequest.html', form=form)
# End resetRequest
