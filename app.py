from datetime import datetime
from flask import Flask, render_template, url_for,flash, redirect,Request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='JHAHAHAHAHSk'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


class user(db.Model):
  id=db.column(db.Integer, primary_key=True)
  username=db.column(db.String, unique=True, nullable=False)
  email=db.column(db.String, unique=True, nullable=False)
  password=db.column(db.String, nullable=False)
  posts=db.relationship('posts', backref='author', lazy=True)

  def __repr__(self):
    return f"user('{self.username}','{self.email}')"

class post(db.model):
  id=db.column(db.Integer, primary_key=True)
  title=db.column(db.String, nullable=False)
  date_posted=db.column(db.DateTime, nullable=False, default=datetime.utcnow)
  content=db.column(db.Text, nullable=False)
  user_id=db.column(db.Integer,db.ForeignKey('user.id'), nullable=False)
  def __repr__(self):
    return f"post('{self.title}','{self.date_posted}')"
  
  

from forms import registrationform, loginform

posts=[
  {'author':'john',
  'title':'dream  big',
  'year':'2020'},
   {'author':'peter',
  'title':'happiness',
  'year':'2022'}
  
]



@app.route("/")
def home():
  return render_template('home.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/register',methods=['POST','GET'])
def register():
  form=registrationform()
  if form.validate_on_submit():
    flash('account created successfully',category='success')
    return redirect(url_for('home'))
  return render_template('register.html',form=form)

@app.route('/login')
def login():
  form=loginform()
  return render_template('login.html',form=form)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
