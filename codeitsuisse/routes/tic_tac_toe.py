import logging
import json
from aiohttp_sse_client import client as sse_client
import pprint

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def with_urllib3(url):
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False)


@app.route('/tic-tac-toe', methods=['POST'])
def tic_tac_toe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    id = data.get("battleId")
    url = 'https://cis2021-arena.herokuapp.com/tic-tac-toe/start/' + id
    logging.info("uri {}".format(url))
    response = with_urllib3(url)
    async with sse_client.EventSource(
        url
    ) as event_source:
        try:
            async for event in event_source:
                print(event)
        except ConnectionError:
            pass
    return json.dumps(url)
