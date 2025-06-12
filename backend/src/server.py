"""
Server which sends the data to the client, all requests follow the same logic
but have different endpoints, to make it easier and more strucutred.
"""

from flask import jsonify, request, redirect, url_for, Flask as fk
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from http import HTTPStatus
from datetime import datetime, timedelta
from utility import get_path, get_key
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
app.config['SECRET_KEY'] = get_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = generate_password_hash(data["password"])

    if User.query.filter_by(username=username).first():
        return jsonify(error="invalid_request"), HTTPStatus.BAD_REQUEST

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Created user"}), HTTPStatus.OK

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        today = datetime.utcnow().date()

        if user.last_login_at == today:
            pass  # Already logged in today
        elif user.last_login_at == today - timedelta(days=1):
            user.login_streak += 1
        else:
            user.login_streak = 1

        user.last_login_at = today
        db.session.commit()

        login_user(user)
        return jsonify({
            "message": "Logged in successfully",
            "login_streak": user.login_streak
        }), HTTPStatus.OK

    return jsonify({"error": "Invalid credentials"}), HTTPStatus.UNAUTHORIZED

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out user"}), HTTPStatus.OK

@app.route("/stats")
@login_required
def stats():
    # Implement some kind of see stats data or something.
    pass

# Enable CORS for live-server, since it works as a proxy I guess.
CORS(app, origins=["http://127.0.0.1:5500"])

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
    with app.app_context():
        db.create_all()
