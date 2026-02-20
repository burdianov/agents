from dotenv import load_dotenv
import os

load_dotenv(override=True)

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

if deepseek_api_key:
    print(f"DeepSeek API key exists and begins: {deepseek_api_key[:8]}")
else:
    print("DeepSeek API key not set")