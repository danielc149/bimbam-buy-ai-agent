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

# memoria simple en backend
chat_history = []

@app.get("/")
def home():
    return {"message": "Santos Pegasus AI Agent activo"}

@app.get("/ask")
def ask(question: str):
    # guardar pregunta
    chat_history.append({"role": "user", "content": question})

    # preguntar al agente
    result = qa.invoke({"query": question})
    answer = result["result"]

    # guardar respuesta
    chat_history.append({"role": "assistant", "content": answer})

    return {
        "answer": answer,
        "history": chat_history
    }

# ✅ interfaz tipo chat estilo simple
@app.get("/chat", response_class=HTMLResponse)
def chat():
    return """
    <html>
        <head>
            <title>Santos Pegasus AI</title>
        </head>
        <body>
            <h1>💬 Santos Pegasus AI Agent</h1>

            <input id="question" type="text" placeholder="Escribe tu pregunta" style="width:300px;">
            <button onclick="sendQuestion()">Enviar</button>

            <div id="chatbox" style="margin-top:20px;"></div>

