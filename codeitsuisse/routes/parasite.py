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
    result = "[\n"
    for i in range(2):
        result = result + "  {\n"
        c = request.get_json()[i].get("room")
        logging.info("data sent for evaluation {}".format(c))
        result = result + "    \"room\": " + str(c) + ",\n"
        a = request.get_json()[i].get("grid")
        logging.info("data sent for evaluation {}".format(a))
        rows_a = len(a)
        columns_a = len(a[0])
        b = request.get_json()[i].get("interestedIndividuals")
        logging.info("data sent for evaluation {}".format(b))
        rows_b = len(b)
        result = result + "    \"p1\": { "
        for n in range(rows_b):
            result = result +"\""+ b[n] + "\":  "
            if int(a[int(b[n][0])][int(b[n][2])]) != 1:
                result = result + "-1"
            else:
                result = result + "0"
            if n < rows_b-1:
                result = result + ", "
        else:
            result = result + "},\n "

        result = result + "  }\n"
    else:
        result = result + "]"
        print (result)

    return result

