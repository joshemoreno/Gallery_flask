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
contents = ["hola"]
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
        yag.send(email, 'Activa tu cuenta', contents)
        return redirect(url_for('index'))
    # print(user,email,password)
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
