from fastapi import FastAPI
from src.loader import load_documents
from src.vectorstore import create_vectorstore
from src.agent import create_agent

app = FastAPI()

print("Cargando documentos...")
docs = load_documents()

print("Creando base vectorial...")
db = create_vectorstore(docs)

print("Inicializando agente...")
qa = create_agent(db)

@app.get("/")
def home():
    return {"message": "Santos Pegasus AI Agent activo"}

@app.get("/ask")
def ask(question: str):
    result = qa({"query": question})
    return {
        "answer": result["result"]
    }