import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# ブラウザでアクセスした時に表示するチャット画面の設計図 (HTML)
HTML_PAGE = """



    
    マイエージェント
    


    🤖 エージェントとチャット
    
    送信
    
    
        エージェントの回答:
        ここに回答が表示されます
    

    


"""

@app.route("/", methods=["GET"])
def home():
    # URLを開いたら、上のチャット画面を表示する
    return HTML_PAGE

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    # 質問の内容に合わせて回答を変えるルール
    if "こんにちは" in message:
        reply = "こんにちは！何かお手伝いできることはありますか？"
    elif "天気" in message:
        reply = "私はクラウドの中にいるので外の天気は見えませんが、きっといい日だと思いますよ！"
    elif "名前" in message:
        reply = "私はCloud Run上で動くシンプルなエージェントです。"
    else:
        reply = f"「{message}」という質問ですね。まだ勉強中なので、もう少し簡単な言葉で話しかけてもらえると嬉しいです！"

    return jsonify({"response": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)