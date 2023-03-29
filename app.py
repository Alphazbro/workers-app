from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
