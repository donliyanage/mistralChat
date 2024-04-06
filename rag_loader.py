# rag_loader.py

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def generate_rags(ragid: int = 0):
    # Load multiple files
    if ragid == 0:
        folder = os.getcwd().replace("chat", "") + '/data/'

    loaders = [PyPDFLoader(os.path.join(folder, fn)) for fn in os.listdir(folder)]

    all_documents = []

    for loader in loaders:
        print('Loading raw document...' + loader.file_path)
        raw_documents = loader.load()

        print('Splitting text...')
        text_splitter = CharacterTextSplitter(
            separator=' ',
            chunk_size=1000,
            chunk_overlap=0,
            length_function=len,
        )
        documents = text_splitter.split_documents(raw_documents)
        all_documents.extend(documents)

    return all_documents
