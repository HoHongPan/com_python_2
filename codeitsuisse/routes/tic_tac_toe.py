import logging
import json
import pprint
from websocket import create_connection

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tic-tac-toe', methods=['POST'])
def tic_tac_toe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    id = data.get("battleId")
    url = 'https://cis2021-arena.herokuapp.com/tic-tac-toe/start/' + id
    logging.info("uri {}".format(url))
    ws = create_connection(url)
    print("Receiving...")
    result = ws.recv()
    print("Received '%s'" % result)
    ws.close()
    return json.dumps(url)
