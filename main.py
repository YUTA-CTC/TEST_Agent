import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello! 私はCloud Runで動くシンプルなエージェントです。"

@app.route("/chat", methods=["POST"])
def chat():
    # ここに後でAIのAPIを繋げることができます
    data = request.get_json()
    message = data.get("message", "何も言っていませんね")
    return jsonify({"response": f"あなたが言ったこと: {message}"})

if __name__ == "__main__":
    # Cloud Runが指定するポートで起動
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)