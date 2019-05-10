from .forms import RegisterForm
from flask import Blueprint, render_template, request, redirect, url_for
from project import app, db
from project.models import Companies, Users

user_blueprint = Blueprint(
    'register', __name__,
    template_folder='templates'
)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    companies = Companies.query.all()
    regForm = RegisterForm(request.form)
    regForm.company.choices= [(c.id, c.companyName) for c in Companies.query.all()]
    if request.method == 'POST':
        if regForm.validate_on_submit():
            print('form validated')
            print(request.form['email'], request.form['password'], request.form['company'])
            user = Users(request.form['email'], request.form['password'], request.form['company'])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login.login'))
        else:
            print('form NOT validated')
    return render_template('register.html', form=regForm, companies=companies)