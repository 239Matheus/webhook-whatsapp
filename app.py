from flask import Flask, request

app = Flask(__name__)

# Defina um token personalizado que você vai usar no painel do Meta
VERIFY_TOKEN = "matheus123"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token_sent = request.args.get("hub.verify_token")
        if token_sent == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token de verificação inválido.", 403

    if request.method == "POST":
        data = request.json
        print("Mensagem recebida:", data)
        return "Mensagem recebida", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
