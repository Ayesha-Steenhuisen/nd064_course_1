from flask import Flask
import json
import logging
import datetime
app = Flask(__name__)

logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)

@app.route("/")
def hello():
    log('/')
    return "Hello World!"

@app.route("/metrics")
def metrics():
    log('/metrics')
    # Deze functie correspondeert met het /metrics pad, (localhost:5000/metrics) en returnt json
    return app.response_class(response = json.dumps({"data":{"UserCount":140, "UserCountActive":23}}), status = 200, mimetype = 'application/json')

@app.route("/status")
def status():
    # json.dumps maakt van een dictionary (zo heet dat in python) een json string, beetje JSON.stringify
    # We geven de response een inhoud (genaamd response), een statuscode en een mimetype (media type) mee
    log('/status')
    return app.response_class(response = json.dumps({"result":"OK - healthy"}), status = 200, mimetype = 'application/json')

def log(endpoint):
    logging.debug(str(datetime.datetime.now()) + ', ' + endpoint + ' endpoint was reached')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
