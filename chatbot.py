import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file.")
    exit(1)

client = genai.Client(api_key=api_key)

config = types.GenerateContentConfig(
    system_instruction="You are a helpful and concise AI assistant.",
    temperature=0.7,
)

# Updated to the active model
chat = client.chats.create(model="gemini-3.6-flash", config=config)

print("--- AI Chatbot is Ready! Type 'exit' to quit. ---\n")

while True:
    user_input = input("You: ").strip()
    
    if not user_input:
        continue
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"\nBot: {response.text}\n")
    except Exception as e:
        print(f"\n[API Error]: {e}\n")