# LoL Quotes Bot

Pythonで作成した、League of LegendsのチャンピオンセリフBotです。

Discord上でコマンドを入力すると、`quotes.json` に登録されたチャンピオンのセリフをランダムで返します。

ローカルで動く練習用Botから作り始め、最終的にDiscord Botとして動作する形まで発展させました。

## 概要

このBotは、Discord上で以下のようなコマンドに反応します。

```text
!quote ヴィエゴ
```

上のように入力すると、`quotes.json` に登録されたヴィエゴのセリフ一覧から、ランダムで1つ返します。

また、登録チャンピオン一覧や登録数を確認するコマンドも用意しています。

## 主な機能

* `!quote チャンプ名` でランダムセリフを表示
* `!champions` で登録チャンプ一覧を表示
* `!count` で登録チャンプ数とセリフ数を表示
* `!help` で使えるコマンド一覧を表示
* `こんにちは` に反応して返事をする

## 使用技術

* Python
* discord.py
* JSON
* python-dotenv
* Discord Developer Portal

## ファイル構成

```text
Python_Practice
├ champion_discord_bot.py
├ champion_bot.py
├ quotes.json
├ README.md
├ .gitignore
└ .env
```

## ファイルの役割

### champion_discord_bot.py

Discord Bot本体です。

Discord上のメッセージを読み取り、以下のコマンドに反応します。

* `!quote`
* `!champions`
* `!count`
* `!help`

`quotes.json` からセリフデータを読み込み、コマンドに応じてDiscordへ返信します。

### champion_bot.py

ローカル環境で動く練習用Botです。

Discordには接続せず、PowerShell上でメニュー形式のLoLセリフBotとして動作します。

主に以下の学習のために作成しました。

* `input()`
* `if / else`
* `for` 文
* `len()`
* `random.choice()`
* `while True`
* `def`

### quotes.json

チャンピオン名とセリフを保存するデータファイルです。

Bot本体とセリフデータを分けることで、セリフの追加や編集をしやすくしています。

例：

```json
{
    "ヴィエゴ": [
        "王は帰った",
        "イゾルデのために",
        "我が王国は滅びぬ",
        "破滅を受け入れろ"
    ],
    "イブリン": [
        "闇の中で生きろ",
        "私の刃はお前を貫く",
        "幸せな人って好きよ……どん底に落とせるものね",
        "私の愛は永遠よ"
    ],
    "カーサス": [
        "死はすべてを平等にする",
        "私の歌を聴け",
        "魂を解き放て",
        "滅せよ"
    ]
}
```

### .env

Discord Botのトークンを保存するファイルです。

セキュリティ上、GitHubにはアップロードしません。

```text
DISCORD_TOKEN=自分のBotトークン
```

### .gitignore

GitHubにアップロードしないファイルを指定するためのファイルです。

```text
.env
__pycache__/
*.pyc
```

`.env` にはBotトークンが入っているため、必ず除外します。

## 使い方

### 1. 必要なライブラリをインストール

PowerShellで以下を実行します。

```powershell
py -m pip install discord.py python-dotenv
```

### 2. `.env` を作成

プロジェクトフォルダ内に `.env` ファイルを作成し、Discord Botのトークンを保存します。

```text
DISCORD_TOKEN=自分のBotトークン
```

### 3. Botを起動

PowerShellでプロジェクトフォルダに移動します。

```powershell
cd Desktop\Python_Practice
```

Botを起動します。

```powershell
py champion_discord_bot.py
```

ターミナルに以下のように表示されれば、Botの起動に成功しています。

```text
Botがログインしました
LoL Quotes Bot#xxxx
```

## コマンド一覧

### あいさつ

```text
こんにちは
```

Botが以下のように返します。

```text
こんにちは!
```

### ランダムセリフ表示

```text
!quote ヴィエゴ
```

登録されているチャンピオンの場合、ランダムでセリフを返します。

```text
イゾルデのために
```

登録されていないチャンピオンの場合は、以下のように返します。

```text
登録されてないチャンピオンです
```

### 登録チャンプ一覧

```text
!champions
```

登録されているチャンピオン一覧を返します。

```text
ヴィエゴ
イブリン
カーサス
```

### 登録数表示

```text
!count
```

登録チャンプ数と登録セリフ数を返します。

```text
登録チャンプ数: 3体
登録セリフ数: 12個
```

### ヘルプ表示

```text
!help
```

使えるコマンド一覧を返します。

## 工夫した点

### 1. Bot本体とセリフデータを分離した

最初はPythonファイルの中に直接セリフを書いていました。

途中から `quotes.json` にセリフデータを分けることで、Bot本体のコードとデータを分離しました。

これにより、セリフやチャンピオンを追加するときに、Pythonコード本体を大きく変更しなくてもよくなりました。

### 2. ローカル版BotからDiscord Botへ発展させた

最初はPowerShell上で動くローカルBotを作成しました。

その後、同じ `quotes.json` をDiscord Bot側でも読み込むようにし、Discord上のコマンドに反応できる形に発展させました。

### 3. `.env` でトークンを管理した

Discord Botのトークンをコードに直接書かず、`.env` ファイルに保存しました。

これにより、GitHubにコードを公開する場合でも、トークンが漏れないようにしました。

### 4. `.gitignore` を作成した

`.env` やPythonの自動生成ファイルをGitHubにアップロードしないように、`.gitignore` を作成しました。

### 5. 関数化してコードを整理した

ローカル版Botでは、以下のように処理を関数に分けました。

* `show_menu()`
* `show_quote()`
* `show_champions()`
* `show_counts()`

これにより、コードの役割が分かりやすくなりました。

## 苦労した点

### 1. JSONのカンマの位置

JSONでは、データ同士の間にカンマが必要ですが、最後のデータの後ろにはカンマを付けません。

このルールで何度かエラーが出ました。

### 2. Pythonのインデント

Pythonではインデントによって、処理がどこに所属しているかが決まります。

`if`、`for`、`def` の中でインデントがずれると、`IndentationError` が出ることを学びました。

### 3. 変数名・関数名の打ち間違い

Pythonでは、変数名や関数名が1文字でも違うと別物として扱われます。

例：

```text
quotes と quote は別物
show_quote と show_quotes は別物
Client と client は別物
```

この違いによって、`NameError` や `TypeError` が出ました。

### 4. Discord Developer Portalの設定

Botがメッセージ内容を読むためには、Python側だけでなく、Discord Developer Portal側でも Message Content Intent をオンにする必要がありました。

Python側：

```python
intents.message_content = True
```

Discord Developer Portal側：

```text
Bot
↓
Privileged Gateway Intents
↓
Message Content Intent をオン
↓
Save Changes
```

## 学んだこと

* `input()` でユーザー入力を受け取る方法
* `if / else` で条件分岐する方法
* `for` 文でデータを1つずつ取り出す方法
* `len()` でデータ数を数える方法
* `random.choice()` でランダムに選ぶ方法
* `with open` でファイルを安全に開く方法
* `json.load()` でJSONファイルを読み込む方法
* `while True` と `break` でループ処理を作る方法
* `def` で処理を関数に分ける方法
* `.env` を使って秘密情報を管理する方法
* `.gitignore` でGitHubに上げないファイルを指定する方法
* `discord.py` を使ってDiscord Botを作る方法
* Discord Developer PortalでBotを設定する方法

## 現在できること

現在のBotでは、Discord上で以下の操作ができます。

```text
こんにちは
!quote ヴィエゴ
!quote イブリン
!quote カーサス
!champions
!count
!help
```

## 今後追加したい機能

* 登録チャンピオンを増やす
* `!quote random` で全チャンピオンからランダム表示
* `!addquote チャンプ名 セリフ` でDiscord上からセリフを追加
* エラー文をより分かりやすくする
* Riot APIと連携する
* サモナー情報を取得する
* ランク情報を取得する
* `!rank サモナー名` でランクを表示する
* GitHubに整理して公開する

## 今後の目標

最終的には、以下のような作品に発展させたいです。

```text
PythonでJSONを扱い、
Discord Botとして外部サービスと連携し、
さらにRiot APIからデータを取得して、
Discord上で結果を返すBot
```

## 注意

このBotは学習目的で作成しています。

`.env` に保存しているDiscord Botトークンは公開しないようにします。


