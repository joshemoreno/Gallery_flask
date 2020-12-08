# imports
import yagmail
from flask import Flask, render_template, flash, request, redirect, url_for
import utils

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
@app.route('/')
def index():
    return render_template('LandingPage/main.html')