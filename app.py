from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask import Flask
from flask import render_template
app = Flask(__name__)

bootstrap = Bootstrap(app)
fa = FontAwesome(app)

@app.route('/')
def hello():
    return render_template('index.html')
