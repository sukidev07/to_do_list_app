# main.py

# Creating a list management application for tracking tasks.
# Key concepts to learn CRUD: Create Read Update Delete
# imports
import choices

# ------------- Start of program ----------------

# Load existing tasks from file at the start of the program
tasks, load_message = choices.load_tasks()
print(load_message)
print()
print("Welcome to the To-Do List App!")
print("==============================")
# Starting a loop so we can keep the program running to add multiple tasks
while True:
    print("\nSelect an option:")
    print("-----------------")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Mark task as completed")
    print("5. Delete task")
    print("6. Exit")
    print("-----------------")
    choice = input("Enter your choice (1-6): ")

#---------------- Add Task --------------------------
    if choice == "1":
        new_task = choices.add_task(tasks)
        print("New task added:", new_task)
        choices.save_tasks(tasks)

#---------------- List Tasks ------------------------
    elif choice == "2":
        all_the_tasks = choices.list_tasks(tasks)
        print(all_the_tasks)

#
#---------------- Update Task ------------------------
    elif choice == "3":
        update_task = choices.update_task(tasks)
        print(update_task)
        if "updated" in update_task:
            choices.save_tasks(tasks)

#---------------- Mark Task as Completed ------------------------
    elif choice == "4":
        mark_completed = choices.mark_task_completed(tasks)
        print(mark_completed)
        if "marked as completed" in mark_completed:
            choices.save_tasks(tasks)
#---------------- Delete Task ------------------------
    elif choice == "5":
        delete_task = choices.delete_task(tasks)
        print(delete_task)
        if "deleted" in delete_task:
            choices.save_tasks(tasks)

#---------------- End/Quit Program ----------------------------
    elif choice == "6" or choice.lower() == "exit" or choice.lower() == "quit"  or choice.lower() == "q":
        end_program = choices.exit_program()
        print(end_program)
        break
    else:
        print("Invalid choice. Please select a valid option.")

# ------------- End of program ---------------- 
