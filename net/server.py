from urllib import unquote
from flask import Flask, jsonify, request, json
from crossdomain import crossdomain
from jsonp import support_jsonp
from opening import OpeningFinder

import gevent.wsgi
import gevent.monkey
gevent.monkey.patch_all()

app = Flask(__name__)
opening_finder = OpeningFinder()

listeners = []

def trigger_listeners(response):
    for listener in listeners:
        listener(response)

@app.route("/")
@crossdomain(origin='*')
def hello():
    response = jsonify(hey="yo")
    trigger_listeners("yo")
    return jsonify(response)

@app.route("/opener", methods=['GET', 'OPTIONS'])
@support_jsonp
@crossdomain(origin='*')
def get_opener():
    data = json.loads(unquote(request.query_string.partition('&')[2].partition('&')[0].replace('=', '')))
    cards = data.get('cards')
    kingdom_cards = cards
    openings = opening_finder.find_top_openings(kingdom_cards)
    openings_to_string = ""
    for o in openings:
        openings_to_string += o[0][0] + "/" + o[0][1] + "\n"

    trigger_listeners(openings_to_string)
    response = jsonify(o=openings)
    return response

def register_listener(listener):
    print "registering listener"
    listeners.append(listener)

# fapp.run(host='127.0.0.1',port='5000', 
#         debug = False, ssl_context=('server.crt', 'server.key'))  
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
key_rel_path = "server.nocrypt.key"
crt_rel_path = "server.crt"
key_path = os.path.join(script_dir, key_rel_path)
crt_path = os.path.join(script_dir, crt_rel_path)
# http_server = gevent.pywsgi.WSGIServer(('', 5000), app, keyfile=key_path, certfile=crt_path)
app.debug = True
http_server = gevent.pywsgi.WSGIServer(('', 5000), app)


#  curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"cards": ["Tribute", "Merchant Guild", "Menagerie", "Poor House", "Salvager", "Potion", "Venture", "Forager", "Upgrade", "Chapel", "Silver", "Estate"]}' localhost:5000/opener 
#  curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"cards": "hey"}' localhost:5000/opener 
