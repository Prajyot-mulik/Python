Horizon-Powered Chatbot
A ChatGPT-like chatbot built with Streamlit, SQLite, and OpenRouter's Horizon-Beta model. Features a dark-themed UI and persistent chat history.
Setup Instructions

Clone the repository.
Install dependencies: pip install -r requirements.txt
Create a .streamlit/secrets.toml file and add your OpenRouter API key:[general]
OPENROUTER_API_KEY = "your-api-key-here"


Ensure the data/ folder exists for SQLite database storage.
Run the app: streamlit run app.py

Features

Dark-themed, ChatGPT-like interface
Persistent chat history using SQLite
Sidebar for navigating past conversations
Powered by OpenRouter's Horizon-Beta model

Project Structure

app.py: Main Streamlit application
utils/database.py: SQLite database operations
utils/openrouter_api.py: OpenRouter API integration
utils/styles.py: Custom dark theme styling
data/chat_history.db: SQLite database
.streamlit/secrets.toml: API key storage

Running the App

Activate your Python environment.
Run streamlit run app.py.
Access the app at http://localhost:8501.

Notes

Ensure the OpenRouter API key is valid and has sufficient quota.
The app supports multiple chat sessions, accessible via the sidebar.
For image support, extend the UI to handle file uploads (not implemented in this version).
