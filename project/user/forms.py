
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from project.models import Companies

class RegisterForm(FlaskForm):
    email = TextField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirmPassword', validators=[DataRequired()])
    company = SelectField('company', coerce=int)
    #location = TextField('location')
    #assemblyLine = TextField('assemblyLine')