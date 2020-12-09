# imports
import yagmail
from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, BooleanField, SubmitField, FileField
from werkzeug.utils  import secure_filename
from passlib.hash import sha256_crypt
from functools import wraps
import utils
import os

# secret_key=os.urandom(24)
# secret_key='secrect123'
yag = yagmail.SMTP('misiontic2022grupo11@gmail.com', '2022Grupo11')
# UPLOAD_FOLDER = 'D:\Descarga\Mintic\Ciclo3\ProyectoGrupoE'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key=os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Laura
@app.route('/search/<string:name>')
def search_image(name):
    return render_template('Search/searchImage.html')

@app.route('/vote', methods=["POST"])
def vote():
    #save vote
    vote = 1
    status = "ok"
    return status

@app.route('/download', methods=["POST"])
def download():
    #buscar imagen en directorio
    status = "ok"
    return status

@app.route('/insession')
def in_session():
    return render_template('InSession/inSession.html')

@app.route('/update')
def update():
    return render_template('UpdateView/update.html')

@app.route('/showImage')
def showImage():
    return render_template('ShowImage/showImage.html')

@app.route('/logout')
def log_out():
    #logout_user()
    return redirect(url_for('index'))


class LoginForm(Form):
    user = StringField('Usuario',[validators.Length(min=1, max=50)])
    password = PasswordField('Contraseña', [
      validators.DataRequired()
      ])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.user.data
    return render_template('Login/login.html', form=form)
    #return render_template('login.html', title='Login', form=form)

    # status = "ok"
    # return status
    # login_form = forms.LoginForm(request.form)
    # if request.method == 'POST' and login_form.validate():
    #     username = login_form.username.data
    #     successs_message = 'Bienvenido {}'. format(username)
    #     flash(success_message)

    #     session['username'] = login_form.username.data
    # return render_template('LandingPage/main.html', form = login_form)

@app.route('/imageDelete/<id>', methods=["DELETE"])
def image_delete(id):
    return redirect(url_for('update'))

##Validar que no esté duplicado
@app.route('/resetRequest', methods=['GET', 'POST'])
def resetRequest():
    return render_template('Reset/resetRequest.html')
    
#Luis

#jose

# MainRoute
@app.route('/')
def index():
    return render_template('LandingPage/main.html')

# End MainRoute


# Class registerForm
class RegisterForm(Form):
  user = StringField('Usuario',[
      validators.Length(min=5, max=15, message='El nombre del usuario debe tener de 5 a 15 caracteres')
      ,validators.DataRequired()
      ])
  email = StringField('Correo', [
      validators.Length(min=6, max=30, message='El nombre del usuario debe tener de 6 a 30 caracteres')
      ,validators.DataRequired()
      ])
  password = PasswordField('Contraseña', [
      validators.DataRequired(),
      validators.EqualTo('confirm', message='Las contraseñas no coinciden')
      ])
  confirm = PasswordField('Confirma contraseña')
#End Class registerForm

# RegisterRoute
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.user.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        # flash('Ya te has registrado revisa tu correo y activa tu cuenta', 'correcto')
        yag.send(email, 'Activa tu cuenta', 
        ''' <h1> Bienvenid@ a nuestra comunidad </h1>
            <h3><b>Hola, '''+user+'''</b></h3><br><p>Este correo es para informarte que te has registrado en PHOTOS<p>
            <a href="http://localhost:5000/insession">Activa tu cuenta</a>
            <p>Si usted no realizo este registro por favor ignore este mensaje, gracias!</p>
            ''')
        return redirect(url_for('index'))
    return render_template('SingIn/singIn.html', form=form)
# End RegisterRoute

# Class resetForm
class ResetForm(Form):
    password = PasswordField('Contraseña', [
      validators.DataRequired(),
      validators.EqualTo('confirm', message='Las contraseñas no coinciden')
      ])
    confirm = PasswordField('Confirma contraseña', [validators.DataRequired()])
#End Class resetForm

# ResetRoute
@app.route('/resetpassword/<string:id>', methods=['GET', 'POST'])
def reset(id):
    form = ResetForm(request.form)
    if request.method == 'POST' and form.validate():
        password = sha256_crypt.encrypt(str(form.password.data))
        return redirect(url_for('index'))
    return render_template('Reset/resetPassword.html', form=form)
# End ResetRoute

# Class uploadForm
class UploadForm(Form):
  title = StringField('Nombre',[
      validators.Length(min=5, max=15, message='El nombre del usuario debe tener de 5 a 15 caracteres')
      ,validators.DataRequired()
      ])
  description = TextAreaField('Descripción', [
      validators.Length(min=10, max=50, message='El nombre del usuario debe tener de 10 a 50 caracteres')
      ,validators.DataRequired()
      ])
  status = BooleanField()
#End Class uploadForm

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
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
    return render_template('UploadView/upload.html', form=form)


# Class updateForm
class UpdateForm(Form):
  title = StringField('Nombre',[
      validators.Length(min=5, max=15, message='El nombre del usuario debe tener de 5 a 15 caracteres')
      ,validators.DataRequired()
      ])
  description = TextAreaField('Descripción', [
      validators.Length(min=10, max=50, message='El nombre del usuario debe tener de 10 a 50 caracteres')
      ,validators.DataRequired()
      ])
  status = BooleanField()
#End Class updateForm


@app.route('/updateform/<string:id>', methods=['GET', 'POST'])
def updateform(id):
    form = UpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        description = form.description.data
        status = form.status.data
        image = request.files['file']
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('UpdateForm/updateForm.html', form=form)


# @app.route('/update/search/<string:name>')
# def update():
#     return render_template('Updateview/update.html')

# @app.route('/insession/search/<string:name>')
# def inSession():
#     return render_template('inSession/inSession.html')

