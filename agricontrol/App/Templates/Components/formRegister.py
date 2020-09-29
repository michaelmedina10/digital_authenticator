from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SelectField, validators
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    name = StringField("name", validators = [DataRequired()])
    password = PasswordField("Senha")
    password = PasswordField('password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    image = FileField("image", validators = [DataRequired()])
    email = StringField("email",validators = [DataRequired()])
    nivel = SelectField("Nível de acesso", choices=["1","2","3"])
