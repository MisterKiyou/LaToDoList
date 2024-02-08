import unittest
from app.database import Database

class TestDatabase(unittest.TestCase):
    def test_database_initialization(self):
        db_test_path = 'test_todo.db'
        db = Database(db_test_path)
        db.initialize_database()
        # Add assertions based on your test requirements

    def test_add_task_to_database(self):
        # Test adding a task to the database
        # ...

    def test_retrieve_tasks_from_database(self):
        # Test retrieving tasks from the database
        # ...

    # Add more test methods as needed
