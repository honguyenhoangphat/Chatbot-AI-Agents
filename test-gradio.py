import gradio as gr
from app import run_agent, load_history

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Chatbot Tư Vấn Điện Thoại
        Hỏi bất kỳ điều gì về điện thoại: pin, RAM, chụp hình, chơi game, v.v.
        """
    )

    chatbot = gr.Chatbot(label="Trợ lý tư vấn AI", value=load_history())

    with gr.Row():
        user_input = gr.Textbox(placeholder="Bạn muốn hỏi gì về điện thoại?", scale=8)
        send_btn = gr.Button("Gửi", scale=1)

    def respond(message, history):
        response = run_agent(message)
        history = history or []
        history.append((message, response))
        return history, ""

    send_btn.click(fn=respond, inputs=[user_input, chatbot], outputs=[chatbot, user_input])
    user_input.submit(fn=respond, inputs=[user_input, chatbot], outputs=[chatbot, user_input])

if __name__ == "__main__":
    demo.launch(share=True)
