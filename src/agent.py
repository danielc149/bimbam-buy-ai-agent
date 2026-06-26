from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def create_agent(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=False
    )

    return qa
