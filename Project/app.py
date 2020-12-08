# imports
import yagmail
from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import utils
import os
# secret_key=os.urandom(24)
secret_key='secrect123'
yag = yagmail.SMTP('jose_antonio.moreno@uao.edu.co', 'Autonoma0902')


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

@app.route('/login', methods=['GET', 'POST'])
def login():
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
  user = StringField('Usuario',[validators.Length(min=1, max=50)])
  email = StringField('Correo', [validators.Length(min=6, max=50)])
  password = PasswordField('Contraseña', [
      validators.DataRequired(),
      validators.EqualTo('confirm', message='Password do not match')
      ])
  confirm = PasswordField('Confirma contraseña')
#End Class registerForm

# MailContent

# End MailContent

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

# ResetRoute
@app.route('/reset/:id', methods=['GET', 'POST'])
def reset(id):
    return render_template('Reset/resetPassword.html')
# End ResetRoute


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('UploadView/upload.html')

@app.route('/updateform/:id', methods=['GET', 'POST'])
def updateform(id):
    return render_template('UpdateForm/updateForm.html')
