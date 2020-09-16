import requests
appId=1018661814203004669
def Item_Search_API(keyword):
    Item_Search_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
    Item_Search_API_serch_param={"format":"json","keyword":keyword,"applicationId":appId}
    Item_Search_API_result = requests.get(Item_Search_API_Endpoint,Item_Search_API_serch_param).json()
    return Item_Search_API_result
def Ranking_API(gID):
    Ranking_API_Endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
    Ranking_API_serch_param={"applicationId":appId,"geneId":gID}
    Ranking_API_result = requests.get(Ranking_API_Endpoint,Ranking_API_serch_param).json()
    return Ranking_API_result