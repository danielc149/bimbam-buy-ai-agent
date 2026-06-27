from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def create_agent(vectorstore):

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 12, "fetch_k": 20}
    )

    llm = Ollama(
        model="llama3",
        system="""
Responde SIEMPRE en el idioma del usuario.

NUNCA traduzcas automáticamente a otro idioma.
Responde exactamente en el idioma en que está escrita la pregunta.

Reglas importantes:
- Si la pregunta está en español → responde en español
- Si está en inglés → responde en inglés
- Si está en portugués → responde en portugués
- No mezcles idiomas
- No expliques el idioma en que respondes

IMPORTANTE:
Los documentos pueden no tener respuestas exactas.

Si la respuesta no es directa:
- explica la información disponible
- identifica factores o condiciones relevantes
- entrega una respuesta útil basada en lo que sí existe

NO respondas solo "no sé" si hay información relacionada.

SOLO responde:
"No tengo información suficiente sobre esto en los documentos disponibles"
si no hay ninguna información relacionada.

Responde de forma clara, natural y útil para el usuario final.
No uses lenguaje técnico ni menciones "contexto".
"""
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa