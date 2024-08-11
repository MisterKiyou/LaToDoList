import sqlite3

def init_db():
    conn = sqlite3.connect('database/todolist.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            parent_id INTEGER,
            FOREIGN KEY (parent_id) REFERENCES tasks (id)
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
