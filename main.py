# main.py

# Creating a list management application for tracking tasks.
# Key concepts to learn CRUD: Create Read Update Delete
# importss
import choices

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
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

#---------------- Add Task --------------------------
    if choice == "1":
        choices.add_task(tasks)

#---------------- List Tasks ------------------------
    elif choice == "2":
        choices.list_tasks(tasks)

#---------------- Update Task ------------------------
    elif choice == "3":
        choices.update_task(tasks)

#---------------- Delete Task ------------------------
    elif choice == "4":
        choices.delete_task(tasks)

#---------------- End/Quit Program ----------------------------
    elif choice == "5" or choice.lower() == "exit" or choice.lower() == "quit"  or choice.lower() == "q":
        choices.exit_program()
        break
    else:
        print("Invalid choice. Please select a valid option.")


# ------------- End of program ---------------- 
