from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
    result = qa.invoke({"query": question})
    return {
        "answer": result["result"]
    }

@app.get("/chat", response_class=HTMLResponse)
def chat():
    return """
    <html>
        <head>
            <title>Santos Pegasus AI</title>
        </head>
        <body>
            <h1>💬 Santos Pegasus AI Agent</h1>
            <form action="/ask" method="get">
                <input type="text" name="question" placeholder="Escribe tu pregunta" style="width:300px;">
                <button type="submit">Enviar</button>
            </form>
        </body>
    </html>
    """