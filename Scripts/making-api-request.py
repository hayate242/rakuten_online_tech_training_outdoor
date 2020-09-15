import requests
import json


response = requests.get("https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20140222?format=json&genreId=559887&applicationId=1018661814203004669")
print(response.json())