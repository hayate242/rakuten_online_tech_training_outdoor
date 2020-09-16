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
    hits=request.args.get('hits')
    data = rakuten.item_Search_API(category,hits)
    return jsonify(data)
@app.route('/api/ranking', methods=['GET'])
def rankingSearch():
    ranking = request.args.get("genreId")
    hits=request.args.get('hits')
    data = rakuten.ranking_API(ranking,hits)
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)