import requests
appId = 1018661814203004669


def item_Search_API(keyword):
    item_Search_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
    item_Search_API_serch_param = {
        "format": "json", "keyword": keyword, "applicationId": appId}
    item_Search_API_result = requests.get(
        item_Search_API_Endpoint, item_Search_API_serch_param).json()
    return item_Search_API_result


def ranking_API(gID):
    ranking_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
    ranking_API_serch_param = {"applicationId": appId, "geneId": gID}
    ranking_API_result = requests.get(
        ranking_API_Endpoint, ranking_API_serch_param).json()
    return ranking_API_result
