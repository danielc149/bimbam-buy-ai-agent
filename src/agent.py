from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def create_agent(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = Ollama(
        model="llama3",
        system="""
Responde siempre en el mismo idioma en el que el usuario hace la pregunta.
Si la pregunta está en español, responde en español.
Si está en inglés, responde en inglés.
Usa el contexto proporcionado para responder de forma clara y precisa.
"""
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa