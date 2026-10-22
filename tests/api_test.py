import requests

user_name = input("Githubユーザー名を入力してください: ")


url = "https://api.github.com/users/" + user_name

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("ユーザー名:", data["login"])
    print("名前:", data["name"])
    print("公開リポジトリ数:", data["public_repos"])
    print("フォロワー数:", data["followers"])
    print("フォロー数:", data["following"])


else:
    print("ユーザーが見つかりませんでした")
    print("ステータスコード:", response.status_code)
        