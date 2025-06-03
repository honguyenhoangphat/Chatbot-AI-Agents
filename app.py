from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from pymongo import MongoClient
from datetime import datetime
import time
# Kết nối MongoDB local
client = MongoClient("mongodb://localhost:27017")
db = client["AI-Agents-history"]
history_collection = db["chat_history"]

# Load lại vectorstore đã có sẵn
embedding_model = OllamaEmbeddings(model="mxbai-embed-large")
vectorstore = Chroma(persist_directory="./db", embedding_function=embedding_model)

llm = ChatOllama(model="mistral")

# Hàm luu lich su cau hoi
def save_history(question, answer, duration):
    try:
        history_collection.insert_one({
            "timestamp": datetime.now(),
            "question": question,
            "answer": answer.strip(),
            "duration_sec": duration,
            "source": "mistral"
        })
        print("✅ Đã lưu lịch sử vào MongoDB")
    except Exception as e:
        print(f"❌ Lỗi khi lưu MongoDB: {e}")


def load_history():
    history = []
    for doc in history_collection.find().sort("timestamp", 1):  # sắp xếp theo thời gian tăng dần
        history.append((doc["question"], doc["answer"]))
    return history

def run_agent(question):
    try:
        docs = vectorstore.similarity_search(question, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Bạn là một trợ lý AI chuyên tư vấn điện thoại. Bạn **chỉ được phép trả lời dựa trên dữ liệu dưới đây**.

        ### Câu hỏi người dùng:
        {question}

        ### Dữ liệu sản phẩm liên quan:
        {context}

        ### Yêu cầu:
        - Chỉ sử dụng thông tin có trong dữ liệu bên trên.
        - Nếu câu hỏi yêu cầu thông tin chi tiết, hãy liệt kê đầy đủ các mục: tên, RAM, chip, màn hình, camera, và giá.
        - Không đưa ra giả định, không mời người dùng xem thêm trên web khác.
        - Nếu không tìm thấy dữ liệu phù hợp, hãy nói rõ "Không có dữ liệu".

        ==> Câu trả lời:
        """

        start = time.time()
        response = llm.invoke(prompt)
        duration = time.time() - start
        save_history(question, response.content, duration)
        return f"(⏱ {duration:.2f} giây)\n\n{response.content}"
    except Exception as e:
        return f"[Lỗi xử lý]: {e}"
