from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# Load ChromaDB
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# Load Local LLM
llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0
)

print("=" * 50)
print("SupportGPT is Ready!")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    # Retrieve relevant documents
    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI Customer Support Assistant.

Answer ONLY using the information provided in the CONTEXT.

If the answer is not found in the context, reply exactly:

I don't have enough information.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = llm.invoke(prompt)

    print("\nSupportGPT:")
    print(response.content)