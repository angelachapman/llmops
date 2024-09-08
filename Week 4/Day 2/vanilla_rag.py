import asyncio
from operator import itemgetter

from langchain.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

LOCATION = ":memory:"
VECTOR_SIZE = 1536
EMBEDDING_MODEL = "text-embedding-ada-002"
CHAT_MODEL = "gpt-4o-mini"

SYSTEM_PROMPT_TEMPLATE = """
You are a helpful expert in entrepreneurship. Answer user questions based only on the context below. 
If you don't know, say nah.

Question:
{input}

Context:
{context}
"""

# Function to do vanilla RAG on a bunch of text strings that are already chunked
async def vanilla_rag(texts:list[str], openai_key:str, collection_name:str="PMarca Blogs"):

    qdrant_client = QdrantClient(location=LOCATION) 
    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
    )
    print('created qdrant client')

    embeddings = OpenAIEmbeddings( model=EMBEDDING_MODEL)
    qdrant_vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=collection_name,
        embedding=embeddings  # Embedding function from OpenAI embeddings
    )
    await qdrant_vector_store.aadd_texts(texts)
    retriever = qdrant_vector_store.as_retriever()
    print('populated vector db')

    prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT_TEMPLATE)
    primary_qa_llm = ChatOpenAI(model_name=CHAT_MODEL, temperature=0)

    retrieval_augmented_qa_chain = (
        {"context": itemgetter("input") | retriever, "input": itemgetter("input")}
        | RunnablePassthrough.assign(context=itemgetter("context"))
        | {"response": prompt | primary_qa_llm, "context": itemgetter("context")}
    )
    print('created chain')

    return retrieval_augmented_qa_chain

