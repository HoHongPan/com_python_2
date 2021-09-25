import logging
import json
import requests

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/tic-tac-toe', methods=['POST'])
def tic_tac_toe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    id = data.get("battleId")
    ab = 'https://cis2021-arena.herokuapp.com/tic-tac-toe/start/' + id
    data_1 = requests.get(ab)
    logging.info("data sent for evaluation {}".format(data_1))
    a = data.get("youAre")
    logging.info("You are {}".format(a))
    return 0



