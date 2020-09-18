import requests
import json
appId = 1018661814203004669


def item_Search_API(keyword, hits):
    item_Search_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
    item_Search_API_serch_param = {
        "format": "json", "keyword": keyword, "applicationId": appId, "hits": hits}
    item_Search_API_result = requests.get(
        item_Search_API_Endpoint, item_Search_API_serch_param).json()
    return item_Search_API_result


def ranking_API(gID, hits):
    ranking_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
    ranking_API_serch_param = {
        "applicationId": appId, "genreId": gID, "hits": hits}
    ranking_API_result = requests.get(
        ranking_API_Endpoint, ranking_API_serch_param).json()
    return ranking_API_result["Items"][0:int(hits)]
