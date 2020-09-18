from models.database import db_session
import time

"""[categories seeder]
"""
from models.models import Video_items
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
    # "tomato": "pure0124:10000159",
    # "cucumber": "pure0124:10000094",
    # "table salt": "hikaritv:10096785",
    # "avocado": "sumifrujapan:10000054",
    # "red onion": "808seika:10000027"
}

def item_search_api(item_code):
    item_search_api_endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?"
    item_search_api_search_param = {"format": "json", "itemCode": item_code, "applicationId": appId}
    item_search_api_result = requests.get(item_search_api_endpoint, item_search_api_search_param).json()
    return item_search_api_result

exercise = []
for each in exercise_list_of_item_code.keys():
    time.sleep(0.01)
    tmp = item_search_api(exercise_list_of_item_code[each])
    exercise.append([
        tmp['Items'][0]['Item']['mediumImageUrls'][0]['imageUrl'],
        tmp['Items'][0]['Item']['itemName'],
        tmp['Items'][0]['Item']['itemUrl'],
        tmp['Items'][0]['Item']['itemPrice']
    ])

recipe = []
for each in health_list_of_item_code.keys():
    time.sleep(0.01)
    tmp = item_search_api(health_list_of_item_code[each])
    recipe.append([
        tmp['Items'][0]['Item']['mediumImageUrls'][0]['imageUrl'],
        tmp['Items'][0]['Item']['itemName'],
        tmp['Items'][0]['Item']['itemUrl'],
        tmp['Items'][0]['Item']['itemPrice']
    ])

# video items
db_session.add(
    Video_items(
        'exercise',
        exercise[0][0],
        exercise[0][1],
        exercise[0][2],
        exercise[0][3],
        exercise[1][0],
        exercise[1][1],
        exercise[1][2],
        exercise[1][3],
        exercise[2][0],
        exercise[2][1],
        exercise[2][2],
        exercise[2][3],
        exercise[3][0],
        exercise[3][1],
        exercise[3][2],
        exercise[3][3],
        exercise[4][0],
        exercise[4][1],
        exercise[4][2],
        exercise[4][3]
    )
)
db_session.add(
    Video_items(
        'recipe',
        recipe[0][0],
        recipe[0][1],
        recipe[0][2],
        recipe[0][3],
        recipe[1][0],
        recipe[1][1],
        recipe[1][2],
        recipe[1][3],
        recipe[2][0],
        recipe[2][1],
        recipe[2][2],
        recipe[2][3],
        recipe[3][0],
        recipe[3][1],
        recipe[3][2],
        recipe[3][3],
        recipe[4][0],
        recipe[4][1],
        recipe[4][2],
        recipe[4][3]
    )
)

db_session.commit()
