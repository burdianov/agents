import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from IPython.display import Markdown, display

load_dotenv(override=True)

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_base_url = os.getenv("DEEPSEEK_BASE_URL")

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

groq_api_key = os.getenv("GROQ_API_KEY")
groq_base_url = os.getenv("GROQ_BASE_URL")


GEMINI_MODEL = "gemini-2.5-flash"
GROQ_MODEL = "llama-3.1-8b-instant"
DEEPSEEK_MODEL = "deepseek-chat"

if deepseek_api_key:
    print(f"Deepseek API key exists and begins: {deepseek_api_key[:8]}")
else:
    print("Deepseek API key not set")

if gemini_api_key:
    print(f"Google API key exists and begins: {gemini_api_key[:8]}")
else:
    print("Google API key not set")

request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. Respond only with the question. "
request += "Answer only with the question, no explanation"

messages = [
    {"role": "user", "content": request},
]


deepseek_client = OpenAI(api_key=deepseek_api_key, base_url=deepseek_base_url)
response = deepseek_client.chat.completions.create(
    model=DEEPSEEK_MODEL, messages=messages
)

question = response.choices[0].message.content
print(question)

competitors = []
answers = []
messages = [
    {"role": "user", "content": question},
]

response = deepseek_client.chat.completions.create(
    model=DEEPSEEK_MODEL, messages=messages
)
answer = response.choices[0].message.content

display(Markdown(answer).data)

competitors.append(DEEPSEEK_MODEL)
answers.append(answer)


gemini_client = OpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
response = gemini_client.chat.completions.create(model=GEMINI_MODEL, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer).data)

competitors.append(GEMINI_MODEL)
answers.append(answer)

gemini_client = OpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
response = gemini_client.chat.completions.create(model=GEMINI_MODEL, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer).data)

competitors.append(GEMINI_MODEL)
answers.append(answer)


groq_client = OpenAI(api_key=groq_api_key, base_url=groq_base_url)
response = groq_client.chat.completions.create(model=GROQ_MODEL, messages=messages)
answer = response.choices[0].message.content

display(Markdown(answer).data)

competitors.append(GROQ_MODEL)
answers.append(answer)
