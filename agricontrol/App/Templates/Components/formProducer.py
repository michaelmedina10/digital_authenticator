from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, IntegerField
from wtforms.validators import DataRequired

class ProducerForm(FlaskForm):
    name = StringField("name", validators = [DataRequired()])
    farming = StringField("farming", validators = [DataRequired()])
    annualamount = StringField("annualamount", validators = [DataRequired()])
    pesticide = StringField("pesticide", validators = [DataRequired()])

