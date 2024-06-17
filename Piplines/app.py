import gradio as gr
from piplines import simpleRouter, get_RAG_chain, get_normal_chain


def user(prompt, chat_history):
    return '', chat_history + [[prompt, None]]


def response(prompt, chat_history, model_input, temperature_input, topK_input, strategy_input):
    chat_history[-1][1] = ''
    if simpleRouter(chat_history[-1][0]):
        for chunk in get_normal_chain(model_input, temperature_input).stream(
                {'input': prompt, 'chat_history': chat_history}):
            if chunk is not None:
                chat_history[-1][1] += chunk
                yield chat_history
    else:
        for chunk in get_RAG_chain(model_input, temperature_input, topK_input, strategy_input).stream(
                {'input': prompt, 'chat_history': chat_history}):
            if answer_chunk := chunk.get('answer'):
                chat_history[-1][1] += answer_chunk
                yield chat_history


if __name__ == '__main__':
    css = '.custom_option {height: 100px} '
    css += '.custom_option2 {height: 150px}'
    css += '.custom_text {height: 100px} '
    css += '.custom_m {height: 25px} '
    css += '.custom_prompt {background-color: rgb(232,232,232)}'

    with gr.Blocks(title='智能信息处理系统', css=css, theme=gr.themes.Soft()) as demo:
        with gr.Row(equal_height=False):
            with gr.Column(scale=1):

                gr.Markdown('# 大模型选项', elem_classes='custom_m')

                model_input = gr.Radio(['v1.5', 'v2.0', 'v3.0', 'v3.5'], interactive=True, type='value', value='v3.5',
                                       label='讯飞星火模型版本', show_label=True, elem_classes='custom_option')

                temperature_input = gr.Slider(label='Temperature', value=0.5, maximum=1, minimum=0, interactive=True,
                                              elem_classes='custom_text')

                gr.Markdown('# 数据库选项', elem_classes='custom_m')

                strategy_input = gr.Radio(['COSINE', 'EUCLIDEAN', 'MAX_INNER_PRODUCT'], interactive=True,
                                          value='COSINE',
                                          label='数据库检索策略', elem_classes='custom_option2')

                topK_input = gr.Number(label='TopK', value=3, interactive=True, elem_classes='custom_text')

            with gr.Column(scale=2):
                gr.Markdown(value='# 大模型聊天功能',elem_classes='custom_m')
                chatbot = gr.Chatbot(label='Chat !',height='510px')

        prompt = gr.Textbox(label='Prompt', interactive=True,elem_classes='custom_prompt')

        gr.ClearButton(components=[prompt, chatbot], value='Clear Console')
        prompt.submit(fn=user,
                      inputs=[prompt, chatbot],
                      outputs=[prompt, chatbot], queue=False).then(fn=response,
                                                                   inputs=[prompt, chatbot, model_input,
                                                                           temperature_input,
                                                                           topK_input, strategy_input],
                                                                   outputs=[chatbot])

    gr.close_all()

    demo.launch(server_name='', server_port=8080)
