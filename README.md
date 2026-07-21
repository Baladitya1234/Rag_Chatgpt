# 🤖 Local RAG Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot built using **Streamlit**, **LangChain**, **ChromaDB**, and **HuggingFace Embeddings**. The chatbot reads PDF and TXT documents, creates vector embeddings, and retrieves relevant information based on user queries.

---

## 📌 Features

- Upload and use PDF and TXT documents
- Automatic document loading
- Text chunking using RecursiveCharacterTextSplitter
- Vector storage using ChromaDB
- Semantic search with HuggingFace Embeddings
- Simple Streamlit web interface
- No external API required

---

## 📂 Project Structure

```
RAG-Chatbot/
│
├── data/
│   ├── notes.pdf
│   └── sample.txt
│
├── vector_db/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- PyPDF

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/RAG-Chatbot.git

cd RAG-Chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install chromadb
pip install sentence-transformers
pip install pypdf
```

---

## ▶ Run the Project

```bash
python -m streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

## 📖 How It Works

1. Load PDF and TXT documents from the **data** folder.
2. Split documents into smaller chunks.
3. Generate embeddings using HuggingFace.
4. Store embeddings in ChromaDB.
5. Enter a question in the Streamlit interface.
6. Retrieve the most relevant document chunks.
7. Display the retrieved information to the user.

---

## 📸 Sample Questions

- What is Artificial Intelligence?
- Explain Machine Learning.
- Summarize the document.
- What are the key points?
- Explain the first topic.

---

## 📦 Requirements

- Python 3.10 or above
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- PyPDF

---

## 👨‍💻 Author

**Boddepalli Baladitya**

B.Tech Computer Science and Engineering

Vellore Institute of Technology

---

## 📄 License

This project is created for educational and learning purposes.
