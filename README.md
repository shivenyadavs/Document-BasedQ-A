# 📄 Document Based Q&A Chatbot (RAG)

This project is a Document-Based Question Answering system that allows users to upload a PDF and ask questions from it using a chat-style interface. It uses Retrieval Augmented Generation (RAG) with a local LLM powered by Ollama.
## 🛠 Tech Stack
- Python
- Streamlit (Frontend)
- LangChain
- FAISS (Vector Database)
- HuggingFace Embeddings
- Ollama (Llama3 model)
- NVIDIA GPU -RTX 4050

## ✨ Features
- Chat-style user interface
- Ask questions from a PDF document
- Uses Retrieval Augmented Generation (RAG)
- Local LLM using Ollama (no API key required)
- GPU acceleration supported
- Fast and accurate answers from document

## ⚙️ How It Works (Architecture)

1. PDF document is loaded using PyPDFLoader
2. Text is split into chunks
3. Each chunk is converted into embeddings using HuggingFace embeddings
4. Embeddings are stored in FAISS vector database
5. When user asks a question:
   - Relevant chunks are retrieved from FAISS
   - Retrieved text is passed to the LLM (Ollama - Llama3)
   - Final answer is generated





## 📂 Folder Structure

Document-BasedQA/
│
├── app.py
├── data/
│   └── sample.pdf
├── requirements.txt
├── README.md
└── .gitignore


## 🚀 Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/document-based-qa.git
cd document-based-qa
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3.Install Ollama and pull model:
```bash
ollama pull llama3:3b
```
4.Run the application:
```bash
py -3.12 -m streamlit run app.py
```
5. Sample Questions
```bash
## 💬 Sample Questions
- What is a computer network?
- Explain LAN and WAN
- What is DNS?
- Difference between Internet and WWW
- Explain network topologies
```


