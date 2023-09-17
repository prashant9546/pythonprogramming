from builtins import print, input, enumerate, FileNotFoundError, open
import json

# Initialize an empty task list
tasks = []

# Load tasks from a JSON file if available
try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (optional): ")
    category = input("Enter category (optional): ")
    status = "Open"

    tasks.append({
        'Name': task_name,
        'Priority': priority,
        'Due Date': due_date,
        'Category': category,
        'Status': status
    })

    save_tasks()
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['Name']} (Priority: {task['Priority']}, Due Date: {task['Due Date']}, Status: {task['Status']})")

# You can similarly implement functions to update and delete tasks

# Main menu
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
