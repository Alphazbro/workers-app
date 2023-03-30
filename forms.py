from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import data_required, Email, EqualTo

class registrationform(FlaskForm):
  username=StringField('username',validators=[data_required()])
  email=StringField('email',validators=[Email(),data_required()])
  password=PasswordField('password',validators=[data_required()])
  confirmpassword=PasswordField('password',validators=[data_required(), EqualTo(password)])
  submit=SubmitField('Register')

class loginform(FlaskForm):
  email=StringField('email',validators=[Email(),data_required()])
  password=PasswordField('password',validators=[data_required()])
  remember=BooleanField('remember me')
  submit=SubmitField('Login')
