import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    def initialize_database(self):
        try :
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    due_date DATE,
                    completed BOOLEAN
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error initializing database: {e}")

    def add_task(self, task_name, due_date=None):
        try :
            self.cursor.execute('INSERT INTO tasks (task_name, due_date, completed) VALUES (?, ?, ?)',
                                (task_name, due_date, False))
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error adding task to database: {e}")

    def get_all_tasks(self):
        try :
            self.cursor.execute('SELECT * FROM tasks')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error retrieving tasks from database: {e}")
            return []
