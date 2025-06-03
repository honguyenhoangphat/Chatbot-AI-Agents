# build_vector.py
import pandas as pd
import json
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

load_dotenv()

# Load dữ liệu
with open("phone_database.phones1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.json_normalize(data)
df = df.fillna("không có thông tin")
for col in df.columns:
    df[col] = df[col].astype(str)

# Chuyển mỗi dòng thành văn bản ngắn
def row_to_doc(row):
    content = f"Tên: {row['Ten']}\nGiá: {row['Gia']}\nRAM: {row['Dung_luong_ram']}\nChip: {row['Chipset']}\nCamera sau: {row['Camera_sau']}"
    return Document(page_content=content)

documents = [row_to_doc(row) for _, row in df.iterrows()]

# Tạo embedding + ChromaDB
embedding_model = OllamaEmbeddings(model="mxbai-embed-large")
vectorstore = Chroma.from_documents(documents, embedding=embedding_model, persist_directory="./db")
vectorstore.persist()

print("✅ Tạo vectorstore thành công tại ./db")
