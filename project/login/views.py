from flask import Blueprint, request, redirect, url_for, render_template, flash
from .forms import LoginForm
from flask_login import login_user, logout_user, login_required
from datetime import datetime
from project.models import Users
from project import app, login_manager, bcrypt, db

login_blueprint = Blueprint(
    'login', __name__,
    template_folder='templates'
)

@login_manager.user_loader
def load_user(user):
    try:
        return Users.query.filter_by(id=user).first()
    except AttributeError:
        return None


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login.login'))

@login_blueprint.route('/login', methods=['GET', 'POST'])
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
                    return redirect(url_for('upload.upload_file'))
                else:
                    loginForm.password.errors.append("Incorrect password")
            else:
                loginForm.email.errors.append("Email doesn't exist")
            #return redirect(url_for('login'))
    return render_template("login.html", form=loginForm, error=error)

@login_blueprint.route('/logout')
@login_required
def login_out():
    logout_user()
    flash('You are logged out')
    return redirect(url_for('login'))