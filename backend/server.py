from flask import Flask, request
import firebase_admin
from firebase_admin import firestore, credentials
from os import getenv
from dotenv import load_dotenv

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

if __name__ == "__main__":
    app.run(host=IP_ADDRESS, debug=True)
