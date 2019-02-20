
from __future__ import print_function
#from future.standard_library import install_aliases
#install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print(json.dumps(req, indent=4))
    # i select the appropriate logic for the right intent, in this case "book_visit"
    if req["queryResult"]["intent"]["displayName"] == "book_visit":
        string = "Ok, ti cerco un " + req["queryResult"]["parameters"]["medic"] + ". Dove vuoi trovarlo?"
        my_result = {
            "fulfillmentText": string,
            "source": string
        }
    elif req["queryResult"]["intent"]["displayName"] == "book_visit_followup1":
        string = "Ok, che giorno preferisci?"
        my_result = {
            "fulfillmentText": string,
            "source": string
        }
    elif req["queryResult"]["intent"]["displayName"] == "book_visit_followup2":
        string = "Ok, a che ora?"
        my_result = {
            "fulfillmentText": string,
            "source": string
        }
    elif req["queryResult"]["intent"]["displayName"] == "book_visit_followup3":
        print("--------------------------------------------------")
        print(req)
        params = req["queryResult"]["outputContexts"][0]["parameters"]
        string = "Ok, ora cerco un " + params["medic"] + ", a " + str(params["place"]) + ", il giorno " + str(params["day"]) + " alle " + str(params["hour"])

        my_result = {
            "fulfillmentText": string,
            "source": string
        }
    res = json.dumps(my_result, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeWebhookResult(data):
    print ("starting makeWebhookResult...")
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Today the weather in " + location.get('city') + ": " + condition.get('text') + \
             ", And the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)
    #Naresh
    return {

    "fulfillmentText": speech,
     "source": "Yahoo Weather"
    }


@app.route('/test', methods=['GET'])
def test():
    return "Hello there my friend !!"


@app.route('/static_reply', methods=['POST'])
def static_reply():

    req = request.get_json(silent=True, force=True)


    string = "You are awesome !!"
    print(req)
    my_result =  {

    "fulfillmentText": string,
     "source": string
    }

    res = json.dumps(my_result, indent=4)

    r = make_response(res)

    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':

    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')