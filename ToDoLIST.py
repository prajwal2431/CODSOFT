class ToDoList:
    def __init__(self, name):
        self.name = name
        self.todo_list = []

    def add_task(self, task):
        self.todo_list.append(task)
        print(f"Task '{task}' added to {self.name} to-do list.")

    def display_todo_list(self):
        print(f"{self.name} To-Do List:")
        if not self.todo_list:
            print("No tasks.")
        else:
            for index, task in enumerate(self.todo_list, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_index):
        try:
            removed_task = self.todo_list.pop(task_index - 1)
            print(f"Task '{removed_task}' removed from {self.name} to-do list.")
        except IndexError:
            print("Invalid task index.")


def main():
    todo_lists = []

    while True:
        print("\nOptions:")
        print("1. Create a new To-Do List")
        print("2. Display To-Do List")
        print("3. Add Task")
        print("4. Remove Task")
        print("5. Quit")
        try:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                name = input("Enter the name for the new to-do list: ")
                new_todo_list = ToDoList(name)
                todo_lists.append(new_todo_list)
                print(f"{name} to-do list created.")
            elif choice == 2:
                list_name = input("Enter the name of the to-do list to display: ")
                for todo_list in todo_lists:
                    if todo_list.name == list_name:
                        todo_list.display_todo_list()
                        break
                else:
                    print(f"To-do list with name '{list_name}' not found.")
            elif choice == 3:
                list_name = input("Enter the name of the to-do list to add a task: ")
                for todo_list in todo_lists:
                    if todo_list.name == list_name:
                        task = input("Enter the task: ")
                        todo_list.add_task(task)
                        break
                else:
                    print(f"To-do list with name '{list_name}' not found.")
            elif choice == 4:
                list_name = input("Enter the name of the to-do list to remove a task: ")
                for todo_list in todo_lists:
                    if todo_list.name == list_name:
                        todo_list.display_todo_list()
                        task_index = int(input("Enter the index of the task to remove: "))
                        todo_list.remove_task(task_index)
                        break
                else:
                    print(f"To-do list with name '{list_name}' not found.")
            elif choice == 5:
                print("Exiting the to-do list program. Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
