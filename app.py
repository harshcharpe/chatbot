import os
import streamlit as st
from google import genai

st.set_page_config(page_title="Open Source Gemini Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Open Source Gemini Chatbot")
st.caption("Powered by Google Gemini | Free & Open Source")

# Retrieve API key securely from Streamlit Secrets or local environment
api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

if not api_key:
    # Allows users or reviewers to test using their own key if none is hosted
    api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")
    if not api_key:
        st.info("Please provide a Gemini API key in the sidebar or deploy secrets to continue.")
        st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Initialize persistent session chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User prompt input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        try:
            # Build conversation history for the model
            contents = [
                {"role": m["role"], "parts": [{"text": m["content"]}]}
                for m in st.session_state.messages
            ]
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=contents,
            )
            bot_reply = response.text
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            st.error(f"Error: {e}")
