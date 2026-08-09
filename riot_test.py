import os
import requests
from dotenv import load_dotenv

load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")

game_name = input("Riot IDの名前を入力してください: ")
tag_line = input("タグを入力してください: ")

url = (
    "https://asia.api.riotgames.com"
    + "/riot/account/v1/accounts/by-riot-id/"
    + game_name
    + "/"
    + tag_line
)

headers = {
    "X-Riot-Token": RIOT_API_KEY
}

response = requests.get(url, headers=headers)

print("ステータスコード:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("ゲーム名:", data["gameName"])
    print("タグ:", data["tagLine"])
    print("PUUID:", data["puuid"])
    rank_url = (
        "https://jp1.api.riotgames.com"
        + "/lol/league/v4/entries/by-puuid/"
        + data["puuid"]
    )

    rank_response = requests.get(rank_url, headers=headers)

    print("ランク取得ステータス:", rank_response.status_code)
rank_data = rank_response.json()

for rank_info in rank_data:
    if rank_info["queueType"] == "RANKED_SOLO_5x5":
        print("ソロランク:", rank_info["tier"], rank_info["rank"])
        print("LP:", rank_info["leaguePoints"])
        print("勝利:", rank_info["wins"])
        print("敗北:", rank_info["losses"])    

