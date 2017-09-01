                             #!/usr/bin/python3
import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required
from datetime import datetime
from forms import LoginForm, RegisterForm

app = Flask(__name__)

#config
app.config.from_object(os.environ['APP_SETTINGS'])
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from models import *


@login_manager.user_loader
def load_user(user):
    try:
        return Users.query.filter_by(id=user).first()
    except AttributeError:
        return None


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

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
    error = None
    loginForm = LoginForm(request.form)
    if request.method == 'POST':
        if loginForm.validate_on_submit():
            email = request.form['email']
            password = request.form['password']
            user = Users.query.filter_by(email=email).first()
            if user:
                if bcrypt.check_password_hash(user.password, password):
                    login_user(user)
                    user.accessDate = datetime.today()
                    db.session.commit()
                    return redirect(url_for('upload_file'))
                else:
                    error = "Incorrect password"
            else:
                error = "Username doesn't exist"
            #return redirect(url_for('login'))
    return render_template("login.html", form=loginForm, error=error)

@app.route('/logout')
@login_required
def login_out():
    logout_user()
    flash('You are logged out')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    registerForm = RegisterForm(request.form)
    return render_template('register.html', form=registerForm)

if __name__ == "__main__":
    app.run()
