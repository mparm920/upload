from .forms import RegisterForm
from flask import Blueprint, render_template, request
from project import app
from project.models import Companies

user_blueprint = Blueprint(
    'register', __name__,
    template_folder='templates'
)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        pass
    else:
        registerForm = RegisterForm(request.form)
        companies = Companies.query.all()
        return render_template('register.html', form=registerForm, companies=companies)