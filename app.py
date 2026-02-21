from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.json)
    return "OK", 200

@app.route("/", methods=["GET"])
def home():
    return "Server running", 200
