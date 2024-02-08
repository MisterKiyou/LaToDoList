class Task:
    def __init__(self, task_name, due_date=None):
        self.task_name = task_name
        self.due_date = due_date
        self.completed = False
