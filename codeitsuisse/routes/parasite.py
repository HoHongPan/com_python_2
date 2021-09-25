import logging
import json
import requests

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/parastie', methods=['POST'])
def parastie():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    return 0

