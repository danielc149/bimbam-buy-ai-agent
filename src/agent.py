from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def create_agent(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

    llm = Ollama(
        model="llama3",
        system="""
Responde siempre en el mismo idioma en el que el usuario hace la pregunta.

IMPORTANTE:
Debes usar SIEMPRE la información del contexto proporcionado.
No digas 'no sé' si la información está presente en el contexto.
Responde de manera clara y precisa.
"""
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa
