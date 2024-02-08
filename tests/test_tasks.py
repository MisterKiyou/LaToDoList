import unittest
from app.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        """
        Test the creation of a Task instance.

        This test ensures that a Task instance is created with the correct attributes.
        """
        task = Task('Do laundry', '2024-02-10')
        self.assertEqual(task.task_name, 'Do laundry')
        self.assertEqual(task.due_date, '2024-02-10')
        self.assertFalse(task.completed)

if __name__ == '__main__':
    unittest.main()

