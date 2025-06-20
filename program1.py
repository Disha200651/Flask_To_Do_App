# Simple To-Do List App
tasks = []  # This will hold our tasks

while True:
    print("\n==== To-Do List App ====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"name": task, "done": False})
        print(f"✅ Task '{task}' added.")
    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            for i, t in enumerate(tasks, 1):
                status = "✔️ Done" if t["done"] else "❌ Not Done"
                print(f"{i}. {t['name']} [{status}]")
    elif choice == "3":
        num = int(input("Enter the task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"✅ Task {num} marked as done.")
        else:
            print("❌ Invalid task number.")
    elif choice == "4":
        num = int(input("Enter the task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted_task = tasks.pop(num - 1)
            print(f"🗑️ Task '{deleted_task['name']}' deleted.")
        else:
            print("❌ Invalid task number.")
    elif choice == "5":
        print("👋 Exiting the app. Good job!")
        break
    else:
        print("❌ Invalid choice. Try again.")
