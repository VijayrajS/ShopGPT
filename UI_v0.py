import os
import openai
import gradio as gr
from GPTService import GPTService

os.environ['NO_PROXY'] = '127.0.0.1'
shopGPTService = GPTService()


def chatbot(input_):
    return shopGPTService.serve_query(input_)

iface = gr.Interface(fn=chatbot, inputs="textbox", outputs="html",
                     title="ShopGPT", description="What product recommendations are you looking for?",
                     theme="compact")
iface.launch(share=True, server_port=8080)