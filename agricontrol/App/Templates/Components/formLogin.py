from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators = [DataRequired()])
    password = PasswordField("Senha")
    image = FileField("image", validators = [DataRequired()])
