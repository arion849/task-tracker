from task_tracker import Task

while True:
    print("\n1. Exit")
    print("2. Add Task")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("Goodbye")
        break
    if choice == "2":
        Task.add_task()

