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
    return [["<p style='font-size: 20px;'>Hello, I am ShopGPT. I am here to help your shopping needs.</p>","<p style='font-size: 20px;'>What product recommendations are you looking for?</p>"]]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(value=start_message())
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = shopgpt_chatbot(message)
        chat_history.append(("<p style='font-size: 20px;'>"+message+"</p>", bot_message))
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