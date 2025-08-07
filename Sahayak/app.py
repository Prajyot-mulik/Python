import streamlit as st
import sqlite3
import os
from datetime import datetime
from utils.database import init_db, save_message, load_chat_history, get_chat_sessions
from utils.openrouter_api import get_openrouter_response
from utils.styles import apply_dark_theme
from gtts import gTTS

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Horizon Chatbot", page_icon="🤖", layout="wide")

# Apply dark theme after set_page_config
apply_dark_theme()

# Initialize database
init_db()

# Initialize session state
if "chat_id" not in st.session_state:
    st.session_state.chat_id = str(datetime.now().timestamp())
    st.session_state.messages = []
if "chat_title" not in st.session_state:
    st.session_state.chat_title = f"Chat {st.session_state.chat_id[:8]}"
if "language" not in st.session_state:
    st.session_state.language = "English"

# Sidebar for chat history and language selection
with st.sidebar:
    st.header("Chat History")
    chat_sessions = get_chat_sessions()
    chat_options = {session[1]: session[0] for session in chat_sessions}
    chat_options["New Chat"] = st.session_state.chat_id
    selected_chat = st.selectbox(
        "Select a chat",
        options=list(chat_options.keys()),
        index=list(chat_options.keys()).index(st.session_state.chat_title) if st.session_state.chat_title in chat_options else 0
    )
    
    if selected_chat != st.session_state.chat_title:
        st.session_state.chat_id = chat_options[selected_chat]
        st.session_state.chat_title = selected_chat
        st.session_state.messages = load_chat_history(st.session_state.chat_id)
    
    st.header("Language")
    st.session_state.language = st.selectbox(
        "Choose your language",
        options=["English", "Hindi", "Marathi"],
        index=["English", "Hindi", "Marathi"].index(st.session_state.language)
    )

# Main chat interface
st.title("🤖 Sahayak")
st.markdown(f"Ask anything : **{st.session_state.language}**")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "audio_path" in msg:
            st.audio(msg["audio_path"], format="audio/mp3")

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    save_message(st.session_state.chat_id, "user", prompt, st.session_state.chat_title)

    # Get and display Horizon response
    with st.chat_message("assistant"):
        response = get_openrouter_response(prompt, st.session_state.messages, st.session_state.language)
        st.markdown(response)
        
        # Generate and save audio
        audio_dir = os.path.join("data", "audio")
        os.makedirs(audio_dir, exist_ok=True)
        audio_path = os.path.join(audio_dir, f"response_{st.session_state.chat_id}_{len(st.session_state.messages)}.mp3")
        tts = gTTS(text=response, lang={"English": "en", "Hindi": "hi", "Marathi": "mr"}[st.session_state.language])
        tts.save(audio_path)
        st.audio(audio_path, format="audio/mp3")
        
    st.session_state.messages.append({"role": "assistant", "content": response, "audio_path": audio_path})
    save_message(st.session_state.chat_id, "assistant", response, st.session_state.chat_title)