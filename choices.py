# choices.py

# refaactor main.py splitting out code into functions.
# choices add, remove, list, append, quit

# ---------------- Add Task --------------------------
def add_task(tasks):
        # Add a task | get a user input store in new_task
        new_task = input("Please add a new task: ")
        # tasks is are list we are appending the tasks with (new_task) that we just got from the user input
        tasks.append(new_task)
        # print configraiton of what we just added
        print("New task added:", new_task)

# ---------------- List Tasks ------------------------
def list_tasks(tasks):
        print("\n--- Task List ---")
        if not tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

# ---------------- Update Task ------------------------
# oops I miss typed my add task lets ammend it
# # task update operation so we can update inline instead of deleting and shifting the list operation
def update_task(tasks):
        print("\n--- Update a task ---")
        if not tasks:
            # error_handling for an empty list - move on
            print("No tasks found.")
        else:
            # reuse of the same logic as add, list and delete
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                # Ask user which task they would like to update
            try:
                # Ask user which task they would like to update
                task_to_update = int(input("Enter the number of the task to update: "))
                # error_handling check to validate
                # validates against the len() function to check tasks list total amount
                if 1 <= task_to_update <= len(tasks):
                    # validate
                    # gets the new updated value to be used to replace the specified index
                    update_task = input("Enter the updated task: ")
                    # gets the tasks list, validates  against input of task_to_update - 1 to get the correct index number
                    # then adds thew new information from update_task to tasks at the proper index
                    tasks[task_to_update - 1] = update_task
                    print(f"Task {task_to_update} has been updated to: {update_task}")
                    print("Task updated successfully!")
                else:
                    print("Invalid task number. No task updated.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

    
# ---------------- Delete Task ------------------------
# delete operation to list the current tasks in an ordered number list
# validate an empty list before continueing
# request the user to input and validate the request can done
def delete_task(tasks):
        print("\n--- Delete a task ---")
        if not tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                # Ask user which task they would like to delete
                task_to_delete = int(input("Enter the number of the task to delete: "))

                # error_handling check to validate
                # use of the len() function to review the list and range the range starting at index 0
                if 1 <= task_to_delete <= len(tasks):
                    # validate -1 task since you know, we start at 0, but people think 1-100 not 0-99 
                    # use of the pop() function to get the index number -1 and perform 2 action 
                    # 1. to get the object string value to print {deleted_task} 
                    # 2. actually remove pop() specified index from the list in tasks
                    deleted_task = tasks.pop(task_to_delete - 1)
                    print(f"Task '{deleted_task}' has been deleted.")
                else:
                    print("Invalid task number. No task deleted.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
    
# ----------------- End/Quit Program ----------------------------
def exit_program():
        print("Exiting the program. Goodbye!")
    # catch to show invalid input if the yester fails to select an of the correct options