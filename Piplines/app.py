import gradio as gr
from piplines import pipline


def response(prompt, chat_history,model_input, temperature_input, topK_input, strategy_input):
    if not chat_history:
        chat_history = []
    chat_history.append((prompt, pipline(prompt, chat_history, model_input, temperature_input, topK_input, strategy_input)))
    return chat_history


if __name__ == '__main__':
    with gr.Blocks() as demo:
        with gr.Row('布局'):
            with gr.Column('选项'):
                model_input = gr.Radio(['v1.5', 'v2.0', 'v3.0', 'v3.5'], interactive=True, type='value')
                temperature_input = gr.Slider(label='Temperature', value=0.5, maximum=1, minimum=0, interactive=True)
                strategy_input = gr.Radio(['COSINE', 'l2', 'Inner'], interactive=True)
                topK_input = gr.Number(label='TopK', value=3, interactive=True)
            with gr.Column('聊天'):
                chatbot = gr.Chatbot()
                prompt = gr.Textbox(label='Prompt',interactive=True)
                gr.ClearButton(components=[prompt, chatbot], value='Clear Console')
                prompt.submit(fn=response,
                              inputs=[prompt, chatbot, model_input, temperature_input, topK_input, strategy_input],
                              outputs=[chatbot])

    gr.close_all()

    demo.launch(server_name='', server_port=8080)
