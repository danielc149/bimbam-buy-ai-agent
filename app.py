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
    return {"message": "Bimbam Buy AI Agent activo"}


@app.get("/ask")
def ask(question: str):
    from langchain_community.llms import Ollama
    from src.vectorstore import create_vectorstore
    from src.loader import load_documents

    print(f"Pregunta recibida: {question}")

    # cargar vectorstore
    docs = load_documents()
    db = create_vectorstore(docs)

    retriever = db.as_retriever(search_kwargs={"k": 1})
    results = retriever.invoke(question)

    context = results[0].page_content[:300] if results else ""

    llm = Ollama(
        model="mistral",
        num_predict=60
    )

    prompt = f"""
Contexto:
{context}

Pregunta:
{question}

Responde brevemente:
"""

    response = llm.invoke(prompt)

    print("Respuesta generada")

    return {"answer": response}

@app.get("/chat", response_class=HTMLResponse)
def chat():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Bimbam Buy AI Agent</title>
</head>
<body>
    <h1>💬 Bimbam Buy AI Agent</h1>

    <p style="margin-top:-10px; color:gray; font-size:14px;">
        Asistente inteligente para consultas internas de Bimbam Buy
    </p>

    <input id="question" type="text" placeholder="Escribe tu pregunta..." style="width:300px;">
    <button onclick="sendQuestion()">Enviar</button>

    <div id="response" style="margin-top:20px; font-size:16px;"></div>

    <script>
        async function sendQuestion() {
            let button = document.querySelector("button");
            let question = document.getElementById("question").value;

            button.innerText = "Enviando...";
            button.disabled = true;
            button.style.backgroundColor = "orange";

            let response = await fetch(`/ask?question=${encodeURIComponent(question)}`);
            let data = await response.json();

            let cleanAnswer = data.answer
                .replace(/\\n/g, "<br>")
                .replace(/\\*/g, "")
                .replace(/\\(.*?\\)/g, "");

            document.getElementById("response").innerHTML +=
                "<p><b>Pregunta:</b> " + question + "</p>" +
                "<p><b>Respuesta:</b> " + cleanAnswer + "</p><hr>";

            button.innerText = "Enviar";
            button.disabled = false;
            button.style.backgroundColor = "";

            document.getElementById("question").value = "";
        }
    </script>
</body>
</html>
"""
