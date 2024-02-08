class UI:
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(f"Task ID: {task[0]}, Task Name: {task[1]}, Due Date: {task[2]}, Completed: {task[3]}")
    @staticmethod
    def get_user_input(prompt, valid_choices):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in valid_choices:
                return user_input
            else:
                print("Invalid choice. Please try again.")
