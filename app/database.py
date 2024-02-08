import sqlite3
import configparser
import logging

class Database:
    def __init__(self):
        """
        Initialize the Database class.

        Reads the 'db_path' from the configuration file or uses the default value 'todo.db'.
        Establishes a connection to the SQLite database.

        :raises sqlite3.Error: If there is an error in establishing the database connection.
        """
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Use 'db_path' from the configuration file if provided, else use the default value
        self.db_path = config.get('Database', 'db_path', fallback='todo.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def initialize_database(self):
        """
        Initialize the tasks table in the database if it does not exist.

        :raises sqlite3.Error: If there is an error in executing the SQL command.
        """
        try:
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
        """
        Add a task to the tasks table in the database.

        :param task_name: The name of the task.
        :param due_date: The due date of the task (default is None).
        :raises sqlite3.Error: If there is an error in executing the SQL command.
        """
        try:
            self.cursor.execute('INSERT INTO tasks (task_name, due_date, completed) VALUES (?, ?, ?)',
                                (task_name, due_date, False))
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error adding task to database: {e}")

    def get_all_tasks(self):
        """
        Retrieve all tasks from the tasks table in the database.

        :return: A list of tasks as tuples.
        :rtype: list
        :raises sqlite3.Error: If there is an error in executing the SQL command.
        """
        try:
            self.cursor.execute('SELECT * FROM tasks')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error retrieving tasks from database: {e}")
            return []
