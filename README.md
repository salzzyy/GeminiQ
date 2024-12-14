# **QAWithPDF - Question Answering System for PDFs** 📄🤖

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) 
[![Python Version](https://img.shields.io/badge/Python-3.8-green.svg)](https://www.python.org/downloads/)

## **Overview** 🌟
**GEMINIQ** is an innovative **Question Answering System** designed to interact with PDF documents. It uses **Gemini Embeddings** to process PDF content and allows users to ask questions related to the document. With the power of **Generative AI** and **LLama Index**, the system provides real-time, accurate responses based on the content of the uploaded PDFs.

This project allows you to **upload PDFs**, **parse the text**, and **query the content** using natural language.

---

## **Features** ✨

- 📄 **Extracts text** from PDF files with high accuracy.
- 🔄 **Generates embeddings** using **Gemini Embedding** for text processing.
- 🗣️ **Real-time question answering** based on PDF content.
- ⚡ **Uses LLama Index** for efficient indexing and querying.
- 🌍 **Streamlit** interface for easy interaction.

---

### **Core Components**:
1. **PDF Parsing**:  
   We use **PyMuPDF** to extract text content from PDFs in real-time.
   
2. **Text Embedding**:  
   **Gemini Embedding** is used to convert PDF text into vector representations for efficient search and question answering.

3. **Indexing with LLama**:  
   The embedded text is indexed using **LLama Index** for quick and accurate retrieval during querying.

4. **Generative AI Model**:  
   The system employs a **Generative AI** model to process the input questions and provide relevant answers based on the indexed content.

---

## **Getting Started** 🚀

### **Prerequisites** ⚙️

- Python 3.8 or higher
- Conda (for environment management)
- Internet connection (for model embedding)

### **Installation** 🛠️

**Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/QAWithPDF.git
   cd QAWithPDF
