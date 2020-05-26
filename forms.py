from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])

class AddEditReceipeForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired('A recipe title is required'),Length(min=3, max=100)])
    description = StringField('Description')
    