import streamlit as st
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA   # works in langchain 0.1.16

st.set_page_config(page_title="Document Q&A System", layout="centered")
st.title("📄 Document Based Q&A System (RAG)")

pdf_path = "data/lecs110.pdf"

if not os.path.exists(pdf_path):
    st.error("❌ Please put lecs110.pdf inside the data folder")
else:
    st.success("✅ PDF file found!")

    with st.spinner("⏳ Processing document, please wait..."):
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings()
        vectorstore = FAISS.from_documents(chunks, embeddings)

        llm = Ollama(model="llama3:8b")

        qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )

    question = st.text_input("Ask a question from the document:")

    if st.button("Get Answer"):
        if question.strip() == "":
            st.warning("⚠️ Please enter a question")
        else:
            with st.spinner("🤖 Generating answer..."):
                answer = qa.run(question)
                st.write("### ✅ Answer:")
                st.write(answer)