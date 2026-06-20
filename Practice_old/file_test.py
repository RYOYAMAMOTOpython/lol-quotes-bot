import json
import random

with open("quotes.json", "r" , encoding="utf-8") as file:
    quotes=json.load(file)


champ=input("チャンプの名前を入力してください:")

if champ in quotes:
    message=random.choice(quotes[champ])
    print(message)
    
else:
    print("登録されていないチャンピオンです")

