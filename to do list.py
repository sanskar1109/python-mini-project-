import datetime

# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task, priority, due_date, reminder):
    task_data = {
        "task": task,
        "priority": priority,
        "due_date": due_date,
        "reminder": reminder,
    }
    tasks.append(task_data)
    print("Task added:", task)

# Function to view tasks
def view_tasks():
    if tasks:
        print("Tasks:")
        for i, task_data in enumerate(tasks, start=1):
            print(f"{i}. Task: {task_data['task']}")
            print(f"   Priority: {task_data['priority']}")
            print(f"   Due Date: {task_data['due_date']}")
            print(f"   Reminder: {task_data['reminder']}")
    else:
        print("No tasks to display.")

# Function to remove a task
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print("Task removed:", removed_task["task"])
    else:
        print("Invalid task index.")

# Function to edit a task
def edit_task(task_index, new_task, new_priority, new_due_date, new_reminder):
    if 1 <= task_index <= len(tasks):
        task_data = tasks[task_index - 1]
        task_data["task"] = new_task
        task_data["priority"] = new_priority
        task_data["due_date"] = new_due_date
        task_data["reminder"] = new_reminder
        print("Task edited.")
    else:
        print("Invalid task index.")

# Function to save tasks to a file
def save_tasks_to_file(filename):
    with open(filename, 'w') as file:
        for task_data in tasks:
            file.write(f"{task_data['task']}|{task_data['priority']}|{task_data['due_date']}|{task_data['reminder']}\n")
    print("Tasks saved to file:", filename)

# Main loop
while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Edit Task")
    print("5. Save Tasks to File")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        priority = input("Enter priority (High, Medium, Low): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        reminder = input("Set a reminder (YYYY-MM-DD HH:MM): ")
        add_task(task, priority, due_date, reminder)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task index to edit: "))
        new_task = input("Enter the new task: ")
        new_priority = input("Enter the new priority (High, Medium, Low): ")
        new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
        new_reminder = input("Set a new reminder (YYYY-MM-DD HH:MM): ")
        edit_task(task_index, new_task, new_priority, new_due_date, new_reminder)
    elif choice == "5":
        filename = input("Enter the filename to save tasks: ")
        save_tasks_to_file(filename)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
