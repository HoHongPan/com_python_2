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
    result = data.get("room")
    logging.info("data sent for evaluation {}".format(result))
    a = data.get("room")
    logging.info("data sent for evaluation {}".format(a))
    return result

