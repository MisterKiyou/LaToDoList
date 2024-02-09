import logging
from datetime import datetime


class UI:
    @staticmethod
    def display_tasks(tasks):
        try:
            for task in tasks:
                print(f"Task ID: {task[0]}, Task Name: {task[1]}, Due Date: {task[2]}, Completed: {task[3]}")
        except IndexError as e:
            logging.error(f"Error displaying tasks: {e}")

    @staticmethod
    def get_user_input_for_task():
        """
        Get user input for creating a task.

        :return: A tuple containing task information (name, referent, due_date, comment).
        """
        while True:
            try:
                name = input("Enter Task Name: ").strip()
                referent = input("Enter Referent: ").strip()
                due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
                comment = input("Enter Comment: ").strip()
                # Due date verification
                if UI.validate_date_format(due_date):
                    logging.info(f"Input returned")
                    return name, referent, due_date, comment  # This tuple needs to be unpacked with * when used
                else:
                    print("Invalid due date. Please ensure the date is after the current date.")
            except Exception as e:
                logging.error(f"Error in get_user_input_for_task: {e}")
                print("An error occurred. Please try again or contact support.")

    @staticmethod
    def validate_date_format(date_string):
        """
        Validate the format and due date of a date string.

        :param date_string: The input date string.
        :return: True if the date format and due date are valid, False otherwise.
        """
        try:
            # Parse the input date string
            due_date = datetime.strptime(date_string, '%Y-%m-%d')

            # Check if the due date is after the current date
            current_date = datetime.now()
            if due_date > current_date:
                return True
            else:
                return False
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False
