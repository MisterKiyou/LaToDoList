import sqlite3
import configparser
import logging


class Database:
    def __init__(self, db_path=None):
        """
        Initialize the Database class.

        Reads the 'db_path' from the configuration file or uses the provided value or the default value 'todo.db'.
        Establishes a connection to the SQLite database.

        :param db_path: The path to the SQLite database file.
        :type db_path: str or None
        :raises sqlite3.Error: If there is an error in establishing the database connection.
        """
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Use 'db_path' from the configuration file if provided, else use the provided value or the default value
        self.db_path = db_path or config.get('Database', 'db_path', fallback='todo.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        logging.info(f"Database as been created")

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
                    referent TEXT,
                    due_date DATE,
                    comment TEXT,
                    state BOOLEAN
                )
            ''')
            self.conn.commit()
            logging.info(f"Database as been initialized")
        except sqlite3.Error as e:
            logging.error(f"Error initializing database: {e}")

    def add_task(self, task):
        """
        Add a task to the tasks table in the database.

        :param task: Task to add.
        :raises sqlite3.Error: If there is an error in executing the SQL command.
        """
        try:
            self.cursor.execute('INSERT INTO tasks (task_name, referent, due_date, comment, state) VALUES (?, ?, ?, ?, ?)',
                                (task.name, task.referent, task.due_date, task.comment, task.state))
            self.conn.commit()
            logging.info(f"Task as been added to a Database")
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

    def del_task(self, id_to_del) -> None:
        """
        Delete task with the given id from the tasks table in the database.

        :param id_to_del: The name of the task we want to delete.
        :return: None.
        :raises sqlite3.Error: If there is an error in executing the SQL command.
        """
        try:
            self.cursor.execute('DELETE FROM tasks WHERE id = ?;', (id_to_del,))
            self.conn.commit()
            logging.info(f"A Task  as been deleted")
        except sqlite3.Error as e:
            logging.error(f"Error deleting tasks from database: {e}")
