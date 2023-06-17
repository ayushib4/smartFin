from os import getenv
import pinecone
from backend.constants import DIMENSIONS

PINECONE_API_KEY = getenv("PINECONE_API_KEY")
PINECONE_ENV = getenv("PINECONE_ENVIRONMENT")

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

pinecone.create_index("example-index", dimension=DIMENSIONS)
metadata_config = {"indexed": ["color"]}
# with the metadata config, pinecone will only filter with the provided metadata field(s)
pinecone.create_index(
    "example-index-2", dimension=1024, metadata_config=metadata_config
)

index = pinecone.Index("example-index")

upsert_response = index.upsert(
    vectors=[
        (
            "vec1",  # Vector ID
            [0.1, 0.2, 0.3, 0.4],  # Dense vector values
            {"genre": "drama"},  # Vector metadata
        ),
        ("vec2", [0.2, 0.3, 0.4, 0.5], {"genre": "action"}),
    ],
    namespace="example-namespace",
)

index_name = "semantic-search"

# only create index if it doesn't exist
if index_name not in pinecone.list_indexes():
    pinecone.create_index(name=index_name, dimension=DIMENSIONS, metric="cosine")

# now connect to the index
index = pinecone.GRPCIndex(index_name)

from tqdm.auto import tqdm

batch_size = 128

for i in tqdm(range(0, len(questions), batch_size)):
    # find end of batch
    i_end = min(i + batch_size, len(questions))
    # create IDs batch
    ids = [str(x) for x in range(i, i_end)]
    # create metadata batch
    metadatas = [{"text": text} for text in questions[i:i_end]]
    # create embeddings
    xc = model.encode(questions[i:i_end])
    # create records list for upsert
    records = zip(ids, xc, metadatas)
    # upsert to Pinecone
    index.upsert(vectors=records)

# check number of records in the index
index.describe_index_stats()

query = "which city has the highest population in the world?"

# create the query vector
xq = model.encode(query).tolist()

# now query
xc = index.query(xq, top_k=5, include_metadata=True)
xc
