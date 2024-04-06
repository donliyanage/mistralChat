# llm_handler.py

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from rag_loader import generate_rags

key = ''
def initialize_llm(ragid: int = 1):
    # Load RAG data
    docs = generate_rags(ragid)

    # Using HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings()

    # Using Chroma vector database to store and retrieve embeddings of our text
    db = Chroma.from_documents(docs, embeddings)
    retriever = db.as_retriever(search_kwargs={'k': 2})
    print('Loaded raw document s1...')


    # Specify the model repository ID
    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    # Initialize the HuggingFace Hub
    llm = HuggingFaceHub(
        huggingfacehub_api_token=key,
        repo_id=repo_id,
        model_kwargs={"temperature": 0.74, "max_new_tokens": 300}
    )
    print('Base model loaded...')


    # Create the Conversational Retrieval Chain
    qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever, return_source_documents=True)

    return qa_chain