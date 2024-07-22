tasks = []
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")
def complete_task(task_index):
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['task']}' marked as completed.")
    else:
        print("Invalid task index.")
def remove_task(task_index):
    if task_index >= 0 and task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task index.")
def print_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['task']} - {status}")
while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Remove Task")
    print("4. View Tasks")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        task_name = input("Enter task name: ")
        add_task(task_name)
    elif choice == '2':
        task_index = int(input("Enter task index to complete: ")) - 1
        complete_task(task_index)
    elif choice == '3':
        task_index = int(input("Enter task index to remove: ")) - 1
        remove_task(task_index)
    elif choice == '4':
        print_tasks()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")