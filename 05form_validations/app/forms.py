from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, RadioField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, AnyOf, InputRequired

favourite_animals = ["bison", "lion", "leopard", "snake"]

class myForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Data Where")])
    password = PasswordField("Password", validators=[InputRequired("Please Input Password")])
    gender = RadioField("Gender", choices=[("M","M"),("F","F"),("O","O")])
    recap_form = RecaptchaField()
    button = SubmitField("Submit")



