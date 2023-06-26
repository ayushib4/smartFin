from flask import Flask, request
from server_constants import *
from data_constants import *

import random

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "<h1>smartFin Flask Server!</h1>"


# TODO: Verify FIRESTORE_CLIENT and parse JSON object into `add_transactions`
@app.route("/add-user", methods=["GET"])
def add_user() -> str:
    data = request.get_json()
    user_id = data["user_id"]

    TRANSACTIONS_INTERFACE.add_transactions(
        user_id,
        (doc.to_dict() for doc in FIRESTORE_CLIENT.collection(user_id).stream()),
    )

    return "Added user transactions"


@app.route("/query", methods=["GET"])
def query() -> str:
    return FINANCE_BRO.interview_agent(
        request.args.get("query") or random.choice(DEFAULT_PROMPTS)
    )
