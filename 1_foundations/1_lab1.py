from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(override=True)

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

if api_key:
    print(f"DeepSeek API key exists and begins: {api_key[:8]}")
else:
    print("DeepSeek API key not set")

client = OpenAI(api_key=api_key, base_url=base_url)

question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
messages = [
    {"role": "user", "content": question},
]

response = client.chat.completions.create(model="deepseek-chat", messages=messages)

question = response.choices[0].message.content
print(question)

messages = [
    {"role": "user", "content": question},
]

response = client.chat.completions.create(model="deepseek-chat", messages=messages)

answer = response.choices[0].message.content
print(answer)

from IPython.display import Markdown, display

display(Markdown(answer))
