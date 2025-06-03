from app import run_agent
import streamlit as st
# === Giao diện người dùng Streamlit hiện đại ===
st.set_page_config(page_title="📱 Chatbot Tư Vấn Sản Phẩm", layout="centered")

st.markdown("<h1 style='text-align: center; color: #0072C6;'>🤖 Chatbot Tư Vấn Điện Thoại</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Dữ liệu lấy từ Điện Máy Xanh - Hãy hỏi bất cứ điều gì về điện thoại!</p>", unsafe_allow_html=True)

# Hộp chat
with st.form(key="chat_form"):
    query = st.text_input("💬 Câu hỏi của bạn:", placeholder="Ví dụ: Điện thoại nào có pin trên 5000mAh?")
    submitted = st.form_submit_button("Gửi")
if query:
    with st.spinner(" Đang xử lý..."):
        try:
            answer = agent.run(query)
            st.success(answer)
        except Exception as e:
            st.error(f"Lỗi: {e}")
