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
    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Credenciales incorrectas. Intenta de nuevo'
    #     else:
    #         return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/imageDelete/<id>', methods=["DELETE"])
def image_delete(id):
    return redirect(url_for('update'))


#Luis

#jose
@app.route('/')
def index():
    return render_template('LandingPage/main.html')