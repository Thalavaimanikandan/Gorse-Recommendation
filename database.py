import sqlite3
from config import DB_PATH

def get_db_connection():
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory=sqlite3.Row
    return conn
def init_db():
    conn=get_db_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS user_actions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        video_id TEXT,
        sql_type TEXT,
        timestamp TEXT
    )
    """)
    conn.close()