from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "seu_token_personalizado"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token de verificação inválido!", 403

    if request.method == "POST":
        data = request.json
        print("Mensagem recebida:", data)
        return "Mensagem recebida", 200

if __name__ == "__main__":
    app.run(port=5000)
