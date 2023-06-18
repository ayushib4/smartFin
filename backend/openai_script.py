import openai
from os import getenv
from constants import INFERENCE_MODEL

openai.organization = getenv("OPENAI_ORG_ID")
openai.api_key = getenv("OPENAI_API_KEY")
openai.Model.list()


def fetch_gpt_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=INFERENCE_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0,
    )

    return response["choices"][0]["message"]["content"]
