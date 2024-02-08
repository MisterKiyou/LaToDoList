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
    def get_user_input(prompt, valid_choices, validate_date=False):
        while True:
            try:
                user_input = input(prompt).strip().lower()
                if user_input in valid_choices:
                    return user_input
                elif validate_date and not UI.validate_date_format(user_input):
                    print("Invalid due date. Please ensure the date is after the current date.")
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                logging.error(f"Error in get_user_input: {e}")
                print("An error occurred. Please try again or contact support.")

    @staticmethod
    def validate_date_format(date_string):
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
