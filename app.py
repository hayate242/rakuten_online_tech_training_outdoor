from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask import Flask
from flask import render_template
import requests
app = Flask(__name__)

bootstrap = Bootstrap(app)
fa = FontAwesome(app)
appId=1018661814203004669
gID=100938#genre ID of Healthcare items
Item_Search_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
Item_Search_API_serch_param={"format":"json","keyword":"","applicationId":appId}
Item_Search_API_result = requests.get(Item_Search_API_Endpoint,Item_Search_API_serch_param).json()
print(len(Item_Search_API_result["Items"]))
Ranking_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
Ranking_API_serch_param={"applicationId":appId,"geneId":gID}
Ranking_API_result = requests.get(Ranking_API_Endpoint,Ranking_API_serch_param).json()
print(len(Item_Search_API_result["Items"]))

@app.route('/')
def index():
    return render_template('index.html',)


@app.route('/exercise')
def exercise():
    return render_template('today.html')


@app.route('/recipe')
def recipe():
    return render_template('today.html')
