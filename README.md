# Chatbot-AI-Agents
# Chatbot Tư Vấn Sản Phẩm - Điện Máy Xanh

**Hệ thống chatbot thông minh hỗ trợ người dùng tra cứu thông tin sản phẩm điện tử, điện lạnh, gia dụng... từ siêu thị Điện Máy Xanh.**  
Không cần kết nối API, dữ liệu được thu thập và xử lý cục bộ.

## 🎯 Mục tiêu

- Hỗ trợ người dùng hỏi đáp về sản phẩm như: thông số kỹ thuật, giá bán, thương hiệu, công nghệ...
- Trả lời chính xác, trực quan dựa trên dữ liệu thật được thu thập từ trang [dienmayxanh.com](https://www.dienmayxanh.com/).
- Ứng dụng các công nghệ NLP và mô hình ngôn ngữ để cải thiện trải nghiệm tra cứu sản phẩm.

## 🗂 Dữ liệu sử dụng

- **Nguồn**: Website chính thức của Điện Máy Xanh
- **Hình thức thu thập**: Web scraping với Selenium + BeautifulSoup
- **Cấu trúc dữ liệu**:
  - Danh mục sản phẩm (`TV`, `Tủ lạnh`, `Máy giặt`, ...)
  - Mỗi sản phẩm gồm:
    - Tên sản phẩm
    - Giá
    - Thông số kỹ thuật chi tiết
    - URL sản phẩm
    - Mô tả tổng quan

## 🧠 Kiến trúc

- `Selenium`: crawl dữ liệu HTML động
- `BeautifulSoup`: phân tích nội dung HTML
- `Pandas/JSON`: xử lý và lưu trữ dữ liệu
- `LLM (Ollama + Mistral)` và `Phi`: tạo phản hồi ngôn ngữ tự nhiên
- `Streamlit` hoặc `Gradio`: giao diện người dùng thân thiện

## 🔁 Luồng hoạt động


