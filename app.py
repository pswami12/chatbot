import gradio as gr
import openai

# Set your OpenAI API key here
openai.api_key = ""

system_context = ""

def chatgpt(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": system_context},
            {"role": "user", "content": input_text}
        ]
    )
    
    return response.choices[0].message.content

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    def respond(message, chat_history):
        bot_message = chatgpt(message)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()