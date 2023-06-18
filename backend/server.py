from flask import Flask, request
import firebase_admin
from firebase_admin import firestore, credentials
from os import getenv
from dotenv import load_dotenv
from flask import g
import finance_bro
import random

load_dotenv()

app = Flask(__name__)
IP_ADDRESS = getenv("IP_ADDRESS")


@app.route("/trigger-core", methods=["POST"])
def trigger_core_services():
    try:
        data = request.get_json()
        user_id = data["user_id"]
        cred = credentials.Certificate("firebase-credentials.json")
        app = firebase_admin.initialize_app(cred)
        firestore_client = firestore.client()
        coll_ref = firestore_client.collection(user_id)
        docs = coll_ref.stream()
        data = [doc.to_dict() for doc in docs]
        # insert pinecone function
        return "200"
    except Exception as e:
        return {"error": str(e)}, 400

@app.route("/init-agent", methods=["POST"])
def init_agent():
    traits = """ Kevin have a straightforward and practical approach to personal finance, 
    emphasizing disciplined budgeting and prioritizing financial goals to help everyday people make sound spending decisions. 
    Kevin emphasizes the importance of tracking expenses and making informed choices based on long-term financial objectives.
    Kevin has a keen eye for growth and maximizing returns on purchases. 
    """
    status = "providing financial advice based on transactions"
    agent = finance_bro.FinanceBro("Mr. Wonderful", 68, traits, status)
    g.agent = agent
    return "200"

@app.route("agent-observe", methods=["POST"])
def agent_observe():
    question = request.args.get("question")
    random_questions = ["Which purchase was the most wasteful?", 
                        "Which was the best transaction I made?", 
                        "How can I save money when buying food?", 
                        "How can I save money when buying clothing?"
                        ]

    try: 
        if question != "": 
            advice = g.agent.interview_agent(question)
        else: 
            advice = g.agent.interview_agent(random.choice(random_questions))
            
        return advice
    
    except Exception as e: 
        return {"agent is not persisting. Error": str(e)}, 410


if __name__ == "__main__":
    app.run(host=IP_ADDRESS, debug=True)
