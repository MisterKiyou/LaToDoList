import unittest
from app.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task('Do laundry', '2024-02-10')
        self.assertEqual(task.task_name, 'Do laundry')
        self.assertEqual(task.due_date, '2024-02-10')
        self.assertFalse(task.completed)

if __name__ == '__main__':
    unittest.main()
