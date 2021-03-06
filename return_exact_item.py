import requests
appId = 1018661814203004669


exercise_list_of_item_code = {
    "yoga map": "cincshop:10001813",
    "sports bra": "yvette:10000013",
    "yoga leggings": "xexymix:10000335",
    "gym shirts": "happysmiles:10000815",
    "sports water bottle": "ringo0812:10000586"
}

health_list_of_item_code = {
    "olive oil": "natuland-asahi:10000829",
    "sunflower oil": "kawasakigroup:10020280",
    "lemon": "mikasasangyou:10000198",
    "cilantro(パクチー)": "808seika:10000103",
    "black pepper": "e-sbfoods:10000538",
    "tomato": "pure0124:10000159",
    "cucumber": "pure0124:10000094",
    "table salt": "hikaritv:10096785",
    "avocado": "sumifrujapan:10000054",
    "red onion": "808seika:10000027"
}


def item_search_api(item_code):
    item_search_api_endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
    item_search_api_search_param = {"format": "json", "itemCode": item_code, "applicationId": appId}
    item_search_api_result = requests.get(item_search_api_endpoint, item_search_api_search_param).json()
    return item_search_api_result


#example
#print(item_search_api(exercise_list_of_item_code["yoga map"]))


