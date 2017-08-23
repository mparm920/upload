                             #!/usr/bin/python3
import os
from flask import Flask, request, redirect, url_for, render_template, flash, session
from werkzeug.utils import secure_filename
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

#UPLOAD_FOLDER = '/opt/data'
UPLOAD_FOLDER = '/Users/mparm920/Code/upload/files/'

app = Flask(__name__)
app.secret_key = 'eflex upload page'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///upload.db' 

db = SQLAlchemy(app)

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
        if password == 'admin' and username == 'admin':
            session['logged_in'] = True
            return redirect(url_for('upload_file'))
        return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/logout')
def login_out():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
