from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask import Flask
from flask import render_template

app = Flask(__name__)

bootstrap = Bootstrap(app)
fa = FontAwesome(app)


@app.route('/')
def index():
    title = 'Healthcare'
    return render_template('index.html', Title=title)


@app.route('/exercise')
def exercise():
    title = "Today's 5 min Exercise"
    return render_template('exercise.html', Title=title)


@app.route('/recipe')
def recipe():
    title = "Today's 5 min Recipe"
    return render_template('recipe.html', Title=title)
