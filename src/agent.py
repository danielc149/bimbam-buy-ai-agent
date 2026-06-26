from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def create_agent(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = Ollama(model="llama3")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa
