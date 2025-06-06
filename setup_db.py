import sqlite3

def initialize_database():
    conn = sqlite3.connect("urban_insights.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            image_analysis TEXT NOT NULL,
            analyst_notes TEXT,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")
