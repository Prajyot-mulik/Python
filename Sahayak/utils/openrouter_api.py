import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_openrouter_response(prompt, history, language):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )
    
    # Prepare messages for the API
    messages = [{"role": msg["role"], "content": msg["content"]} for msg in history]
    # Add system prompt to enforce language
    system_prompt = f"You are a helpful assistant. Respond only in {language}."
    messages.insert(0, {"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    # Call OpenRouter API
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "http://localhost:8501",  # Your local Streamlit app URL
            "X-Title": "Horizon Chatbot"  # App title for OpenRouter
        },
        model="openrouter/horizon-beta",
        messages=messages,
        stream=True
    )
    
    # Collect streamed response
    full_response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
    
    return full_response