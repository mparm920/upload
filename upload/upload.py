                             #!/usr/bin/python3
import os
from flask import Flask, request, redirect, url_for, render_template, flash, session
from werkzeug.utils import secure_filename
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#config
app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)
from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args, **kargs):
        if 'logged_in' in session:
            return f(*args, **kargs)
        else:
            flash("You need to login!!!")
            return redirect(url_for("login"))
    return wrap

@app.route('/', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No Selected File')
            return redirect(request.url)
        if file:
            print(file.filename)
            filename = secure_filename(file.filename) 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=""))
    return render_template("main.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']
        user = Users.query.filter_by(email=username).first()
        if user:
            if password == user.password:
                session['logged_in'] = True
                user.accessDate = datetime.today()
                db.session.commit()
                return redirect(url_for('upload_file'))
            else:
                flash("Incorrect password")
        else:
            flash("Username doesn't exist")
        return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/logout')
def login_out():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run()
