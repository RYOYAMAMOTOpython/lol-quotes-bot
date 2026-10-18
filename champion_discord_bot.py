import os
import json
import random
import requests
import riot_api
import discord
import embeds
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv(override=True)

# .envからのDiscord botのトークを取得する
TOKEN = os.getenv("DISCORD_TOKEN")
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
def get_riot_headers():
    return{
        "X-Riot-Token":RIOT_API_KEY

    }

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

def find_flex_rank(rank_data):
    for queue in rank_data:
        if queue["queueType"] == "RANKED_FLEX_SR":
            return queue

    return None        






def get_github_user(user_name):
    url = "https://api.github.com/users/" + user_name
    response = requests.get(url)

    return response

# Botが起動してDiscordにログインしたときに実行される
@client.event
async def on_ready():
    print("Botがログインしました")
    print(client.user)



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





def create_help_message():
    embed = discord.Embed(
        title="LoL Bot Help",
        color=discord.Color.blue()

    )
    embed.add_field(
        name="Quote Commands",
        value=(
            "!quote <champ>\n"
            "!quote random\n"
            "!quote list <champ>\n"
            "!champions\n"
            "!count"

        ),
        inline=False

    )

    embed.add_field(
        name="Riot Commands",
        value=(
            "!rank <name#tag>\n"
            "!recent <name#tag>\n"
            "!mastery <name#tag>\n"
            "!stats <name#tag>\n"
            "!ingame <name#tag>\n"

            
        ),

    inline=False    
    )

    embed.add_field(
        name="Other",
        value="!github <username>",
        inline=False
    )

    return embed





def split_riot_id(riot_id):
    game_name, tag_line = riot_id.rsplit("#", 1)
    return game_name, tag_line

def get_puuid(game_name, tag_line, headers):
    account_response = riot_api.get_riot_account(
        game_name,
        tag_line,
        headers
    )

    if account_response.status_code == 200:
        account_data = account_response.json()
        return account_data["puuid"]

    return None     

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
        help_embed = embeds.create_help_embed()
        await message.channel.send(embed=help_embed)
    
        
    
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


        game_name, tag_line = split_riot_id(riot_id)

       

        
        
        headers = get_riot_headers()

    
        

        puuid = get_puuid(
            game_name,
            tag_line,
            headers
        )

        if puuid is None:
            await message.channel.send(
                "アカウント情報を取得できませんでした"

            )
            return
        rank_response = riot_api.get_rank_data(
            puuid,
            headers
        )
        if rank_response.status_code == 200:
            rank_data = rank_response.json()

            solo_rank = find_solo_rank(rank_data)
            flex_rank = find_flex_rank(rank_data)
                
                    
                    
                
                        
                        

            if solo_rank is not None:
                rank_embed = embeds.create_rank_embed(solo_rank, flex_rank)

                await message.channel.send(embed=rank_embed)
                    
                    

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

        


    if message.content.startswith("!recent"):
        riot_id = message.content.replace("!recent", "").strip()

        if riot_id == "":
            await message.channel.send("使い方: !recent ゲーム名#タグ")
            return

        if "#" not in riot_id:
            await message.channel.send("タグまで入力してください\n例: !recent 名前#JP1")
            return
 
        game_name, tag_line = split_riot_id(riot_id)

        headers = get_riot_headers()

        puuid = get_puuid(
            game_name,
            tag_line,
            headers
        )
        if puuid is None:
            await message.channel.send(
                "アカウント情報を取得できませんでした"
            )
            return

        match_response = riot_api.get_recent_match_ids(puuid, headers)

        if match_response.status_code == 200:
            match_ids = match_response.json()

            recent_message = "直近5試合\n\n"
            number = 1
                
            wins_count = 0
            losses_count = 0

                
                
            champion_map = riot_api.get_champion_map()

            for match_id in match_ids:
                match_data_response = riot_api.get_match_data(match_id, headers)

                timeline_response = riot_api.get_match_timeline(match_id, headers)

                    

                if timeline_response.status_code == 200:
                    match_data = match_data_response.json()
                        


                    participants = match_data["info"]["participants"]

                    player_data = None
                    for participant in participants:
                        if participant["puuid"] == puuid:
                            player_data = participant
                            break
                                   

                    if player_data is not None:
                        if player_data["win"]:
                            result = "WIN"
                            wins_count = wins_count + 1

                        else:
                            result = "LOSS"
                            losses_count = losses_count + 1
                            
                            timeline_data = timeline_response.json()
                            
                            frames = timeline_data["info"]["frames"]
                            last_frame = frames[-1]

                            participant_id = str(player_data["participantId"])
                        
                            participant_frame = last_frame["participantFrames"][participant_id]
                           

                            

                            
                            
                            game_duration = match_data["info"]["gameDuration"]


                            minions_cs = participant_frame.get("minionsKilled", 0)
                            jungle_cs = participant_frame.get("jungleMinionsKilled",0)

                            cs = minions_cs + jungle_cs

                            

                            game_duration = match_data["info"]["gameDuration"]
                            minutes = game_duration // 60
                            seconds = game_duration % 60

                            team_id = player_data["teamId"]
                            team_kills = 0
                            
                            for participant in participants:
                                if participant["teamId"] == team_id:
                                    team_kills += participant["kills"]

                            if team_kills > 0:
                                kill_participation = (
                                    (player_data["kills"] + player_data["assists"])
                                    / team_kills
                                    *100

                                )
                            else:
                                kill_participation = 0            


                            recent_message +=str(number) + ". " + result + "\n"
                            champion_name = champion_map.get(
                                player_data["championId"],
                                player_data["championName"]

                            )

                            recent_message += "チャンピオン: " + champion_name + "\n"

                            recent_message += "KDA: "
                            recent_message += str(player_data["kills"]) + "/"
                            recent_message += str(player_data["deaths"]) + "/"
                            recent_message += str(player_data["assists"]) + "\n\n"
                            recent_message += "CS: " + str(cs) + "\n"
                        
                            

                            recent_message += "試合時間: " + str(minutes) + "分" + str(seconds) + "秒\n"

                            recent_message += "キル関与率: "
                            recent_message += str(round(kill_participation, 1)) + "%\n\n"


                    number = number + 1

            summary = (
                "直近5試合: "
                + str(wins_count)
                + "勝 "
                + str(losses_count)
                + "敗\n\n"

            )    
            recent_embed = embeds.create_recent_embed(summary, recent_message)


            await message.channel.send(embed=recent_embed)                    





        else:
            await message.channel.send(
                "試合履歴の取得に失敗しました\n"
                + "ステータスコード: "
                +str(match_response.status_code)

            )    

        
    if message.content.startswith("!mastery"):
        riot_id = message.content.replace("!mastery", "").strip()
        if riot_id == "":
            await message.channel.send(
                "使い方: !mastery ゲーム名#タグ"

            )
            return

        game_name, tag_line = split_riot_id(riot_id)

        headers = get_riot_headers()

        puuid = get_puuid(
            game_name,
            tag_line,
            headers
        )
        
        if puuid is None:
            await message.channel.send(
                "アカウント情報を取得できませんでした"

            )
            return


        mastery_response = riot_api.get_mastery_data(puuid, headers)
        
            

        mastery_data = mastery_response.json()
        
        champion_map = riot_api.get_champion_map()
        
        mastery_message = ""
        number = 1

        for mastery in mastery_data[:3]:
            champion_name = champion_map.get(
                mastery["championId"],
                str(mastery["championId"])

            )

            mastery_message += str(number) + ", " + champion_name + "\n"
            mastery_message += "レベル: " + str(mastery["championLevel"]) + "\n"
            mastery_message += "ポイント: " + format(mastery["championPoints"], ",") + "\n\n"

            number = number + 1

        mastery_embed = embeds.create_mastery_embed(
            mastery_message

        )

        await message.channel.send(embed=mastery_embed)    

    if message.content.startswith("!stats"):
        riot_id = message.content.replace("!stats", "").strip()

        if "#" not in riot_id:
            await message.channel.send(
                "使い方: !stats ゲーム名#タグ"

            )
            return

        game_name, tag_line = split_riot_id(riot_id)

        headers = get_riot_headers()

        
        puuid = get_puuid(
            game_name,
            tag_line,
            headers
        )

        if puuid is None:
            await message.channel.send(
                "アカウント情報を取得できませんでした"
            )
            return

        match_response = riot_api.get_recent_match_ids(puuid, headers)

        

        if match_response.status_code == 200:
            match_ids = match_response.json()

            total_kills = 0
            total_deaths = 0
            total_assists = 0
            total_cs = 0
            wins_count = 0
            games_count = 0

            champion_counts ={}
            champion_wins = {}


            for match_id in match_ids:
                match_data_response = riot_api.get_match_data(match_id, headers)

                


                player_data = None

                if match_data_response.status_code == 200:
                    match_data = match_data_response.json()
                    participants = match_data["info"]["participants"]


                    

                    for participant in participants:
                        if participant["puuid"] == puuid:
                            player_data = participant
                            break

                    
                    if player_data is not None:
                        total_kills += player_data["kills"]
                        total_deaths += player_data["deaths"]
                        total_assists += player_data["assists"]
                        champion_id = player_data["championId"]

                        if champion_id in champion_counts:
                            champion_counts[champion_id] += 1

                        else:
                            champion_counts[champion_id] = 1

                        if champion_id not in champion_wins:
                            champion_wins[champion_id] = 0

                        if player_data["win"]:
                            champion_wins[champion_id] += 1
                            wins_count += 1

                        timeline_response = riot_api.get_match_timeline(match_id, headers)    
                
                                    

                if timeline_response.status_code == 200:
                    timeline_data = timeline_response.json()

                    frames = timeline_data["info"]["frames"]
                    last_frame = frames[-1]

                    participant_id = str(player_data["participantId"])

                    participant_frame = last_frame["participantFrames"][participant_id]

                    minions_cs = participant_frame.get("minionsKilled", 0)

                    jungle_cs = participant_frame.get("jungleMinionsKilled", 0)

                    cs = minions_cs + jungle_cs
                    total_cs += cs

                games_count += 1    

            
            if games_count > 0:
                average_kills = total_kills / games_count
                average_deaths = total_deaths / games_count
                average_assists = total_assists / games_count
                average_cs = total_cs / games_count

                win_rate = wins_count / games_count * 100
                losses_count = games_count - wins_count
                if wins_count > losses_count:
                    recent_result = "勝ち越し"
                elif wins_count < losses_count:
                    recent_result = "負け越し"
                else:
                    recent_result = "五分"     

                sorted_champions = sorted(
                    champion_counts.items(),
                    key=lambda item: item[1],
                    reverse=True
                )

                champion_map = riot_api.get_champion_map()

                champion_message = ""
                number = 1

                for champion_id, count in sorted_champions:
                    champion_name = champion_map.get(
                        champion_id,
                        str(champion_id)
                    )
                        

                    champion_win_count = champion_wins.get(champion_id, 0)
                    champion_loss_count = count - champion_win_count
                    champion_win_rate = champion_win_count / count * 100

                    champion_message += (
                        str(number)
                        +". "
                        +champion_name
                        + " "
                        +str(count)
                        + "試合 "
                        +str(champion_win_count)
                        + "勝"
                        +str(champion_loss_count)
                        + "敗 "
                        + "勝率"
                        +str(round(champion_win_rate, 1))
                        + "%\n"


                    )

                    number += 1

                top_champion_count = sorted_champions[0][1]
                top_champion_names =[]

                for champion_id, count in sorted_champions:
                    if count == top_champion_count:
                        champion_name = champion_map.get(
                            champion_id,
                            str(champion_id)
                        )
                        top_champion_names.append(champion_name)

                if len(top_champion_names) == 1:
                    top_champion_message = (
                        top_champion_names[0]
                        +" ("
                        +str(top_champion_count)
                        + "試合) "

                        
                    )
                else:
                    top_champion_message = (
                        " / " .join(top_champion_names)
                        + " (各"
                        +str(top_champion_count)
                        + "試合) "
                    )            

                


                stats_embed = embeds.create_stats_embed(
                    games_count,
                    wins_count,
                    losses_count,
                    recent_result,
                    average_kills,
                    average_deaths,
                    average_assists,
                    average_cs,
                    win_rate,
                    champion_message,
                    top_champion_message
                )

                await message.channel.send(embed=stats_embed)

    if message.content.startswith("!ingame"):
        riot_id = message.content.replace("!ingame", "").strip()

        if "#" not in riot_id:
            await message.channel.send(
                "使い方: !ingame ゲーム名#タグ"
            
            )
            return
        game_name, tag_line = split_riot_id(riot_id)

        headers = get_riot_headers()

        puuid = get_puuid(
            game_name,
            tag_line,
            headers
        )
        if puuid is None:
            await message.channel.send(
                "アカウント情報を取得できませんでした"

            )
            return
        ingame_response = riot_api.get_ingame_data(
            puuid,
            headers
        )

        

        if ingame_response.status_code == 404:
            await message.channel.send(
                "現在試合中ではありません"

            )
            return
        if ingame_response.status_code == 200:
            

            ingame_data = ingame_response.json()
            

            participants = ingame_data["participants"]
            

            my_team_id = None

            for participant in participants:
                if participant["puuid"] == puuid:
                    my_team_id = participant["teamId"]
                    break
            ally_team =[]
            enemy_team = []

            for participant in participants:
                if participant["teamId"] == my_team_id:
                    ally_team.append(participant)
                else:
                    enemy_team.append(participant)

        
        
        champion_map = riot_api.get_champion_map()
        ally_message = ""
        enemy_message = ""
        
        for participant in ally_team:
            champion_name = champion_map.get(
                participant["championId"],
                str(participant["championId"])



            )
            ally_message += champion_name + "\n"
            
        for participant in enemy_team:
            champion_name = champion_map.get(
                participant["championId"],
                str(participant["championId"])

            )

            enemy_message += champion_name + "\n"    

        ingame_embed = embeds.create_ingame_embed(
            ally_message,
            enemy_message
        )
        await message.channel.send(embed=ingame_embed)







               



    

client.run(TOKEN)