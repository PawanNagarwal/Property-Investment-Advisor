import os
from langchain.embeddings import OpenAIEmbeddings     
from langchain.vectorstores import FAISS      
from langchain.text_splitter import CharacterTextSplitter      
from langchain.document_loaders import PyPDFDirectoryLoader             

def setup_rag():
    folder_path ="data"
    loader = PyPDFDirectoryLoader(folder_path)   
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(texts, embeddings)
    return db

def rag_query(db, query):
    docs = db.similarity_search(query)
    return docs[0].page_content
