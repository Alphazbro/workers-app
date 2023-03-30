from flask import Flask, render_template, url_for,flash, redirect,Request

app = Flask(__name__)
app.config['SECRET_KEY']='JHAHAHAHAHSk'

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
    flash('account created successfully','success')
    return redirect(url_for('home'))
  return render_template('register.html',form=form)

@app.route('/login')
def login():
  form=loginform()
  return render_template('login.html',form=form)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
