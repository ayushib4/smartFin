import openai
from os import getenv
from constants import INFERENCE_MODEL

openai.organization = getenv("OPENAI_ORG_ID")
openai.api_key = getenv("OPENAI_API_KEY")
openai.Model.list()

response = openai.ChatCompletion.create(
    model=INFERENCE_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain asynchronous programming in the style of the pirate Blackbeard.",
        },
    ],
    temperature=0,
)

print(response["choices"][0]["message"]["content"])
