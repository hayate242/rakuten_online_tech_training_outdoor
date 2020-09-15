from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/exercise')
def exercise():
    return render_template('today.html') 

@app.route('/recipe')
def recipe():
    return render_template('today.html') 