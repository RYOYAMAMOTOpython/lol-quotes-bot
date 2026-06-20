import json
import random



# quotes.json からセリフデータを読み込む
with open("quotes.json", "r" , encoding="utf-8") as file:
    quotes=json.load(file)

#メニューを追加する
def show_menu():
    print("=== LoL セリフBot ===")
    print("1:セリフを聞く")
    print("2:登録チャンプ一覧を見る")
    print("3:登録数を見る")
    print("4:終了")

#登録チャンプ一覧と、チャンプごとのセリフ数を表示する
def show_champions():
    print("登録チャンプ一覧")

    for champ in quotes:
        print(champ, ":" ,len(quotes[champ])), "個"

#登録チャンプ数と登録セリフ総数を表示する
def show_counts():
    total_quotes = 0

    for champ in quotes:
        total_quotes = total_quotes + len(quotes[champ])

    print("登録チャンプ数:", len(quotes), "体")
    print("登録セリフ数:", total_quotes, "個")

#チャンプ名を入力して、ランダムでセリフを表示する        
def show_quotes():
    champ = input("チャンプの名前を入力してください")

    if champ in quotes:
        message = random.choice(quotes[champ])
        print(message)
    else:
        print("登録されていないチャンピオンです")

while True:
    print("=== LoL セリフBot ===")
    print("1: セリフを聞く")
    print("2: 登録チャンプ一覧を見る")
    print("3: 登録数を見る")
    print("4: 終了")

    choice = input("番号を入力してください: ")

    if choice == "1":
        show_quotes()

    elif choice =="2":
        show_champions()

    elif choice == "3":
        show_counts()

    elif choice == "4":
        print("Botを終了します")
        break

    else:
        print("その番号はありません")

    print()