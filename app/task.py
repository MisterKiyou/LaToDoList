class Task:
    def __init__(self, task_name, due_date=None):
        """
        Initialize a Task instance.

        :param task_name: The name of the task.
        :type task_name: str
        :param due_date: The due date of the task (default is None).
        :type due_date: str or None
        """
        self.task_name = task_name
        self.due_date = due_date
        self.completed = False
