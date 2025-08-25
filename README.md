# 📚 Information Retrieval System

An **Information Retrieval (IR) System** built with Python that processes documents (PDFs, text) and enables **semantic search & conversational Q&A** using **LangChain, ChromaDB, and Google Gemini API**.  

---

## 🚀 Features
- 📄 Extract text from PDFs  
- ✂️ Split documents into chunks for efficient processing  
- 🔎 Store embeddings in **ChromaDB** (persistent vector database)  
- 🤖 Query documents with **Conversational Retrieval Chain**  
- 🧠 Context-aware answers with chat history memory  
- 🔑 Powered by **Google Gemini (Generative AI)**  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **LangChain** – framework for LLM apps  
- **Chroma** – vector database  
- **Google Gemini API** – LLM + embeddings  
- **PyPDF2** – PDF text extraction  
- **dotenv** – environment variable management  

---

## 📂 Project Structure
Information-Retrieval-System/
│── helper.py # Core logic (PDF reading, embeddings, chain)
│── app.py # Streamlit / CLI app (if applicable)
│── requirements.txt # Dependencies
│── .env # API keys (not committed to GitHub)
│── README.md # Documentation
│── chroma_db/ # Persistent Chroma database
│── sample_pdfs/ # Example PDFs (optional)

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/Information-Retrieval-System.git
   cd Information-Retrieval-System
Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root folder:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
▶️ Usage
Extract Text & Build Vector Store
python
Copy
Edit
from helper import get_pdf_text, get_text_chunks, get_vector_store

pdf_text = get_pdf_text(["sample_pdfs/example.pdf"])
chunks = get_text_chunks(pdf_text)
vector_store = get_vector_store(chunks)
Start Conversational Retrieval
python
Copy
Edit
from helper import get_conversational_chain

chain = get_conversational_chain(vector_store)
response = chain.run("What is this document about?")
print(response)
⚠️ Troubleshooting
ResourceExhausted: 429 → You exceeded Gemini API quota.

Use gemini-1.5-flash instead of gemini-1.5-pro.

Add retry with exponential backoff.

Check quota/billing in Google Cloud Console.

📌 Roadmap
 Add support for scanned PDFs (OCR)

 Web UI with Streamlit

 Multi-document retrieval

 Deployment on cloud

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch

Submit a pull request

📜 License
This project is licensed under the MIT License.

⭐ Acknowledgements
LangChain

ChromaDB

Google Gemini API

yaml
Copy
Edit

---

👉 Do you also want me to create a **requirements.txt** file for this project so your GitHub repo is plug-and-play?






You said:
please give all things in a single cell


ChatGPT said:
Got it 👍 Here’s a complete README.md in one single block so you can copy-paste directly into your repo:

markdown
Copy
Edit
# 📚 Information Retrieval System

An **Information Retrieval (IR) System** built with Python that processes documents (PDFs, text) and enables **semantic search & conversational Q&A** using **LangChain, ChromaDB, and Google Gemini API**.  

---

## 🚀 Features
- 📄 Extract text from PDFs  
- ✂️ Split documents into chunks for efficient processing  
- 🔎 Store embeddings in **ChromaDB** (persistent vector database)  
- 🤖 Query documents with **Conversational Retrieval Chain**  
- 🧠 Context-aware answers with chat history memory  
- 🔑 Powered by **Google Gemini (Generative AI)**  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **LangChain** – framework for LLM apps  
- **Chroma** – vector database  
- **Google Gemini API** – LLM + embeddings  
- **PyPDF2** – PDF text extraction  
- **dotenv** – environment variable management  

---

## 📂 Project Structure
Information-Retrieval-System/
│── helper.py # Core logic (PDF reading, embeddings, chain)
│── app.py # Streamlit / CLI app (if applicable)
│── requirements.txt # Dependencies
│── .env # API keys (not committed to GitHub)
│── README.md # Documentation
│── chroma_db/ # Persistent Chroma database
│── sample_pdfs/ # Example PDFs (optional)

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/Information-Retrieval-System.git
   cd Information-Retrieval-System
Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root folder:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
▶️ Usage
Extract Text & Build Vector Store
python
Copy
Edit
from helper import get_pdf_text, get_text_chunks, get_vector_store

pdf_text = get_pdf_text(["sample_pdfs/example.pdf"])
chunks = get_text_chunks(pdf_text)
vector_store = get_vector_store(chunks)
Start Conversational Retrieval
python
Copy
Edit
from helper import get_conversational_chain

chain = get_conversational_chain(vector_store)
response = chain.run("What is this document about?")
print(response)
⚠️ Troubleshooting
ResourceExhausted: 429 → You exceeded Gemini API quota.

Use gemini-1.5-flash instead of gemini-1.5-pro.

Add retry with exponential backoff.

Check quota/billing in Google Cloud Console.

📌 Roadmap
 Add support for scanned PDFs (OCR)

 Web UI with Streamlit

 Multi-document retrieval

 Deployment on cloud

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch

Submit a pull request

📜 License
This project is licensed under the MIT License.

⭐ Acknowledgements
LangChain

ChromaDB

Google Gemini API