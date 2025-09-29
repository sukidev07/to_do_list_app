# choices.py

# refaactor main.py splitting out code into functions.
# choices add, remove, list, append, quit

# ---------------- Save Tasks ------------------------

def save_tasks(tasks, filename="tasks.txt"):
    # open a new or existing file tasks.txt created locally in the path.
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
        return f"Tasks saved to {filename}."
    # print("Tasks saved to", filename)

# ---------------- Load Tasks ------------------------
def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks, f"Tasks loaded from {filename}."
        # print("Tasks loaded from", filename)
    except FileNotFoundError:
        return tasks, f"No existing task file found. Starting with an empty task list."
        # print("No existing task file found. Starting with an empty task list.")
    except Exception as e:
        return tasks, f"An error occurred while loading tasks: {e}"
        # print("An error occurred while loading tasks:", e)

# ---------------- Add Task --------------------------
def add_task(tasks):
        # Add a task | get a user input store in new_task
        new_task = input("Please add a new task: ")
        # tasks is are list we are appending the tasks with (new_task) that we just got from the user input
        tasks.append(new_task)
        # print configraiton of what we just added
        return new_task
        # print("New task added:", new_task)

# ---------------- List Tasks ------------------------
def list_tasks(tasks):
        
        # changed order to return false before showing task list
        if not tasks:
            return "No tasks found."
        
        # setting var for task list to be defined once found.
        task_list_string = "\n--- Task List ---\n"

        # can remove the else and go into loop, we validated first, now do a task.
        for index, task in enumerate(tasks, start=1):
             task_list_string += f"{index}. {task}\n"
        return task_list_string


# ---------------- Update Task ------------------------
# oops I miss typed my add task lets ammend it
# # task update operation so we can update inline instead of deleting and shifting the list operation
def update_task(tasks):
        if not tasks:
            return "No tasks found."
        # called the list_task(tasks) function because it repeats 
        # gets and returns the list more DRY
        return_task_list = list_tasks(tasks)
        print(return_task_list)
        
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
                return f"Task '{task_to_update}' has been updated to: '{update_task}'"
                #print(f"Task {task_to_update} has been updated to: {update_task}")
                #print("Task updated successfully!")
            else:
                return "Invalid task number. No task updated."
        except ValueError:
            return "Invalid input. Please enter a valid task number."

    
# ---------------- Delete Task ------------------------
# delete operation to list the current tasks in an ordered number list
# validate an empty list before continueing
# request the user to input and validate the request can done
def delete_task(tasks):
       
        if not tasks:
            return "No tasks found."
        
        # called the list_task(tasks) function because it repeats 
        # gets and returns the list more DRY
        return_task_list = list_tasks(tasks)
        print(return_task_list)

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
                return f"Task '{task_to_delete}' has been deleted: {deleted_task}"
                #print(f"Task {task_to_delete} has been deleted.")
                #print("Task deleted successfully!")
            else:
                return "Invalid task number. No task deleted."
        except ValueError:
            return "Invalid input. Please enter a valid task number."
# ----------------- End/Quit Program ----------------------------
def exit_program():
        return "Exiting the program. Goodbye!"
    # catch to show invalid input if the yester fails to select an of the correct options