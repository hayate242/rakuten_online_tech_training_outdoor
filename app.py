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


@app.route('/api/category', methods=['GET'])
def categorySearch():
    category = request.args.get('category')
    hits = request.args.get('hits')
    data = rakuten.item_Search_API(category, hits)
    return jsonify(data)


@app.route('/api/ranking', methods=['GET'])
def rankingSearch(hits):
    ranking = request.args.get("geneId")
    data = rakuten.ranking_API(ranking, hits)
    return jsonify(data)
