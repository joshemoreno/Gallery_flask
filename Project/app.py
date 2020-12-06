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