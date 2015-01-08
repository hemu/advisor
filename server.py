from flask import Flask, jsonify
from crossdomain import crossdomain

app = Flask(__name__)

@app.route("/")
@crossdomain(origin='*')
def hello():
    return jsonify(hey="yo")

@app.route("/opener/<cardA>/<cardB>")
@crossdomain(origin='*')
def getOpener(cardA, cardB):
    return jsonify(cardA=cardA, cardB=cardB)

print jsonify


if __name__ == "__main__":
    app.run()