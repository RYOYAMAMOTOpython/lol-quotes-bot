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

# Botが起動してDiscordにログインしたときに実行される
@client.event
async def on_ready():
    print("Botがログインしました")
    print(client.user)

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
                quote_list = champ_name + "の登録セリフ一覧\n"

                number = 1

                for quote in quotes[champ_name]:
                    quote_list = quote_list + str(number) + ", " + quote + "\n"
                    number = number + 1

                await message.channel.send(quote_list)

            else:
                await message.channel.send("登録されてないチャンピオンです")        
            
        elif champ == "random":
            random_champ =random.choice(list(quotes.keys()))
            quote = random.choice(quotes[random_champ])
            await message.channel.send(random_champ + ": " + quote)

        elif champ in quotes:
            quote = random.choice(quotes[champ])
            await message.channel.send(quote)

        else:
            await message.channel.send("登録されていないチャンピオンです")



    #登録されているチャンプ一覧を返す
    if message.content =="!champions":
        champion_list ="登録チャンピオン一覧\n"

        for champ in quotes:
            champion_list = champion_list + champ + " : " +str(len(quotes[champ])) + "個\n"

        await message.channel.send(champion_list)    

    # 登録チャンプ数と登録セリフ数を返す
    if message.content == "!count":
        total_quotes = 0

        for champ in quotes:
            total_quotes = total_quotes + len(quotes[champ])

        count_message = "登録チャンプ数: " +str(len(quotes)) +"体\n"
        count_message = count_message + "登録セリフ数: " +str(total_quotes) + "個"

        await message.channel.send(count_message)    
    # 使えるコマンド一覧を返す
    if message.content == "!help":
        help_message = ""
        help_message = help_message + "使えるコマンド一覧\n"
        help_message = help_message + "!quote チャンプ名 : ランダムでセリフを表示\n"
        help_message = help_message + "!quote random : 全チャンプからランダムでセリフを表示\n"
        help_message = help_message + "!quote list : 指定したチャンプの登録セリフ一覧を表示\n"
        help_message = help_message + "!champions : 登録チャンプ一覧を表示\n"
        help_message = help_message + "!count : 登録チャンプ数とセリフ数を表示\n"
        help_message = help_message + "!github ユーザー名 : Githubユーザー情報を表示\n"
        help_message = help_message + "こんにちは : あいさつを返す"
        

        await message.channel.send(help_message)
    
    if message.content.startswith("!github"):
        user_name = message.content.replace("!github", "").strip()

        if user_name == "":
            await message.channel.send("使い方: !github ユーザー名\n例: !github RYOYAMAMOTOpython")
            return
        

        url = "https://api.github.com/users/" + user_name

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            github_message = ""
            github_message = github_message + "ユーザー名" + data["login"] + "\n"
            github_message = github_message + "名前" + str(data["name"]) + "\n"
            github_message = github_message + "公開リポジトリ数: " + str(data["public_repos"]) + "\n"
            github_message = github_message + "フォロワー数: " + str(data["followers"]) + "\n"
            github_message = github_message + "フォロー数: " + str(data["following"])

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

        account_url = (
            "https://asia.api.riotgames.com"
            + "/riot/account/v1/accounts/by-riot-id/"
            + game_name
            + "/"
            + tag_line

        )
        headers = {
            "X-Riot-Token" :RIOT_API_KEY

    
        }

        account_response = requests.get(account_url, headers=headers)

        print("アカウント取得:", account_response.status_code)

        if account_response.status_code == 200:
            account_data = account_response.json()

            puuid = account_data["puuid"]

            rank_url = (
                "https://jp1.api.riotgames.com"
                + "/lol/league/v4/entries/by-puuid/"
                + puuid

            )

            rank_response = requests.get(rank_url, headers=headers)

            print("ランク取得:", rank_response.status_code)

            if rank_response.status_code == 200:
                rank_data =rank_response.json()

                solo_rank = None
                
                for rank_info in rank_data:
                    if rank_info["queueType"] == "RANKED_SOLO_5x5":
                        solo_rank = rank_info
                        break

                if solo_rank is not None:
                    rank_message =""
                    rank_message += "ソロランク: " + solo_rank["tier"] + " " + solo_rank["rank"] + "\n"
                    rank_message += "LP: " + str(solo_rank["leaguePoints"]) + "\n"
                    rank_message += "勝利: " + str(solo_rank["wins"]) + "\n"
                    rank_message += "敗北: " + str(solo_rank["losses"])
                    
                    await message.channel.send(rank_message)

                else:
                    await message.channel.send("このプレイヤーはソロランクをしていません")

            else:
                await message.channel.send(
                    "ランク情報の取得に失敗しました\n"
                    + "ステータスコード: "
                    + str(rank_response.status_code)

                )           
        
        else:
            await message.channel.send(
                "Riot IDが見つからないか、アカウント情報の取得に失敗しました\n"
                + "ステータスコード: "
                + str(account_response.status_code)

            )

client.run(TOKEN)