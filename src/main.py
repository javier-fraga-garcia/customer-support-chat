import os
from openai import OpenAI
from dotenv import load_dotenv

from core.prompts import system_message
from tools.config import tools_config
from tools.utils import handle_tool_calls

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
PORT = int(os.environ.get('PORT', 3000))

if not OPENAI_API_KEY:
    raise RuntimeError("No OPENAI_API_KEY provided. Please set it in your environment or .env file.")

openai_client = OpenAI(api_key=OPENAI_API_KEY)


def chat(message, history):
    messages = system_message + history + [{"role": "user", "content": message}]
    done = False
    while not done:
        response = openai_client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=messages,
            tools=tools_config,
            parallel_tool_calls=False,
        )
        if response.choices[0].finish_reason == "tool_calls":
            message = response.choices[0].message
            tool_calls = message.tool_calls
            results = handle_tool_calls(tool_calls)
            messages.append(message)
            messages.extend(results)
        else:
            done = True
    return response.choices[0].message.content


if __name__ == '__main__':
    import gradio as gr
    gr.ChatInterface(chat, type="messages").launch(server_name='0.0.0.0', server_port=PORT, share=False)