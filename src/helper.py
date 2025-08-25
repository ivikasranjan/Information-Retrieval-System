import os
import asyncio
import time
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from tenacity import retry, stop_after_attempt, wait_exponential
from google.api_core.exceptions import ResourceExhausted

# Ensure event loop exists to avoid RuntimeError in Streamlit
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load Google API key
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("Missing GOOGLE_API_KEY in .env")

# Create embeddings and LLM
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=google_api_key
)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=google_api_key,
    temperature=0.3
)

# Retry wrapper for Gemini API calls
@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=4, max=60))
def safe_llm_call(prompt: str):
    try:
        return llm.invoke(prompt)
    except ResourceExhausted:
        print("Quota exceeded, retrying with backoff...")
        raise


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # safer extraction
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks, persist_directory="chroma_db"):
    vector_store = Chroma.from_texts(
        text_chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    vector_store.persist()
    return vector_store


def get_conversational_chain(vector_store):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain
