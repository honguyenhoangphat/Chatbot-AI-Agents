import time
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from pymongo import MongoClient
from datetime import datetime

# Kết nối MongoDB local
client = MongoClient("mongodb://localhost:27017")
db = client["AI-Agents-history"]
history_collection = db["chat_history"]

# === Load vectorstore đã build sẵn từ ./db ===
embedding_model = OllamaEmbeddings(model="mxbai-embed-large")
vectorstore = Chroma(persist_directory="./db", embedding_function=embedding_model)


llm = ChatOllama(model="phi")

# Hàm luu lich su cau hoi
def save_history(question, answer, duration):
    history_collection.insert_one({
        "timestamp": datetime.now(),
        "question": question,
        "answer": answer.strip(),
        "duration_sec": duration,
        "source": "phi"
    })

def load_history():
    history = []
    for doc in history_collection.find().sort("timestamp", 1):  # sắp xếp theo thời gian tăng dần
        history.append((doc["question"], doc["answer"]))
    return history

# === Hàm hỏi–đáp chính ===
def run_agent(question):
    try:
        docs = vectorstore.similarity_search(question, k=2)
        context = "\n\n".join([
            "\n".join(line for line in doc.page_content.split("\n") if "tên:" in line or "chip:" in line)
            for doc in docs
        ])

        prompt = f"""Bạn là một trợ lý AI tư vấn điện thoại.

        Người dùng hỏi: {question}

        Dưới đây là thông tin về các điện thoại liên quan:
        {context}

        Hãy liệt kê tên, RAM, chip, và giá của các điện thoại có trong dữ liệu.
        Không được suy đoán nếu không có dữ liệu rõ ràng."""

        start = time.time()
        response = llm.invoke(prompt)
        duration = time.time() - start
        save_history(question, response.content, duration)

        return f"(⏱ {duration:.2f} giây)\n\n{response.content}"
    except Exception as e:
        return f"[Lỗi xử lý]: {e}"
