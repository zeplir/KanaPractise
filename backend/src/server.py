from flask import jsonify, request, Flask as fk
from flask_cors import CORS
from utility import get_path
import logging

# For debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)
app = fk(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/kanji', methods=['GET'])
def home():
    data = request.json
    amount = data.get('amount')

@app.route("/kana", methods=['GET'])
def hiragana():
    data = request.json
    amount = data.get('amount')
    kana_type = data.get('kana_type')
    if not amount or not kana_type:
        logger.debug("Either amount or kana_type was incorrectly set")
        return jsonify(error="invalid_request"), 400

    try:
        path_to_json = get_path(f"/json/{kana_type}")
        logger.debug("%s", path_to_json)
    except FileNotFoundError:
        logger.debug("Incorrect kana type was chosen")
        return jsonify(error="invalid_request"), 400

    with open(path_to_json, 'r', encoding='utf-8') as f:
        return jsonify(f)

# Uses default ip: http://127.0.0.1:5000
if __name__ == '__main__':
    app.run(debug=True)
