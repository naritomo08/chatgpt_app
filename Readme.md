# chatgpt_app

chatgptに質問をしてみて回答を得るアプリになります。

## Pythonプログラム稼働環境構築

あらかじめpythonインストールを実施していること。
本プログラムはmac/Linuxで動かしてください。

### 初期設定

```bash
git clone https://github.com/naritomo08/chatgpt_app.git
cd chatgpt_app.git
rm -rf .git
python3 -m venv venv
. venv/bin/activate
pip3 list
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
pip3 list

各種Pythonプログラム実施

```

### 仮想環境ログイン

```bash
. venv/bin/activate

このあとに各スクリプトを実施
```

### 仮想環境ログアウト

```bash
deactivate
```

### 仮想環境バックアップ

```bash
pip3 freeze > requirements.txt
```

### 仮想環境リストア

```bash
pip3 install -r requirements.txt
```

### Pythonプログラム稼働方法

ChatGPT APIの入手

以下のコマンドでプログラムを動かす

```bash
cp variable_ref.py variable.py
vi variable.py

以下の””の中にAPIキーを入力する。

api_key = ""

以下のコマンドでChatGPTに質問を投げる。
初回以降は以下のコマンドを動かすだけでいい。

python3 script.py "質問内容"

回答と質問が返答されること。

```

## 今後の展望

```bash
質問・回答について日時と合わせ別途保管するようにしたい。
Web画面で質問・回答が出てくる形にしたい。
Docker上で動かすようにして、K8S上でも稼働するようにしたい。
```
