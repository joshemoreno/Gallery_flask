# imports
import yagmail
from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, BooleanField, SubmitField, FileField
from  werkzeug.utils  import  secure_filename
from passlib.hash import sha256_crypt
from functools import wraps
import utils
import os
# secret_key=os.urandom(24)
secret_key='secrect123'
yag = yagmail.SMTP('misiontic2022grupo11@gmail.com', '2022Grupo11')


app = Flask(__name__)

#Laura
@app.route('/search/<name>')
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

@app.route('/logout')
def log_out():
    #logout_user()
    return redirect(url_for('index'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
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
  image = FileField(validators.DataRequired())

#End Class uploadForm

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        description = form.description.data
        status = form.status.data
        images = form.image.data
        filename = secure_filename(images.filename)
        f.save(os.path.join(
            app.instance_path,'photos',filename
        ))
        print(title,description,status,image)
    return render_template('UploadView/upload.html', form=form)

@app.route('/updateform/<string:id>', methods=['GET', 'POST'])
def updateform(id):
    return render_template('UpdateForm/updateForm.html')
