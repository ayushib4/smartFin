from langchain import FewShotPromptTemplate, LLMChain, PromptTemplate
import openai
from dotenv import load_dotenv
from os import getenv
from constants import INFERENCE_MODEL
from langchain.chat_models import ChatOpenAI

load_dotenv()

openai.api_key = getenv("OPENAI_API_KEY")
openai.organization = getenv("OPENAI_ORG_ID")


# TODO: Fix prompt and example inputs, see https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/few_shot_examples
class InferenceModel:
    def __init__(
        self,
        model_name=INFERENCE_MODEL,
        prompt_examples: list[dict[str, str]] = [],
    ) -> None:
        self.model_name = model_name

        example_prompt = PromptTemplate(
            input_variables=list(prompt_examples[0].keys()),
            template="Question: {question}\n{answer}",
        )

        prompt = FewShotPromptTemplate(
            examples=prompt_examples,
            example_prompt=example_prompt,
            suffix="Question: {input}",
            input_variables=["input"],
        )

        self.chain = LLMChain(
            llm=ChatOpenAI(temperature=0, model=model_name), prompt=prompt
        )

    def fetch_gpt_response(self, prompt: str) -> str:
        return self.chain.run(prompt)
