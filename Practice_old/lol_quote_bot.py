print("bot起動")

def get_quote(name):
    quotes = {
        "ヴィエゴ": "王は帰った",
        "ヤスオ": "風を見よ",
        "タロン": "刃は決して嘘をつかない",
    }

    if name in quotes:
        return quotes[name]
    else:
        return "登録されていない"


name = input("チャンプ名前を入力してください: ")

print(get_quote(name))
