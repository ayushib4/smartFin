# from firebase_admin import firestore, credentials
from inference import InferenceModel
from embedding import EmbeddingModel
from finance import FinanceBro
from transactions import TransactionsInterface

# import firebase_admin

DEFAULT_PROMPTS = [
    "Which purchase was the most wasteful?",
    "Which was the best transaction I made?",
    "How can I save money when buying food?",
    "How can I save money when buying clothing?",
]

# TODO: Setup firebase-credentials-example.json (or ideally put in .env rather than .json)
# firebase_admin.initialize_app(credentials.Certificate("firebase-credentials.json"))
# FIRESTORE_CLIENT = firestore.client()
INFERENCE_MODEL = InferenceModel()
EMBEDDING_MODEL = EmbeddingModel()
FINANCE_BRO = FinanceBro()
TRANSACTIONS_INTERFACE = TransactionsInterface(INFERENCE_MODEL, EMBEDDING_MODEL)
