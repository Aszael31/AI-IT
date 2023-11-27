import openai
import gradio
import gradio as gr

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a information technology experts that specializes in troubleshooting technology issues"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "IT Support AI")

demo.launch(share=True)