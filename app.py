import os
import streamlit as st
from dotenv import load_dotenv

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🤖 RAG Chatbot")
st.write("Step 1: App Started")

load_dotenv()
st.write("Step 2: .env Loaded")

st.write(os.listdir("data"))

try:
    from langchain_community.document_loaders import TextLoader, PyPDFLoader
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma
    from langchain_google_genai import ChatGoogleGenerativeAI

    load_dotenv()
    import os
    st.write("API Key Loaded:", os.getenv("GOOGLE_API_KEY"))

    st.write("✅ Libraries imported")

    if not os.path.exists("data"):
        st.error("data folder not found")
        st.stop()

    documents = []

    for file in os.listdir("data"):
        path = os.path.join("data", file)

        if file.endswith(".txt"):
            documents.extend(TextLoader(path, encoding="utf-8").load())

        elif file.endswith(".pdf"):
            documents.extend(PyPDFLoader(path).load())

    st.write(f"Loaded {len(documents)} document(s).")

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents,
        embedding,
        persist_directory="vector_db"
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    query = st.text_input("Ask a question")

    if query:
        docs = db.similarity_search(query, k=3)

        context = "\n".join([d.page_content for d in docs])

        response = llm.invoke(
            f"Answer using only this context:\n{context}\n\nQuestion:{query}"
        )

        st.write(response.content)

except Exception as e:
    st.error("Error occurred:")
    st.exception(e)