import os
import openai
import gradio as gr
from GPTService import GPTService
import time

os.environ['NO_PROXY'] = '127.0.0.1'
shopGPTService = GPTService()


def shopgpt_chatbot(input_):
    return shopGPTService.serve_query(input_)


def start_message():
    return [["","<p style='font-size: 20px; color:orange ' >Hello, I am ShopGPT. I am here to help your shopping needs.</p><p style='font-size: 20px; color:orange '>What product recommendations are you looking for?</p>"]]

with gr.Blocks() as demo:
    title = gr.HTML(value='''<img src="https://drive.google.com/uc?export=view&id=1amJbcxljmYMuXl8o4N-X7hu3BMnOrZTi" alt="Logo" width="100" height="100"><h1>ShopGPT</h1>''')
    chatbot = gr.Chatbot(value=start_message(), layout="panel", label="ShopGPT", show_label=True)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = shopgpt_chatbot(message)
        chat_history.append(("<p style='font-size: 20px;'>"+message+"</p>", '''<div style="color: orange;">''' + bot_message + '''</div>'''))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(share=True, server_port=8080)


### Older Interface Code
# iface = gr.Interface(fn=chatbot, inputs="textbox", outputs="html",
#                      title="ShopGPT", description="What product recommendations are you looking for?",
#                      theme="compact")
# iface.launch(share=True, server_port=8080)
