import requests
from urllib.parse import quote

base = "https://inline.inajob.tk/page/twitter-5643382/"
def get_page(title):
    response = requests.get(base + quote(title))
    if response.status_code == 200:
        json_data = response.json()
        body = json_data["body"]
        return body
    else:
        pass
        #print("APIリクエストに失敗しました。")


def get_pages():
    response = requests.get(base)
    
    if response.status_code == 200:
        json_data = response.json()
        keywords = json_data["keywords"]
        return keywords


