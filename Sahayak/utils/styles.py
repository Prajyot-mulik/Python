import streamlit as st

def apply_dark_theme():
    st.markdown("""
        <style>
        body {
            color: #ffffff;
            background-color: #1e1e1e;
        }
        .stApp {
            background-color: #1e1e1e;
        }
        .stTextInput > div > div > input {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 1px solid #444;
        }
        .stButton > button {
            background-color: #3a3a3a;
            color: #ffffff;
            border: 1px solid #555;
        }
        .stSelectbox > div > div > select {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 1px solid #444;
        }
        .stMarkdown {
            color: #ffffff;
        }
        .stSidebar {
            background-color: #252525;
        }
        .stChatMessage {
            background-color: #2d2d2d;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
        </style>
    """, unsafe_allow_html=True)