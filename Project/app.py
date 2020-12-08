# imports
import yagmail
from flask import Flask, render_template, flash, request, redirect, url_for
import utils

app = Flask(__name__)

#Laura

#Luis

#jose
@app.route('/')
def index():
    return render_template('LandingPage/main.html')

# @app.route('/update/search/<string:name>')
# def update():
#     return render_template('Updateview/update.html')

# @app.route('/insession/search/<string:name>')
# def inSession():
#     return render_template('inSession/inSession.html')