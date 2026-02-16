import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "cases.db")

def init_db():
    os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_name TEXT,
            investigator TEXT
        )
    """)

    conn.commit()
    conn.close()

def create_case(case_name, investigator):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        "INSERT INTO cases (case_name, investigator) VALUES (?, ?)",
        (case_name, investigator)
    )

    conn.commit()
    conn.close()

