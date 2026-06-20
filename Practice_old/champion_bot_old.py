import random

quotes = {
    "ヴィエゴ":[
        "王は帰った",
        "我が王国は滅びぬ",
        "闇こそ真実",
        "イゾルデはのために",
    
    ],
    
    "イブリン":[
        "愛は痛み",
        "幸せは私のもの",
        "幸せな人って好きよ.....どん底まで落とせるものね",
        "嫌...まだ死なないで",

    ],
    
    "カーサス":[
        "死は私の友",
        "私の歌を聞け",
        "命などただのまやかし",
        "息をすることも愛することも忘れる",

    ],

}

print("登録チャンプ一覧")

for champ in quotes:
    print(champ, ":",len(quotes[champ]),"個")

total_quotes = 0

for champ in quotes :
    
    total_quotes = total_quotes + len(quotes[champ])

print("登録チャンプ:", len(quotes), "体")
print("登録セリフ総数", total_quotes, "個")


champ = input("チャンプの名前を入力してください: ")

if champ in quotes:
    message = random.choice(quotes[champ])
    print(message)
else:
        print("登録されていないチャンピオンです")
