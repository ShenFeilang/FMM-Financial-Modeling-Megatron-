import os
from langchain_postgres.vectorstores import PGVector
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

if __name__ == '__main__':

    llm = get_llm('v3.5', 0.5)

    embedding = HuggingFaceEmbeddings(model_name='../acge_text_embedding'
                                      , show_progress=True
                                      , model_kwargs={'device': 'cuda'}
                                      , encode_kwargs={'normalize_embeddings': True})
    db = PGVector(
        embeddings=embedding,
        collection_name='test',
        connection=PGVECTOR_CONNECTION_STRING,
        use_jsonb=True
    )

    def topK_filter(n):
        return EmbeddingsFilter(embeddings=embedding, k=n)

    compression_retriever = ContextualCompressionRetriever(
        base_compressor=topK_filter(3), base_retriever=db.as_retriever()
    )

    combine_docs_chain = create_stuff_documents_chain(llm, prompt=retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(compression_retriever, combine_docs_chain)
    output_parser = StrOutputParser()
    chain = normal_prompt | llm | output_parser


    def simpleRouter(question):
        flag = True
        for i in content:
            if i in question:
                flag = False
                break
        return flag

    def pipline(question, chat_history):
        if simpleRouter(question):
            answer = ''
            length = 0
            for chunk in chain.stream({'input': question, 'chat_history': chat_history}):
                if chunk is not None:
                    print(chunk[length:], flush=True, end='')
                    length = len(answer)

        else:
            print(retrieval_chain.invoke({'input': question, 'chat_history': chat_history})['answer'])


    chat_history = []

    pipline('什么是基金定投？', chat_history)
