from google import genai
from google.genai import types

# Initialize the client directly with your API key
API_KEY = "AQ.Ab8RN6K6cTcAtiueHLfaUzp0ZyqLonMYfo2mwGEkAeXq_UDKFw"
client = genai.Client(api_key=API_KEY)

# Assistant configuration
config = types.GenerateContentConfig(
    system_instruction="You are a helpful and concise AI assistant.",
    temperature=0.7,
)

# Start multi-turn conversation session
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