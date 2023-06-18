import openai
import math
import faiss
from dotenv import load_dotenv
from os import getenv
from langchain.chat_models import ChatOpenAI
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import TimeWeightedVectorStoreRetriever
from langchain.vectorstores import FAISS

load_dotenv()

openai.organization = getenv("OPENAI_ORG_ID")
openai.api_key = getenv("OPENAI_API_KEY")

USER_NAME = "Person A"  # The name you want to use when interviewing the agent.
LLM = ChatOpenAI(model_name="gpt-3.5-turbo")

from langchain.experimental.generative_agents import (
    GenerativeAgent,
    GenerativeAgentMemory,
)


def relevance_score_fn(score: float) -> float:
    """
    Converts the euclidean norm of normalized embeddings
    (0 is most similar, sqrt(2) most dissimilar)
    to a similarity function (0 to 1)
    """

    return 1.0 - score / math.sqrt(2)


def create_new_memory_retriever():
    """Create a new vector store retriever unique to the agent."""

    embeddings_model = OpenAIEmbeddings()

    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(
        embeddings_model.embed_query,
        index,
        InMemoryDocstore({}),
        {},
        relevance_score_fn=relevance_score_fn,
    )
    return TimeWeightedVectorStoreRetriever(
        vectorstore=vectorstore, other_score_keys=["importance"], k=15
    )


tommies_memory = GenerativeAgentMemory(
    llm=LLM,
    memory_retriever=create_new_memory_retriever(),
    verbose=False,
    reflection_threshold=8,  # we will give this a relatively low number to show how reflection works
)

# TODO: Allow user input to define the agent
# TODO: Cache agent or run as a temporary instance
tommie = GenerativeAgent(
    name="Tommie",
    age=25,
    traits="anxious, likes design, talkative",
    status="looking for a job",
    memory_retriever=create_new_memory_retriever(),
    llm=LLM,
    memory=tommies_memory,
)

tommie_observations = [
    "Tommie remembers his dog, Bruno, from when he was a kid",
    "Tommie feels tired from driving so far",
    "Tommie sees the new home",
    "The new neighbors have a cat",
    "The road is noisy at night",
    "Tommie is hungry",
    "Tommie tries to get some rest.",
]
for observation in tommie_observations:
    tommie.memory.add_memory(observation)


def interview_agent(agent: GenerativeAgent, message: str) -> str:
    """Help the notebook user interact with the agent."""
    new_message = f"{USER_NAME} says {message}"
    return agent.generate_dialogue_response(new_message)[1]


interview_agent(tommie, "What do you like to do?")
interview_agent(tommie, "What are you looking forward to doing today?")
interview_agent(tommie, "What are you most worried about today?")
