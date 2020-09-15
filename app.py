from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template
app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def hello():
    return render_template('index.html')
