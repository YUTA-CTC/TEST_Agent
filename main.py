import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Cloud Runのエージェントが元気に稼働中です！"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    # ユーザーからのメッセージを受け取る
    message = data.get("message", "")

    # 質問の内容に合わせて回答を変えるルール
    if "こんにちは" in message:
        reply = "こんにちは！何かお手伝いできることはありますか？"
    elif "天気" in message:
        reply = "私はクラウドの中にいるので外の天気は見えませんが、きっといい日だと思いますよ！"
    elif "名前" in message:
        reply = "私はCloud Run上で動くシンプルなエージェントです。"
    else:
        # 知らない質問が来た場合
        reply = f"「{message}」という質問ですね。まだ勉強中なので、もう少し簡単な言葉で話しかけてもらえると嬉しいです！"

    return jsonify({"response": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)