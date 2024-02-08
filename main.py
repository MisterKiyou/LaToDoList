from app.database import Database
from app.task import Task
from app.ui import UI
import logging

# Set up basic logging configuration
# - Log messages with severity ERROR and above (higher severity levels: CRITICAL > ERROR > WARNING > INFO > DEBUG)
# - Write log messages to the 'app.log' file
logging.basicConfig(filename='app.log', level=logging.ERROR)

# Create Database instance
db = Database('todo.db')  # Use your actual database file path

# Initialize the database (create tasks table)
db.initialize_database()

# I added a sample task as an exemple
sample_task = Task('Sample Task', '2024-02-15')
db.add_task(sample_task.task_name, sample_task.due_date)

# Lets look at our tasks
tasks = db.get_all_tasks()
UI.display_tasks(tasks)
