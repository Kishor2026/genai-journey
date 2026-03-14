tasks = []

while True:

    print("\n1 Add Task")
    print("2 View Tasks")
    print("3 Remove Task")
    print("4 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(i + 1, task)

    elif choice == "3":
        index = int(input("Enter task number to remove: "))
        tasks.pop(index - 1)
        print("Task removed")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid option")