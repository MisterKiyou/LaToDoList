from app.database import Database
from app.task import Task
from app.ui import UI
import logging

# Set up basic logging configuration
# - Log messages with severity ERROR and above (higher severity levels: CRITICAL > ERROR > WARNING > INFO > DEBUG)
# - Write log messages to the 'app.log' file
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Create UI

ui = UI()

# Create Database instance
db = Database()

# Initialize the database (create tasks table)
db.initialize_database()

# Add a sample task as an example
sample_task = Task(*ui.get_user_input_for_task())  # * can unpact tuples
db.add_task(sample_task)

# Delete tasks
# for i in range(1,11):
#    db.del_task(i)

# Retrieve all tasks from the database
tasks = db.get_all_tasks()

# Display tasks using the UI module
UI.display_tasks(tasks)
