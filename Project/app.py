# imports
import yagmail
from flask import Flask, render_template, flash, request, redirect, url_for, session, logging, g
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, BooleanField, SubmitField, FileField
from werkzeug.utils  import secure_filename
from passlib.hash import sha256_crypt
from functools import wraps
import utils
import os

# secret_key=os.urandom(24)
# secret_key='secrect123'
yag = yagmail.SMTP('misiontic2022grupo11@gmail.com', '2022Grupo11')
UPLOAD_FOLDER = os.path.abspath("./uploader")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key=os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#Laura

#Check the session at the beggining of request
@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#Classes of Login
class LoginForm(Form):
    user = StringField('Usuario',[
        validators.Length(min=1, max=50, message=('El nombre debe tener máximo 50 caracteres')),
        validators.DataRequired('El nombre del usuario es obligatorio')
        ])
        
    password = PasswordField('Contraseña', [
      validators.DataRequired('La contraseña es obligatoria')
      ])

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username}>'

## Esta información vendría de DB
users = []
users.append(User(id=1, username='Laura', password='password'))
users.append(User(id=2, username='Jose', password='secret'))
users.append(User(id=3, username='Luis', password='hola'))
users.append(User(id=4, username='Ivan', password='mundo'))
##
#End Classes of Login

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('in_session'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        session.pop('user_id', None)

        username = form.user.data
        password = form.password.data

        usuario = [x for x in users if x.username == username][0]
        #password_candidate = sha256_crypt.encrypt(str(usuario.password)) #para validar contraseña encriptada que viene de DB
        #if password_candidate == password: #para validar contraseña encriptada
        if usuario and usuario.password == password:
            session['user_id'] = usuario.id
            # successs_message = 'Bienvenido {}'. format(usuario.username)
            # flash(success_message)
            app.logger.info('PASSWORD MATCHED')
            return redirect(url_for('in_session'))
        else:
            app.logger.info('PASSWORD NO MATCHED')
            error = 'sesión inválida'
            return render_template('Login/login.html', form=form, error=error)
        return redirect(url_for('login'))
    return render_template('Login/login.html', form=form)
#End Login route

# InSession Route
@app.route('/insession')
def in_session():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('InSession/inSession.html')
# End InSession Route

# Logout Route
@app.route('/logout')
def log_out():
    session.pop('user_id', None)
    return redirect(url_for('index'))
# End Logout Route

# Update Route
@app.route('/update')
def update():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('UpdateView/update.html')
# End Update Route

# DeleteImage Route
@app.route('/update/delete/<string:id>', methods=["POST"]) 
def image_delete(id):
    if not g.user:
        return redirect(url_for('login'))
    return redirect(url_for('update'))
# End DeleteImage Route

# End Class Search
class SearchForm(Form):
    texto = StringField('Texto',[
        validators.DataRequired()
        ])
# End Class Search

# Search Route
@app.route('/search', methods=["POST"])
def search_image():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        texto = request.form['texto']
        return render_template('Search/searchImage.html', form=form)
    return render_template('LandingPage/main.html')
#End Search Route

# ShowImage Route
@app.route('/showImage/<string:id>')
def showImage(id):
    return render_template('ShowImage/showImage.html')
#End ShowImage Route

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
@app.route('/vote/<string:id>', methods=["POST"])
def vote(id):
    #save vote
    vote = 1
    status = "ok"
    return status
# End Vote Route

# Download Route
@app.route('/download/<string:id>', methods=["POST"])
def download(id):
    #buscar imagen en directorio
    status = "ok"
    return status
# End Download Route

# ResetRequest Route (Validar que no esté repetida)
# @app.route('/resetRequest', methods=['GET', 'POST'])
# def resetRequest():
#     return render_template('Reset/resetRequest.html')
# End ResetRequest Route

#End Laura

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
  image   = FileField('Image File', [validators.Length(min=)])
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
    if not g.user:
        return redirect(url_for('login'))
    form = UploadForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        description = form.description.data
        status = form.status.data
        image = request.files['file']
        if str(image) == "<FileStorage: '' ('application/octet-stream')>":
            print("Hola mundo")
            return render_template('UploadView/upload.html', form=form)
            
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

class InSessionSearchForm(Form):
    texto = StringField('Texto',[
        validators.DataRequired()
        ])

@app.route('/update/search', methods=["POST"])
def update_search():
    form = InSessionSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        texto = request.form['texto']
        return render_template('Updateview/update.html', form=form)
    return render_template('Updateview/update.html')

@app.route('/insession/search', methods=["POST"])
def inSession_search():
    form = InSessionSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        texto = request.form['texto']
        return render_template('inSession/inSession.html', form=form)
    return render_template('inSession/inSession.html')


# Class ResetRequestForm
class ResetRequestForm(Form):
  email = StringField('Correo', [
      validators.Length(min=6, max=30, message='El nombre del usuario debe tener de 6 a 30 caracteres')
      ,validators.DataRequired()
      ])
# End Class ResetRequestForm

# reset_request
@app.route('/resetRequest/<string:id>', methods=['GET', 'POST'])
def resetRequest(id):
    form = ResetRequestForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        # user = form.user.data
        # flash('Ya te has registrado revisa tu correo y activa tu cuenta', 'correcto')
        yag.send(email, 'Reestablecer contraseña de PHOTOS', 
        ''' <h1>¿HAS OLVIDADO TU CONTRASEÑA? </h1>
            <h3><b>Hola, '''+email+'''</b></h3><br><p>Esta es una solicitud para restablecer tu contraseña</p>
            Haz clic en el siguiente enlace para restablecer tu contraseña
            <a href="http://localhost:5000/resetpassword/1">Restablece tu contraseña</a>
            <p>Si no has solicitado una nueva contraseña, por favor ignore este mensaje, gracias!</p>
            ''')
        return redirect(url_for('login'))
    return render_template('Reset/resetRequest.html', form=form)
# End resetRequest



