# main.py

# Creating a list management application for tracking tasks.
# Key concepts to learn CRUD: Create Read Update Delete

# ------------- Start of program ----------------

# list tasks []
# this is the location where we keep our stuff and is base EMPTY
# this is where our "to-do-list information will be held" 
# list 
tasks = []

print("--- Welcome to the Task Manager ---")


# Starting a loop so we can keep the prgram running to add multiple tasks
while True:
    print("\nSelect an option:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        new_task = input("Please add a new task: ")
        tasks.append(new_task)
        print("New task added:", new_task)
    elif choice == "2":
        print("\n--- This feature is coming soon")
    elif choice == "3" or choice.lower() == "exit" or choice.lower() == "quit" or choice.lower() == "q":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")


# ------------- End of program ---------------- 
