# LoL Quotes Bot

Pythonで作成した、League of Legends向けのDiscord Botです。

最初はチャンピオンのセリフをランダムに表示するローカルBotとして作成し、その後Discord Botへ発展させました。

現在は、JSONによるセリフデータ管理に加えて、GitHub API・Riot Games APIとの連携にも対応しています。

Riot Games APIを利用して、Riot IDからLeague of Legendsのソロランク情報を取得し、Discord Embedで表示できます。

---

## 概要

このBotはPython学習を目的として制作しています。

開発を進めながら、以下の内容を学習・実装しました。

- Pythonの基本文法
- JSONファイルの読み込み
- Discord Botの作成
- 外部APIとの連携
- HTTPステータスコードによるエラー処理
- `.env` を利用した秘密情報の管理
- Git / GitHubによるバージョン管理
- 関数を使ったコード整理
- Discord Embedによる表示

---

## 主な機能

### LoLセリフ機能

```text
!quote チャンプ名
```

指定したチャンピオンの登録セリフから、ランダムで1つ表示します。

```text
!quote ガレン
```

表示例：

```text
デマーシア！
```

---

### 全チャンピオンからランダム表示

```text
!quote random
```

登録されているチャンピオンからランダムで1体を選び、そのチャンピオンのセリフを表示します。

表示例：

```text
ガレン: デマーシア！
```

---

### セリフ一覧表示

```text
!quote list チャンプ名
```

指定したチャンピオンに登録されているセリフを一覧で表示します。

表示例：

```text
ガレンの登録セリフ一覧

1. デマーシア！
2. 我が剣にかけて！
3. 正義のために！
```

---

### 登録チャンピオン一覧

```text
!champions
```

登録されているチャンピオンと、それぞれのセリフ数を表示します。

表示例：

```text
登録チャンピオン一覧

ヴィエゴ: 4個
イブリン: 4個
カーサス: 4個
ガレン: 3個
ガリオ: 3個
```

---

### 登録数表示

```text
!count
```

登録されているチャンピオン数と、セリフの合計数を表示します。

表示例：

```text
登録チャンプ数: 5体
登録セリフ数: 18個
```

---

## GitHubユーザー情報表示

```text
!github ユーザー名
```

GitHub APIを利用して、指定したユーザーの情報を取得します。

表示する情報：

- ユーザー名
- 名前
- 公開リポジトリ数
- フォロワー数
- フォロー数

使用例：

```text
!github octocat
```

存在しないユーザー名が入力された場合は、ユーザーが見つからないことを表示します。

---

## LoLソロランク表示

```text
!rank ゲーム名#タグ
```

Riot Games APIを利用して、指定したプレイヤーのソロランク情報を取得します。

使用例：

```text
!rank ゲーム名#JP1
```

取得・表示する情報：

- ランクティア
- ディビジョン
- LP
- 勝利数
- 敗北数
- 勝率

表示例：

```text
LoL Solo Rank

ランク
PLATINUM IV

LP
42

勝利
254

敗北
235

勝率
51.9%
```

ランク情報はDiscord Embedで表示します。

また、IRON・BRONZE・SILVER・GOLD・PLATINUM・EMERALD・DIAMOND・MASTER・GRANDMASTER・CHALLENGERなど、ランクティアに応じてEmbedのカラーが変化します。

---

## Riot APIのエラー処理

Riot Games APIのHTTPステータスコードに応じて、Discord上に異なるエラーメッセージを表示します。

```text
401 : APIキーが無効、または期限切れ
403 : APIへのアクセスが拒否された
404 : Riot IDが見つからない
429 : APIへのアクセス回数が多すぎる
```

ソロランクをプレイしていないプレイヤーの場合は、

```text
このプレイヤーはソロランクをしていません
```

と表示します。

---

## その他のコマンド

### ヘルプ

```text
!help
```

使用可能なコマンド一覧を表示します。

### あいさつ

```text
こんにちは
```

Botがあいさつを返します。

---

## 使用技術

- Python
- discord.py
- JSON
- python-dotenv
- requests
- GitHub API
- Riot Games API
- Git
- GitHub
- GitHub Desktop
- Visual Studio Code
- PowerShell

---

## ファイル構成

```text
Python_Practice
│
├─ champion_discord_bot.py
├─ champion_bot.py
├─ quotes.json
├─ api_test.py
├─ riot_test.py
├─ README.md
├─ .gitignore
├─ .env
│
└─ Practice_old/
```

---

## ファイルの役割

### champion_discord_bot.py

Discord Bot本体です。

Discord上のメッセージを読み取り、各コマンドに応じて処理を行います。

主な機能：

```text
!quote
!quote random
!quote list
!champions
!count
!help
!github
!rank
こんにちは
```

GitHub API・Riot Games APIへのアクセスもこのファイルから行います。

Botの機能が増えてコードが長くなったため、処理ごとに関数へ分割しています。

---

### champion_bot.py

Discord Bot化する前に作成した、ローカル環境用のLoLセリフBotです。

PowerShell上でメニューを選択して使用します。

Pythonの基本文法やJSONの扱いを学習するために作成しました。

---

### quotes.json

チャンピオン名とセリフを保存しているJSONファイルです。

Bot本体とセリフデータを分離することで、Pythonコードを変更せずにチャンピオンやセリフを追加しやすくしています。

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

---

### api_test.py

GitHub APIを学習するために使用したテストファイルです。

主に以下を学習しました。

```text
requests.get()
response.status_code
response.json()
```

APIから取得したJSONデータの中から必要な情報を取り出す練習にも使用しました。

---

### riot_test.py

Riot Games APIを学習するために使用したテストファイルです。

Riot IDからPUUIDを取得し、そのPUUIDを利用してLeague of Legendsのランク情報を取得する処理をテストしました。

Discord Botへ実装する前に、API単体で正常に動作するか確認するために使用しています。

---

### .env

Discord Bot TokenとRiot API Keyを保存します。

```text
DISCORD_TOKEN=自分のDiscord Bot Token
RIOT_API_KEY=自分のRiot API Key
```

秘密情報を含むため、GitHubにはアップロードしません。

---

### .gitignore

GitHubにアップロードしないファイルを指定します。

```text
.env
__pycache__/
*.pyc
```

`.env` に保存したDiscord TokenやRiot API KeyがGitHubに公開されないようにしています。

---

### Practice_old

Python学習途中で作成した練習用ファイルを保存しています。

メインで使用するファイルと、学習用ファイルを分けるために作成しました。

---

## セットアップ方法

### 1. 必要なライブラリをインストール

PowerShellで以下を実行します。

```powershell
py -m pip install discord.py python-dotenv requests
```

---

### 2. `.env` を作成

プロジェクトフォルダ内に `.env` ファイルを作成します。

```text
DISCORD_TOKEN=自分のDiscord Bot Token
RIOT_API_KEY=自分のRiot API Key
```

実際のTokenやAPI KeyをREADMEやソースコードへ直接書かないようにします。

---

### 3. Botを起動

PowerShellでプロジェクトフォルダへ移動します。

```powershell
cd Desktop\Python_Practice
```

Botを起動します。

```powershell
py champion_discord_bot.py
```

以下のようなメッセージが表示されれば起動成功です。

```text
Botがログインしました
```

Botを停止する場合は、

```text
Ctrl + C
```

を押します。

---

## 工夫した点

### JSONでセリフデータを管理

最初はPythonコード内に直接セリフを書いていましたが、途中から `quotes.json` に分離しました。

これにより、Bot本体を大きく変更せずにセリフを追加できます。

---

### 外部APIとの連携

GitHub APIとRiot Games APIの2種類の外部APIを利用しています。

自分で用意したデータだけでなく、外部サービスからリアルタイムで情報を取得してDiscordへ表示できるようにしました。

---

### Riot IDからランク情報を取得

Riot Games APIでは、

```text
Riot ID
↓
PUUID
↓
ランク情報
```

という流れでデータを取得しています。

複数のAPIを組み合わせて1つの機能を作る経験ができました。

---

### 勝率を計算

Riot Games APIから取得した勝利数と敗北数を使い、

```text
勝率 = 勝利数 ÷ 総試合数 × 100
```

で勝率を計算しています。

---

### Discord Embedを使用

ランク情報を通常のテキストではなく、Discord Embedで表示しています。

ランクティアに応じてEmbedカラーを変更することで、情報を見やすくしました。

---

### 関数によるコード整理

機能追加によって `on_message` 内のコードが長くなったため、処理を関数へ分割しました。

例えば、以下のような処理を別の関数として管理しています。

```text
Riotアカウント情報の取得
ランク情報の取得
ソロランク情報の検索
勝率計算
ランクEmbedの作成
GitHubユーザー情報の取得
GitHub表示文の作成
セリフ一覧の作成
ランダムセリフ取得
登録チャンピオン一覧作成
登録数表示
ヘルプ表示
```

これにより、Bot本体の処理を読みやすくしました。

---

### `.env` を使った秘密情報管理

Discord TokenやRiot API Keyをコードへ直接書かず、`.env` から読み込んでいます。

`.gitignore` を利用し、秘密情報がGitHubへアップロードされないようにしています。

---

## 苦労した点

### Pythonのインデント

Pythonではインデントによって処理の所属が決まります。

特に、

```text
if
elif
else
for
```

を組み合わせた処理では、インデントの位置によって意図しない動作になることがありました。

---

### 変数名・関数名の違い

Pythonでは1文字でも違うと別の変数として扱われます。

例：

```text
quote / quotes

win / wins

rank_url / rank_ulr

discord.Color / discord.color
```

エラーメッセージを確認しながら修正しました。

---

### APIのURL

APIではURLが少し違うだけでも正常にアクセスできません。

Riot Games APIの実装では、URLのスペルや余分なスペースなどによって通信エラーが発生しました。

APIを使用する際はURLを正確に指定する必要があることを学びました。

---

### HTTPステータスコード

APIから正常なデータが返ってくるとは限らないため、

```python
response.status_code
```

を確認し、成功・失敗によって処理を分ける必要がありました。

---

### APIキーの期限

Riot GamesのDevelopment API Keyには期限があるため、期限切れになるとAPIへアクセスできなくなります。

APIキー更新後は `.env` を更新し、Botを再起動する必要があることを学びました。

---

## 学んだこと

このBotの制作を通して、主に以下を学びました。

```text
Pythonの基本文法
変数
if / elif / else
for
list
dict
def
return
JSON
random.choice()
ファイル読み込み
Discord Bot
async / await
外部API
requests
HTTPステータスコード
JSONレスポンス
.env
Git / GitHub
commit / push
コードの関数化
Discord Embed
エラーの読み方・デバッグ
```

---

## 現在使用できるコマンド

```text
こんにちは

!quote チャンプ名
!quote random
!quote list チャンプ名

!champions
!count
!help

!github ユーザー名

!rank ゲーム名#タグ
```

---

## 今後追加したい機能

- フレックスランク情報の表示
- Riot Games APIを利用したLoL機能の追加
- 登録チャンピオン・セリフの追加
- Discord上からセリフを登録する機能
- Botをクラウド上で常時稼働させる
- コードをさらに整理し、必要に応じてファイルを分割する
- Discord上での表示をさらに改善する

---

## 今後の目標

現在は、

```text
Python
↓
JSON
↓
Discord Bot
↓
GitHub API
↓
Riot Games API
↓
エラー処理
↓
関数化
↓
Discord Embed
```

まで実装しました。

今後はBotをクラウド上で常時稼働させ、自分のPCを起動していない状態でも利用できるようにすることを目標としています。

さらにRiot Games APIを利用した機能を追加し、League of Legendsに特化したDiscord Botとして発展させていきます。

---

## 注意

このBotはPython・API・Discord Bot開発の学習目的で制作しています。

Discord Bot TokenやRiot API Keyなどの秘密情報は `.env` に保存し、GitHubにはアップロードしないようにしています。
