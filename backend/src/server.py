"""
Server which sends the data to the client, all requests follow the same logic
but have different endpoints, to make it easier and more strucutred.
"""

from flask import jsonify, request, Flask as fk
from flask_cors import CORS
from http import HTTPStatus
from utility import get_path
import random
import logging
import json

# For debugging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)
app = fk(__name__)
CORS(app, origins=["http://127.0.0.1:5500"]) # Enable CORS for all routes

@app.route('/kanji', methods=['POST'])
@app.route("/hiragana", methods=['POST'])
@app.route("/katakana", methods=['POST'])
def get_kana_data():
    """
    Function which handles return of kana/kanji data, has different endpoints
    to make front-end easier, but has the same logic in the backend.
    """
    data = request.json
    amount = int(data.get('amount'))
    kana_type = data.get('kana_type')

    if not amount or not kana_type:
        logger.debug("Either amount (%s) or kana_type (%s) was incorrectly set",
                     amount, kana_type)
        return jsonify(error="invalid_request"), HTTPStatus.BAD_REQUEST

    if amount < 0:
        logger.debug("Amount was less than 0")
        return jsonify(error="invalid_request"), HTTPStatus.BAD_REQUEST

    try:
        path_to_json = get_path(f"{kana_type}")
    except FileNotFoundError:
        logger.debug("Incorrect kana type was chosen")
        return jsonify(error="invalid_request"), HTTPStatus.BAD_REQUEST

    with open(path_to_json, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
        random.shuffle(raw_data)
        return jsonify(raw_data[:amount]), HTTPStatus.OK

# Uses default ip: http://127.0.0.1:5000
if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)
