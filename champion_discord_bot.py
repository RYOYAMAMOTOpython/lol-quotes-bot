import os
import json
import random
import requests
import discord
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# .envからのDiscord botのトークを取得する
TOKEN = os.getenv("DISCORD_TOKEN")
RIOT_API_KEY = os.getenv("RIOT_API_KEY")

# quotes.jsonからセリフデータを読み込む
with open("quotes.json" , "r" , encoding="utf-8") as file:
    quotes=json.load(file)

# BotがDiscordのメッセージ内容を読めるようにする
intents = discord.Intents.default()
intents.message_content = True

#Discord Bot本体を作成
client = discord.Client(intents=intents)

def find_solo_rank(rank_data):
    for rank_info in rank_data:
        if rank_info["queueType"] == "RANKED_SOLO_5x5":
            return rank_info
    return None

def get_riot_account(game_name, tag_line, headers):
    account_url = (
        "https://asia.api.riotgames.com"
        + "/riot/account/v1/accounts/by-riot-id/"
        + game_name
        + "/"
        + tag_line

    )
    account_response = requests.get(account_url, headers=headers)
    return account_response

def get_rank_data(puuid, headers):
    rank_url = (
        "https://jp1.api.riotgames.com"
        + "/lol/league/v4/entries/by-puuid/"
        + puuid

    )
    rank_response = requests.get(rank_url, headers=headers)
    return rank_response

def calculate_win_rate(wins, losses):
    total_games = wins + losses
    return (wins / total_games) * 100

def get_github_user(user_name):
    url = "https://api.github.com/users/" + user_name
    response = requests.get(url)

    return response

# Botが起動してDiscordにログインしたときに実行される
@client.event
async def on_ready():
    print("Botがログインしました")
    print(client.user)

def create_rank_message(solo_rank):
    wins = solo_rank["wins"]
    losses = solo_rank["losses"]

    win_rate = calculate_win_rate(wins, losses)

    rank_message = ""
    rank_message += "ソロランク: " + solo_rank["tier"] + " " + solo_rank["rank"] + "\n"
    rank_message += "LP: " + str(solo_rank["leaguePoints"]) + "\n"
    rank_message += "勝利: " + str(wins) + "\n"
    rank_message += "敗北: " + str(losses) + "\n"
    rank_message += "勝率: " + str(round(win_rate,1)) + "%"
    
    return rank_message

def create_github_message(data):
    github_message = ""
    github_message += "ユーザー名: " + data["login"] + "\n"
    github_message += "名前: " + str(data["name"]) + "\n"
    github_message += "公開リポジトリ数: " + str(data["public_repos"]) + "\n"
    github_message += "フォロワー数: " + str(data["followers"]) + "\n"
    github_message += "フォロー数: " + str(data["following"])

    return github_message

def create_quote_list(champ_name, quotes):
    quote_list = champ_name + "の登録セリフ一覧\n"

    number = 1

    for quote in quotes[champ_name]:
        quote_list = quote_list + str(number) + ". " + quote + "\n"
        number = number + 1

    return quote_list

def get_random_quote(quotes):
    random_champ = random.choice(list(quotes.keys()))
    quote = random.choice(quotes[random_champ])

    return random_champ + ": " + quote

def get_champion_quote(champ, quotes):
    quote = random.choice(quotes[champ])

    return quote

def create_champion_list(quotes):
    champion_list = "登録チャンピオン一覧\n"

    for champ in quotes:
        champion_list = champion_list + champ + " : " + str(len(quotes[champ])) + "個\n"

    return champion_list    

def create_count_message(quotes):
    total_quotes = 0

    for champ in quotes:
        total_quotes = total_quotes + len(quotes[champ])

    count_message = "登録チャンプ数: " + str(len(quotes)) + "体/n"
    count_message = count_message + "登録セリフ数: " + str(total_quotes) + "個"

    return count_message

def create_help_message():
    help_message = ""
    help_message += "使えるコマンド一覧\n"
    help_message += "!quote チャンプ名 : ランダムでセリフを表示\n"
    help_message += "!quote random : 全チャンプからランダムでセリフを表示\n"
    help_message += "!quote list チャンプ名 : 指定したチャンプの登録セリフ一覧を表示\n"
    help_message += "!champions : 登録チャンプ一覧を表示\n"
    help_message += "!count : 登録チャンプ数とセリフ数を表示\n"
    help_message += "!github ユーザー名 : GitHubユーザー情報を表示\n"
    help_message += "!rank ゲーム名#タグ : LoLのソロランク情報を表示\n"
    help_message += "こんにちは : あいさつを返す"

    return help_message
# Discordにメッセージが送られた時に実行される
@client.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == client.user:
        return
    

    #挨拶に反応する
    if message.content == "こんにちは":
        await message.channel.send("こんにちは!")

    # !quote チャンプ名でランダムなセリフを返す
    
    if message.content.startswith("!quote"):
        champ = message.content.replace("!quote", "").strip()

        if champ.startswith("list"):
            champ_name =champ.replace("list ", "").strip()

            if champ_name in quotes:
                quote_list = create_quote_list(champ_name, quotes)
                

                await message.channel.send(quote_list)

            else:
                await message.channel.send("登録されてないチャンピオンです")        
            
        elif champ == "random":
            random_quote = get_random_quote(quotes)

            await message.channel.send(random_quote)

        elif champ in quotes:
            quote = get_champion_quote(champ, quotes)
            await message.channel.send(quote)

        else:
            await message.channel.send("登録されていないチャンピオンです")



    #登録されているチャンプ一覧を返す
    if message.content =="!champions":
        champion_list = create_champion_list(quotes)
        
        await message.channel.send(champion_list)    

    # 登録チャンプ数と登録セリフ数を返す
    if message.content == "!count":
        count_message = create_count_message(quotes)
        
        await message.channel.send(count_message)    
    # 使えるコマンド一覧を返す
    if message.content == "!help":
        help_message = create_help_message()
    
        

        await message.channel.send(help_message)
    
    if message.content.startswith("!github"):
        user_name = message.content.replace("!github", "").strip()

        if user_name == "":
            await message.channel.send("使い方: !github ユーザー名\n例: !github RYOYAMAMOTOpython")
            return
        

        response = get_github_user(user_name)

        if response.status_code == 200:
            data = response.json()

            github_message = create_github_message(data)

            await message.channel.send(github_message)


        else:
            await message.channel.send("Githubユーザーが見つかりませんでした")

    if message.content.startswith("!rank"):
        riot_id = message.content.replace("!rank", "").strip()

        if riot_id == "":
            await message.channel.send("使い方: !rank ゲーム名#タグ")
            return

        if "#" not in riot_id:
            await message.channel.send("タグまで入力してください\n例: !rank 名前#JP1")
            return


        game_name, tag_line = riot_id.rsplit("#", 1)

        print("ゲーム名:", game_name)
        print("タグ:", tag_line)

        
        headers = {
            "X-Riot-Token" :RIOT_API_KEY

    
        }

        account_response = get_riot_account(game_name, tag_line, headers)


        print("アカウント取得:", account_response.status_code)

        if account_response.status_code == 200:
            account_data = account_response.json()

            puuid = account_data["puuid"]

            rank_response = get_rank_data(puuid, headers)

            print("ランク取得:", rank_response.status_code)

            if rank_response.status_code == 200:
                rank_data = rank_response.json()

                print([rank_info.get("queueType") for rank_info in rank_data])

                solo_rank = find_solo_rank(rank_data)
                    
                    
                
                        
                        

                if solo_rank is not None:
                    rank_message = create_rank_message(solo_rank)

                    await message.channel.send(rank_message)

                else:
                    await message.channel.send("このプレイヤーはソロランクをしていません"


                    )
                
            elif rank_response.status_code == 401:
                await message.channel.send(
                    "Riot APIキーが無効です、期限切れの可能性があります\n"
                    "Developer Portalで新しいAPIキーに更新してください"

                )
                
                        

            elif rank_response.status_code == 429:
                await message.channel.send(
                    "Riot APIへのアクセス回数が多すぎます\n"
                    "少し時間を空けてからもう一度試してください"

                )
                        
                        
            elif rank_response.status_code == 403:
                await message.channel.send(
                    "ランク情報へのアクセスが拒否されました\n"
                    "APIキーやURLを確認してください"

                )
            else:
                await message.channel.send(
                    "ランク情報の取得に失敗しました\n"
                    + "ステータスコード: "
                    + str(rank_response.status_code)

                )

        elif account_response.status_code == 401:
            await message.channel.send(
                "Riot APIキーが無効か、期限切れの可能性があります\n"
                "Developer Portalで新しいAPIキーに更新してください")

        elif account_response.status_code ==404:
            await message.channel.send(
                "Riot IDが見つかりませんでした\n"
                "ゲーム名とタグを確認してください")

        elif account_response.status_code == 429:
            await message.channel.send(
                "Riot APIへのアクセス回数が多すぎます\n"
                "少し時間をあけてからもう一度試してください"

            )
        elif account_response.status_code == 403:
            await message.channel.send(
                "Riot APIへのアクセスが拒否されました\n"
                "APIキーやURLを確認してください"

            )
        else:
            await message.channel.send(
                "アカウント情報の取得に失敗しました\n"
                + "ステータスコード: "
                + str(account_response.status_code)
            
            )


    

client.run(TOKEN)