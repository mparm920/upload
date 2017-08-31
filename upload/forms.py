from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = TextField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    email = TextField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirmPassword', validators=[DataRequired()])
    company = TextField('company', validators=[DataRequired()])
    location = TextField('location')
    assemblyLine = TextField('assemblyLine', validators=[DataRequired()])
