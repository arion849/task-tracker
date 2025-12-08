from task_tracker import Task


# Main loop 
while True:
    print("\n1. Exit")
    print("2. Add Task")
    print("3. List all tasks")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("Goodbye")
        break
    if choice == "2":
        Task.add_task()
    if choice == "3":
        Task.list_task()

