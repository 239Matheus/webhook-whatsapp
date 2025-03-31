from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "matheus123"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return str(challenge)
        return "Token inválido", 403

    if request.method == "POST":
        data = request.json
        print("📥 Mensagem recebida:")
        print(data)
        return jsonify(status="Mensagem recebida com sucesso"), 200

if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
