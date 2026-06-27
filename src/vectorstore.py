from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
import os

def create_vectorstore(documents):

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # ✅ SI YA EXISTE EL ÍNDICE → cargarlo (OCI)
    if os.path.exists("faiss_index"):
        print("Cargando vectorstore existente...")
        db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
        )
        return db

    print("Creando vectorstore nuevo...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )

    docs = splitter.split_documents(documents)

    db = FAISS.from_documents(docs, embeddings)

    # ✅ guardamos embeddings (SOLO se genera 1 vez)
    db.save_local("faiss_index")

    return db