import sqlite3
import os
from datetime import datetime

# Define absolute path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'chat_history.db')

def init_db():
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats
                 (chat_id TEXT, title TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (chat_id TEXT, role TEXT, content TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_message(chat_id, role, content, title):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT OR REPLACE INTO chats (chat_id, title, created_at) VALUES (?, ?, ?)",
              (chat_id, title, timestamp))
    c.execute("INSERT INTO messages (chat_id, role, content, timestamp) VALUES (?, ?, ?, ?)",
              (chat_id, role, content, timestamp))
    conn.commit()
    conn.close()

def load_chat_history(chat_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT role, content FROM messages WHERE chat_id = ? ORDER BY timestamp", (chat_id,))
    messages = [{"role": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    return messages

def get_chat_sessions():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT chat_id, title FROM chats ORDER BY created_at DESC")
    sessions = c.fetchall()
    conn.close()
    return sessions