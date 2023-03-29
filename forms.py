from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtfforms.validators import Datarequired, email, equalto


class registrationform(FlaskForm):
  username=StringField('username',validators=[Datarequired])
  email=StringField('email',validators=[email,Datarequired])
  password=PasswordField('password',validators=[Datarequired])
  confirmpassword=PasswordField('password',validators=[Datarequired,equalto(password)])
  submit=SubmitField('Register')

class loginform(FlaskForm):
  email=StringField('email',validators=[email,Datarequired])
  password=PasswordField('password',validators=[Datarequired])
  remember=BooleanField('remember me')
  submit=SubmitField('Login')
