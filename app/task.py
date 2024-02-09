class Task:
    def __init__(self, name, referent="Me", due_date=None, comment=None):
        """
        Initialize a Task instance.

        :param name: The name of the task.
        :type name: str
        :param referent: Name of the referent.
        :type referent: str or None
        :param due_date: The due date of the task (default is None).
        :type due_date: str or None
        :param comment: Commentary or describtion of the task.
        :type comment: str or None
        """
        self.name = name
        self.referent = referent
        self.due_date = due_date
        self.comment = comment
        self.state = False
