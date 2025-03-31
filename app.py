from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "matheus123"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge, 200
        return "Token de verificação inválido.", 403

    if request.method == "POST":
        data = request.json
        print("Mensagem recebida:", data)
        return "Mensagem recebida", 200
