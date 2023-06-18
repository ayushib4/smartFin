import openai
from dotenv import load_dotenv
from os import getenv
from constants import INFERENCE_MODEL
from langchain.chat_models import ChatOpenAI

load_dotenv()

openai.api_key = getenv("OPENAI_API_KEY")
openai.organization = getenv("OPENAI_ORG_ID")

chat = ChatOpenAI(temperature=0, model=INFERENCE_MODEL)

def _fetch_gpt_response(prompt: str) -> str:
    return chat.predict(prompt)
