import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

st.set_page_config(
    page_title="SupportGPT",
    page_icon="🤖"
)

st.title("🤖 SupportGPT")
st.write("AI Customer Support Assistant")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0
)

question = st.text_input("Ask your question")

if st.button("Ask"):

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI Customer Support Assistant.

Answer ONLY using the context.

If the answer isn't available, reply:
I don't have enough information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    st.success(response.content)