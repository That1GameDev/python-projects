import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['name']}")

def add_task(tasks):
    name = input("Enter task name: ")
    tasks.append({"name": name, "done": False})
    save_tasks(tasks)
    print(f"Task '{name}' added!")

def complete_task(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to mark complete: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number!")

def delete_task(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Task '{removed['name']}' deleted!")
    else:
        print("Invalid task number!")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List App ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

main()