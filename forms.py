from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])
    