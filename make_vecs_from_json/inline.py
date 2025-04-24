import requests
from urllib.parse import quote

base = "https://inline.inajob.freeddns.org/page/twitter-5643382"
def get_page(title):
    response = requests.get(base + quote(title))
    if response.status_code == 200:
        json_data = response.json()
        body = json_data["body"]
        lastUpdate = int(json_data["meta"].get("lastUpdate", str(1577836800)))
        return body, lastUpdate
    else:
        pass
        #print("APIリクエストに失敗しました。")


def get_pages():
    response = requests.get(base)
    
    if response.status_code == 200:
        json_data = response.json()
        keywords = json_data["keywords"]
        return keywords
    else:
        print("error", response)
        print(response.text)

