import sqlite3
import json
from datetime import datetime

class SharedMemory:
    def __init__(self, db_name="shared_memory.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                format TEXT,
                intent TEXT,
                timestamp TEXT,
                extracted_values TEXT,
                thread_id TEXT
            )
        ''')
        self.conn.commit()

    def log_entry(self, source, format_type, intent, extracted_values, thread_id=None):
        self.conn.execute('''
            INSERT INTO memory (source, format, intent, timestamp, extracted_values, thread_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            source,
            format_type,
            intent,
            datetime.now().isoformat(),
            json.dumps(extracted_values),
            thread_id
        ))
        self.conn.commit()

    def fetch_all(self):
        cursor = self.conn.execute('SELECT * FROM memory')
        return cursor.fetchall()
