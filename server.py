from flask import Flask, jsonify, request
from crossdomain import crossdomain
from opening import OpeningFinder

app = Flask(__name__)
openingFinder = OpeningFinder()

@app.route("/")
@crossdomain(origin='*')
def hello():
    return jsonify(hey="yo")

@app.route("/opener", methods=['POST'])
@crossdomain(origin='*')
def getOpener():
    jsonData = request.get_json()
    kingdomCards = jsonData["cards"]
    return jsonify(o=openingFinder.findBestOpener(kingdomCards))

if __name__ == "__main__":
    app.run()

#  curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"cards": ["Tribute", "Merchant Guild", "Menagerie", "Poor House", "Salvager", "Potion", "Venture", "Forager", "Upgrade", "Chapel", "Silver", "Estate"]}' localhost:5000/opener 
#  curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"cards": "hey"}' localhost:5000/opener 
