import os
import json
import random
import discord
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# .envからのDiscord botのトークを取得する
TOKEN = os.getenv("DISCORD_TOKEN")

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

        elif champ in quote:
            quote = random.choice(quotes[champ])
            await message.channel.send(quote)

        else:
            await message.channel.send("登録されていないチャンピオンです")



    #登録されているチャンプ一覧を返す
    if message.content =="!champions":
        champion_list =""

        for champ in quotes:
            champion_list = champion_list + champ + "\n"

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
        help_message = help_message + "!champions : 登録チャンプ一覧を表示\n"
        help_message = help_message + "!count : 登録チャンプ数とセリフ数を表示\n"
        help_message = help_message + "こんにちは : あいさつを返す"

        await message.channel.send(help_message)


client.run(TOKEN)