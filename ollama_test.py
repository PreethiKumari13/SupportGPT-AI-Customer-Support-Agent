from langchain_ollama import ChatOllama

print("Connecting to Ollama...")

llm = ChatOllama(
    model="qwen2.5:0.5b",
    temperature=0

)

response = llm.invoke("Introduce yourself in one sentence.")

print("\nAI Response:")
print(response.content)