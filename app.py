from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask import Flask
from flask import request
from flask import render_template
import requests
import rakutenAPI as rakuten
import json
from flask import jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

bootstrap = Bootstrap(app)
fa = FontAwesome(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exercise')
def exercise():
    return render_template('today.html')


@app.route('/recipe')
def recipe():
    return render_template('today.html')


@app.route('/api/category', methods=['GET'])
def categorySearch():
    category = request.args.get('category')
    data = rakuten.item_Search_API(category)
    return jsonify(data)
