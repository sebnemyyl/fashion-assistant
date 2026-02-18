import sqlite3
from pathlib import Path

DB_PATH = Path("data/wardrobe.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wardrobe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            color TEXT,
            style TEXT,
            season TEXT,
            occasion TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_item(name, type_, color, style, season, occasion):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO wardrobe (name, type, color, style, season, occasion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, type_, color, style, season, occasion))

    conn.commit()
    conn.close()


def get_all_items():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM wardrobe")
    items = cursor.fetchall()

    conn.close()
    return items
