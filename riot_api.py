import requests

def get_riot_account(game_name, tag_line,headers):
    account_url = (
        "https://asia.api.riotgames.com"
        + "/riot/account/v1/accounts/by-riot-id/"
        + game_name
        + "/"
        +tag_line

    )

    account_response = requests.get(
        account_url,
        headers=headers

    )

    return account_response

def get_rank_data(puuid, headers):
    rank_url = (
        "https://jp1.api.riotgames.com"
        + "/lol/league/v4/entries/by-puuid/"
        + puuid

    )
    rank_response = requests.get(rank_url, headers=headers)
    return rank_response

def get_recent_match_ids(puuid, headers):
    match_url = (
        "https://asia.api.riotgames.com"
        + "/lol/match/v5/matches/by-puuid/"
        + puuid
        + "/ids?start=0&count=5"

    )

    print(repr(match_url))

    match_response = requests.get(match_url, headers=headers)

    print("recent取得:", match_response.status_code)
    print(match_response.text)


    return match_response

def get_match_data(match_id, headers):
    match_url = (
        "https://asia.api.riotgames.com"
        + "/lol/match/v5/matches/"
        + match_id

    )   

    match_response = requests.get(match_url, headers=headers)
    return match_response

def get_match_timeline(match_id, headers):
    timeline_url = (
        "https://asia.api.riotgames.com"
        + "/lol/match/v5/matches/"
        + match_id 
        + "/timeline"

    )

    timeline_response = requests.get(timeline_url, headers=headers)

    return timeline_response

def get_mastery_data(puuid, headers):
    mastery_url = (
        "https://jp1.api.riotgames.com"
        + "/lol/champion-mastery/v4/champion-masteries/by-puuid/"
        + puuid
        
    )

    mastery_response = requests.get(mastery_url, headers=headers)
    return mastery_response

def get_ingame_data(puuid, headers):
    ingame_url = (
        "https://jp1.api.riotgames.com"
        + "/lol/spectator/v5/active-games/by-summoner/"
        + puuid
    )

    ingame_response = requests.get(ingame_url, headers=headers)

    return ingame_response

def get_champion_map():
    version_response = requests.get(
        "https://ddragon.leagueoflegends.com/api/versions.json"

    )

    latest_version = version_response.json()[0]

    champion_url = (
        "https://ddragon.leagueoflegends.com/cdn/"
        + latest_version
        + "/data/ja_JP/champion.json"

    )


    champion_response = requests.get(champion_url)
    champion_data = champion_response.json()

    champion_map ={}

    for champion in champion_data["data"].values():
        champion_id = int(champion["key"])
        champion_name = champion["name"]

        champion_map[champion_id] = champion_name

    return champion_map