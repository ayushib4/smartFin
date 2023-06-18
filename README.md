# smartFin

With smartFin, we’re trying to take the first step to improving both quality of life and equality by bringing smart financial advice catered to your banking data and financial goals--all through our agent, Mr. Wonderful, fine-tuned to be the best version of a finance bro — personalized for you.

> When in doubt, ask smartFin how one can make smarter financial decisions. Your transaction data and relevant inferences made by GPT is safely stored in smartFin's intelligent database, which is specially prompt-engineered to semantically handpick the most relevant, and often the most regrettable :( transactions. Mr. Wonderful, a generative AI agent, then uses his financial prowess to provide expert insights and advice for your financial peace of mind.

# Contributing

## Architectural Overview
Languages: Python ∙ C++ ∙ Dart ∙ Ruby ∙ Swift

Frameworks and Tools: Firebase ∙ Flutter ∙ Flask ∙ LangChain ∙ OpenAI ∙ HuggingFace ∙ PineCone ∙ Plaid

There are a couple of different key engineering modules that this project can be broken down into.

Ingesting Transaction Data and Computing Inferences We begin by developing querying purchase history periodically from the Plaid API. We then use prompt engineering to extract critical user psychographic data and spending behavior, along with some metrics of how useful the transaction was.

Embedding and Semantic Search We then embed the transaction data and inferences using HuggingFace's embedding model and GPT-4's inference model. Subsequently, we store these embeddings in PineCone and use its semantic search to find the most relevant transactions.

Generative AI Agent We prompt-engineer an agent depending on user's long and short-term goals to generate valid questions if the user doesn't pass in questions to the agent. These questions are used to query PineCone, which LangChain's Generative AI Agent then analyses and provides insight into how spending habits can be improved based on the goals provided by the user.

### Contributing

See `CONTRIBUTING.md`
