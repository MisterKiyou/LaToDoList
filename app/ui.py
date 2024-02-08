import logging


class UI:
    @staticmethod
    def display_tasks(tasks):
        try:
            for task in tasks:
                print(f"Task ID: {task[0]}, Task Name: {task[1]}, Due Date: {task[2]}, Completed: {task[3]}")
        except IndexError as e:
            logging.error(f"Error displaying tasks: {e}")

    @staticmethod
    def get_user_input(prompt, valid_choices):
        while True:
            try:
                user_input = input(prompt).strip().lower()
                if user_input in valid_choices:
                    return user_input
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                logging.error(f"Error in get_user_input: {e}")
                print("An error occurred. Please try again or contact support.")
