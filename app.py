from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask import Flask
from flask import request
from flask import render_template
import requests
import rakutenAPI as rakuten
import json
from flask import jsonify

from models.models import Categories, Videos, Video_items

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

bootstrap = Bootstrap(app)
fa = FontAwesome(app)

@app.route('/')
def index():
    title = 'Healthcare'
    categories = Categories.query.all()
    return render_template('index.html', Title=title, categories=categories)


@app.route('/exercise')
def exercise():
    title = "Today's 5 min Exercise"
    videos = Videos.query.filter_by(Type='exercise').all()
    video_items = Video_items.query.filter_by(video_id='exercise').all()
    return render_template('exercise.html', Title=title, videos=videos, video_items=video_items)


@app.route('/recipe')
def recipe():
    title = "Today's 5 min Recipe"
    videos = Videos.query.filter_by(Type='recipe').all()
    video_items = Video_items.query.filter_by(video_id='recipe').all()
    return render_template('recipe.html', Title=title, videos=videos, video_items=video_items)


@app.route('/api/category', methods=['GET'])
def categorySearch():
    category = request.args.get('category')
    hits = request.args.get('hits')
    data = rakuten.item_Search_API(category, hits)
    return jsonify(data)


@app.route('/api/ranking', methods=['GET'])
def rankingSearch():
    ranking = request.args.get("genreId")
    hits = request.args.get('hits')
    data = rakuten.ranking_API(ranking, hits)
    return jsonify(data)
