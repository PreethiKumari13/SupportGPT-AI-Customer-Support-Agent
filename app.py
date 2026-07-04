import re
import streamlit as st

from tools import get_order, create_ticket

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama


# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="🌸 PixieSupportAI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#FFF8FC,#FFE7F3);
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

.title{
    color:#E75480;
    font-size:46px;
    font-weight:bold;
}

.subtitle{
    color:#666;
    font-size:18px;
}

section[data-testid="stSidebar"]{
    background:#FFEAF5;
}

[data-testid="stChatMessage"]{
    border-radius:18px;
    padding:14px;
    margin-top:10px;
    margin-bottom:10px;
    box-shadow:0px 4px 12px rgba(0,0,0,.08);
}

.pink-card{
    background:white;
    border-radius:18px;
    padding:18px;
    border:2px solid #FFD6E7;
    box-shadow:0px 4px 12px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image("images/robot.png", width=180)

    st.markdown("## 🌸 Pixie")

    st.success("🟢 Online")

    st.markdown("---")

    st.write("### 💖 Features")

    st.write("📚 Knowledge Base")

    st.write("📦 Order Tracking")

    st.write("🎫 Support Tickets")

    st.write("🤖 Local AI")

    st.write("💾 SQLite")

    st.write("⚡ Ollama")

    st.markdown("---")

    st.caption("Made with 💖 by Preethi")


# ---------------- TITLE ---------------- #

col1, col2 = st.columns([1,4])

with col1:
    st.image("images/robot.png", width=140)

with col2:
    st.markdown("<div class='title'>🌸 PixieSupportAI</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Your Cute AI Customer Support Assistant 💖</div>", unsafe_allow_html=True)

st.write("")


# ---------------- LOAD AI ---------------- #

@st.cache_resource
def load_ai():

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

    return db, llm


db, llm = load_ai()


# ---------------- CHAT HISTORY ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("💖 Ask Pixie anything...")
if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Pixie is thinking..."):

            answer = ""

            # ---------------- ORDER LOOKUP ---------------- #

            match = re.search(r"\d{4}", question)

            if "order" in question.lower() and match:

                order = get_order(int(match.group()))

                if order:

                    answer = f"""
🌸 **Order Details**

📦 **Order ID:** {order['order_id']}

👤 **Customer:** {order['customer']}

🛍️ **Product:** {order['product']}

🚚 **Status:** {order['status']}

📅 **Delivery:** {order['delivery']}

💖 Thank you for shopping with PixieSupportAI!
"""

                else:

                    answer = """
❌ Order not found.

Please check your Order ID and try again.
"""

            # ---------------- SUPPORT TICKET ---------------- #

            elif any(
                word in question.lower()
                for word in [
                    "damaged",
                    "broken",
                    "complaint",
                    "issue",
                    "refund",
                    "defective",
                    "not working"
                ]
            ):

                ticket_id = create_ticket(
                    "Preethi",
                    question
                )

                answer = f"""
🎫 **Support Ticket Created Successfully!**

🆔 **Ticket ID:** SUP-{ticket_id}

📌 **Status:** Open

💖 Pixie has sent your issue to our support team.

We will contact you shortly.
"""

            # ---------------- RAG ---------------- #

            else:

                docs = db.similarity_search(
                    question,
                    k=3
                )

                context = "\n\n".join(
                    doc.page_content
                    for doc in docs
                )

                prompt = f"""
You are Pixie, a friendly AI Customer Support Assistant.

Answer ONLY using the context below.

If the answer is not available, reply exactly:

I don't have enough information.

Context:
{context}

Question:
{question}

Answer:
"""

                response = llm.invoke(prompt)

                answer = response.content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
    # ---------------- WELCOME CARD ---------------- #

if len(st.session_state.messages) == 0:

    st.markdown("""
    <div class="pink-card">

    ## 🌸 Welcome to PixieSupportAI 💖

    Hi! I'm <b>Pixie</b>, your cute AI Customer Support Assistant.

    I can help you with:

    📦 Order Tracking

    🚚 Shipping Information

    🔄 Return Policy

    🎫 Support Tickets

    🔐 Password Reset

    📚 Frequently Asked Questions

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💡 Try asking Pixie")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📦 Where is my order 1001?")
        st.info("🚚 How long does shipping take?")
        st.info("📚 What is your shipping policy?")

    with col2:
        st.info("🔄 What is your return policy?")
        st.info("🎫 My laptop is damaged.")
        st.info("🔐 How do I reset my password?")

# ---------------- FOOTER ---------------- #

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr>

<div style="text-align:center; color:#666;">

<h3 style="color:#E75480;">
🌸 PixieSupportAI 💖
</h3>

<p>
Your Cute AI Customer Support Assistant
</p>

<p>
🤖 Qwen &nbsp; • &nbsp;
📚 RAG &nbsp; • &nbsp;
💾 ChromaDB &nbsp; • &nbsp;
🗄️ SQLite &nbsp; • &nbsp;
⚡ Ollama
</p>

<p>
Made with 💖 by <b>Preethi Kumari</b>
</p>

</div>
""", unsafe_allow_html=True)