# LoL Quotes Bot

Pythonで作成した、League of LegendsのチャンピオンセリフBotです。

Discord上でコマンドを入力すると、`quotes.json` に登録されたチャンピオンのセリフをランダムで表示したり、登録されているセリフ一覧を確認したりできます。

また、GitHub APIと連携し、GitHubユーザー情報を取得する機能も追加しています。

## 概要

このBotは、Pythonの学習を目的として作成しました。

最初はローカル環境で動く簡単なセリフBotとして作成し、その後、Discord Botとして動作する形に発展させました。

現在は、JSONファイルを使ったデータ管理、Discord Botのコマンド処理、外部API連携などを実装しています。

## 主な機能

* `!quote チャンプ名` で指定したチャンピオンのセリフをランダム表示
* `!quote random` で全チャンピオンからランダムにセリフを表示
* `!quote list チャンプ名` で指定したチャンピオンの登録セリフ一覧を表示
* `!champions` で登録チャンピオン一覧とセリフ数を表示
* `!count` で登録チャンピオン数と登録セリフ数を表示
* `!help` で使えるコマンド一覧を表示
* `!github ユーザー名` でGitHubユーザー情報を表示
* `こんにちは` に反応して返事をする
- `!rank ゲーム名#タグ` でLeague of Legendsのソロランク情報を表示

## 使用技術

* Python
* discord.py
* JSON
* python-dotenv
* requests
* GitHub API
* Git / GitHub
* GitHub Desktop
- Riot Games API

## コマンド一覧

### LoLランク情報表示

```text
!rank ゲーム名#タグ

表示例:ソロランク: PLATINUM IV
LP: 1
勝利: 254
敗北: 235

### 指定チャンピオンのランダムセリフ表示

```text
!quote ガレン
```

指定したチャンピオンに登録されているセリフの中から、ランダムで1つ表示します。

表示例：

```text
デマーシア！
```

### 全チャンピオンからランダムセリフ表示

```text
!quote random
```

登録されている全チャンピオンの中からランダムで1体を選び、そのチャンピオンのセリフをランダムで表示します。

表示例：

```text
ガレン: デマーシア！
```

### 指定チャンピオンのセリフ一覧表示

```text
!quote list ガレン
```

指定したチャンピオンに登録されているセリフを一覧で表示します。

表示例：

```text
ガレンの登録セリフ一覧
1. デマーシア！
2. 我が剣にかけて！
3. 正義のために！
```

### 登録チャンピオン一覧表示

```text
!champions
```

登録されているチャンピオン一覧と、チャンピオンごとのセリフ数を表示します。

表示例：

```text
登録チャンピオン一覧
ヴィエゴ : 4個
イブリン : 4個
カーサス : 4個
ガレン : 3個
ガリオ : 3個
```

### 登録数表示

```text
!count
```

登録チャンピオン数と、登録セリフ数を表示します。

表示例：

```text
登録チャンピオン数: 5体
登録セリフ数: 18個
```

### GitHubユーザー情報表示

```text
!github RYOYAMAMOTOpython
```

GitHub APIからユーザー情報を取得し、Discord上に表示します。

表示する情報は以下の通りです。

* ユーザー名
* 名前
* 公開リポジトリ数
* フォロワー数
* フォロー数

表示例：

```text
ユーザー名: RYOYAMAMOTOpython
名前: ...
公開リポジトリ数: ...
フォロワー数: ...
フォロー数: ...
```

存在しないGitHubユーザー名を入力した場合は、ユーザーが見つからないことを表示します。

### ヘルプ表示

```text
!help
```

使用できるコマンド一覧を表示します。

### あいさつ

```text
こんにちは
```

Botがあいさつを返します。

表示例：

```text
こんにちは!
```

## ファイル構成

```text
Python_Practice
├ champion_discord_bot.py
├ champion_bot.py
├ quotes.json
├ api_test.py
├ README.md
├ .gitignore
├ .env
└ Practice_old
```

## ファイルの役割

### champion_discord_bot.py

Discord Bot本体です。

Discord上のメッセージを読み取り、以下のコマンドに反応します。

* `!quote`
* `!champions`
* `!count`
* `!help`
* `!github`
* `こんにちは`

`quotes.json` からセリフデータを読み込み、コマンドに応じてDiscordへ返信します。

また、`requests` を使ってGitHub APIへアクセスし、GitHubユーザー情報を取得します。

### champion_bot.py

ローカル環境で動く練習用Botです。

Discordには接続せず、PowerShell上でメニュー形式のLoLセリフBotとして動作します。

主にPythonの基礎学習のために作成しました。

### quotes.json

チャンピオン名とセリフを保存するデータファイルです。

Bot本体のコードとセリフデータを分けることで、セリフやチャンピオンを追加しやすくしています。

例：

```json
{
    "ヴィエゴ": [
        "王は帰った",
        "イゾルデのために",
        "我が王国は滅びぬ",
        "破滅を受け入れろ"
    ],
    "ガレン": [
        "デマーシア！",
        "我が剣にかけて！",
        "正義のために！"
    ]
}
```

### api_test.py

API学習用の練習ファイルです。

GitHub APIにアクセスし、ユーザー情報を取得する練習に使用しました。

このファイルでは、以下の内容を学習しました。

* `requests.get()` で外部APIにアクセスする
* `response.status_code` で通信結果を確認する
* `response.json()` でJSONデータをPythonで扱える形にする
* `data["login"]` のように必要な情報を取り出す
* 存在しないユーザー名を入力した場合のエラー処理を行う

### .env

Discord Botのトークンを保存するファイルです。

セキュリティ上、GitHubにはアップロードしません。

例：

```text
DISCORD_TOKEN=自分のBotトークン
```

### .gitignore

GitHubにアップロードしないファイルを指定するためのファイルです。

このプロジェクトでは、以下のように設定しています。

```text
.env
__pycache__/
*.pyc
```

`.env` にはBotトークンが入っているため、必ずGitHubにアップロードしないようにしています。

### Practice_old

学習途中で作成した練習用ファイルをまとめているフォルダです。

作品として使うメインファイルと、練習用ファイルを分けるために作成しました。

## セットアップ方法

### 1. 必要なライブラリをインストール

PowerShellで以下を実行します。

```powershell
py -m pip install discord.py python-dotenv requests
```

### 2. `.env` ファイルを作成

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
```

Botを停止する場合は、PowerShellで `Ctrl + C` を押します。

## 工夫した点

### 1. セリフデータをJSONで管理した

最初はPythonファイルの中に直接セリフを書いていましたが、途中から `quotes.json` に分けました。

これにより、Bot本体のコードを大きく変更しなくても、チャンピオンやセリフを追加できるようになりました。

### 2. 複数のコマンドを実装した

単にセリフを返すだけでなく、以下のような複数のコマンドを追加しました。

* 指定チャンピオンのランダムセリフ表示
* 全チャンピオンからのランダム表示
* 指定チャンピオンのセリフ一覧表示
* 登録チャンピオン一覧表示
* 登録数表示
* ヘルプ表示

これにより、Discord上で使いやすいBotになるようにしました。

### 3. 外部APIと連携した

`requests` を使ってGitHub APIにアクセスし、GitHubユーザー情報を取得する機能を追加しました。

これにより、自作データを返すだけでなく、外部サービスから取得したデータをDiscordに表示できるようになりました。

### 4. `.env` で秘密情報を管理した

Discord Botのトークンをコードに直接書かず、`.env` に保存しました。

また、`.gitignore` を使って `.env` をGitHubにアップロードしないようにしました。

### 5. GitHubで作品として管理した

GitHub Desktopを使って、変更内容をcommit / pushしながら開発しました。

コードを変更したあと、動作確認を行い、GitHubに反映する流れを学びました。

## 苦労した点

### 1. Pythonのインデント

Pythonでは、インデントによって処理の所属が決まります。

`if`、`elif`、`else` の位置がずれると、意図しない動作やエラーが発生しました。

特に、`!quote random` や `!quote list` の処理を追加する際に、インデントの位置を何度も確認しました。

### 2. 変数名の違い

Pythonでは、変数名が1文字でも違うと別物として扱われます。

例：

```text
quotes と "quotes" は別物
quote と quotes は別物
message.content と message.conntent は別物
```

この違いによって、エラーが発生することを学びました。

### 3. JSONの書き方

JSONでは、カンマの位置やダブルクォーテーションの使い方が重要です。

チャンピオンやセリフを追加する際に、JSONの形式が崩れないように注意しました。

### 4. APIのエラー処理

GitHub APIに存在しないユーザー名を送った場合、`404` が返ってきます。

そのため、`response.status_code` を確認し、成功した場合と失敗した場合で処理を分ける必要がありました。

## 学んだこと

* PythonでDiscord Botを作る方法
* `discord.py` を使ったメッセージ処理
* `if / elif / else` による条件分岐
* `for` 文を使った一覧表示
* `len()` を使った件数の取得
* `random.choice()` を使ったランダム表示
* `json.load()` を使ったJSONファイルの読み込み
* `.env` を使った秘密情報の管理
* `.gitignore` を使った除外設定
* `requests` を使った外部APIアクセス
* GitHub APIからJSONデータを取得する方法
* ステータスコードによるエラー処理
* GitHub Desktopを使ったcommit / push
* READMEを書いて作品内容を説明する方法

## 現在できること

現在のBotでは、Discord上で以下の操作ができます。

```text
こんにちは
!quote ヴィエゴ
!quote ガレン
!quote random
!quote list ガレン
!champions
!count
!help
!github RYOYAMAMOTOpython
```

## 今後追加したい機能

* Riot APIと連携する
* `!rank サモナー名` でLeague of Legendsのランク情報を表示する
* 登録チャンピオンをさらに増やす
* Discord上からセリフを追加できる機能を作る
* コマンドのエラー表示をより分かりやすくする
* Botをクラウド上で常時稼働させる

## 今後の目標

最終的には、以下のようなBotに発展させたいです。

```text
PythonでJSONを扱い、
Discord Botとして動作し、
外部APIからデータを取得し、
Discord上で結果を返すBot
```

特に次の目標は、Riot APIと連携してLeague of Legendsのサモナー情報やランク情報を取得することです。

## 注意

このBotは学習目的で作成しています。

Discord Botのトークンなどの秘密情報は `.env` に保存し、GitHubにはアップロードしないようにしています。
