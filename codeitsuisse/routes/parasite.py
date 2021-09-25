import logging
import json
import requests

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    for i in range(20):
        result = request.get_json()[i].get("room")
        logging.info("data sent for evaluation {}".format(result))
        a = request.get_json()[i].get("grid")
        logging.info("data sent for evaluation {}".format(a))
        b = request.get_json()[i].get("interestedIndividuals")
        logging.info("data sent for evaluation {}".format(b))
    return "result"

