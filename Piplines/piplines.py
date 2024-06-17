import os
from langchain_postgres.vectorstores import PGVector
from langchain_postgres.vectorstores import DistanceStrategy
from LLMs.chat_SparkLLM import get_llm
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import EmbeddingsFilter
from Prompts.gen_prompts import retrieval_qa_chat_prompt
from Prompts.gen_prompts import normal_prompt
from langchain_core.output_parsers import StrOutputParser

PGVECTOR_CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver=os.environ.get("PGVECTOR_DRIVER", ""),
    host=os.environ.get("PGVECTOR_HOST", ""),
    port=int(os.environ.get("PGVECTOR_PORT", "")),
    database=os.environ.get("PGVECTOR_DATABASE", ""),
    user=os.environ.get("PGVECTOR_USER", ""),
    password=os.environ.get("PGVECTOR_PASSWORD", ""),
)
with open('金融词汇内容.txt', encoding='utf8') as file:
    content = file.readlines()
    content = [i.strip() for i in content]

embedding = HuggingFaceEmbeddings(model_name='../acge_text_embedding'
                                  , show_progress=True
                                  , model_kwargs={'device': 'cuda'}
                                  , encode_kwargs={'normalize_embeddings': True})

output_parser = StrOutputParser()


def get_db(strategy_input):
    strategy = DistanceStrategy.COSINE
    if strategy_input == 'EUCLIDEAN':
        strategy = DistanceStrategy.EUCLIDEAN
    elif strategy_input == 'MAX_INNER_PRODUCT':
        strategy = DistanceStrategy.MAX_INNER_PRODUCT

    return PGVector(embeddings=embedding,
                    collection_name='test',
                    connection=PGVECTOR_CONNECTION_STRING,
                    use_jsonb=True,
                    distance_strategy=strategy
                    )


def get_compression_retriever(topK_input, strategy_input):
    return ContextualCompressionRetriever(base_compressor=EmbeddingsFilter(embeddings=embedding, k=topK_input)
                                          , base_retriever=get_db(strategy_input).as_retriever())


def get_RAG_chain(model_input, temperature_input, topK_input, strategy_input):
    combine_docs_chain = create_stuff_documents_chain(get_llm(model_input, temperature_input)
                                                      , prompt=retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(get_compression_retriever(topK_input, strategy_input), combine_docs_chain)
    return retrieval_chain


def get_normal_chain(model_input, temperature_input):
    chain = normal_prompt | get_llm(model_input, temperature_input) | output_parser
    return chain


def simpleRouter(question):
    flag = True
    for i in content:
        if i in question:
            flag = False
            break
    return flag
