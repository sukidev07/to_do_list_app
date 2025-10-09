# choices.py

# module for to_do_list_app
import csv

# refaactor main.py splitting out code into functions.
# choices add, remove, list, append, quit

# ---------------- Save Tasks ------------------------

def save_tasks(tasks, filename="tasks.csv"):
    # save the list of tasks to a CSV file
    with open(filename, "w", newline="") as file:
        # define the column names for the CSV file
        fieldnames = ["title", "priority", "due_date", "status"]
       
        # create a DictWriter object to write dictionaries to the CSV file
        writer = csv.DictWriter(file, fieldnames=fieldnames)
       
        # write the header row to the CSV file
        writer.writeheader()

        # write each task as a row in the CSV file
        writer.writerows(tasks)

    return f"Tasks saved to: {filename}."

# ---------------- Load Tasks ------------------------
def load_tasks(filename="tasks.csv"):
    tasks = []
    try:
        with open(filename, "r") as file:
            # read the CSV file as a list of dictionaries
            reader = csv.DictReader(file)
            tasks = list(reader)
        return tasks, f"Tasks loaded from: {filename}."
        # print("Tasks loaded from", filename)
    except FileNotFoundError:
        return tasks, f"No existing task file found. Starting with an empty task list."
        # print("No existing task file found. Starting with an empty task list.")
    except Exception as e:
        return tasks, f"An error occurred while loading tasks: {e}"
        # print("An error occurred while loading tasks:", e)

# ---------------- Validate Date ------------------------
def validate_date(date_str):
        from datetime import datetime
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

# ---------------- Validate Inputs ------------------------
def validate_inputs(input_title, input_priority, input_due_date):
        # Get title, priority, due date from user
        while True:
            input_title = input("Enter the task title: ")
            if input_title.strip() == "":
                print("Task title cannot be empty. Please enter a valid title.")
            else:
                break

        while True:
            input_priority = input("Enter the task priority (Low, Medium, High): ").upper()
            if input_priority not in ["LOW", "MEDIUM", "HIGH"]:
                print("Invalid priority. Please enter Low, Medium, or High.")
            else:
                break

        while True:
            input_due_date = input("Enter the due date (YYYY-MM-DD): ")
            if not validate_date(input_due_date):
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            else:
                break

        return input_title, input_priority, input_due_date
# ---------------- Add Task --------------------------
def add_task(tasks):
        # get and add validated user input from validate_inputs function to add_task function
        title, priority, due_date = validate_inputs(input_title="", input_priority="", input_due_date="")

        # create a new task dictionary
        new_task = {
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "status": "Pending"
        }

        # task added to dictionary list
        tasks.append(new_task)
        # print confirmation of what we just added
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
            status_marker = "[X]" if task.get("status") == "Completed" else "[ ]"
            # f string to format the output of the task list
            task_list_string += f"{index}. {status_marker} Title: {task['title']}, Priority: {task['priority']}, Due Date: {task['due_date']}\n"
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
                # get user input from validate_inputs
                update_title, update_priority, update_due_date = validate_inputs(input_title="", input_priority="", input_due_date="")
                # gets the tasks list, validates  against input of task_to_update - 1 to get the correct index number
                # then adds thew new information from update_task to tasks at the proper index
                tasks[task_to_update - 1] = {"title": update_title, "priority": update_priority, "due_date": update_due_date}
                return f"Task '{task_to_update}' has been updated: '{tasks[task_to_update - 1]}'"
                #print(f"Task {task_to_update} has been updated to: {update_task}")
                #print("Task updated successfully!")
            else:
                return "Invalid task number. No task updated."
        except ValueError:
            return "Invalid input. Please enter a valid task number."

# ----------------- Mark Task as Completed ------------------------
def mark_task_completed(tasks):
        if not tasks:
            return "No tasks found."
        
        # called the list_task(tasks) function because it repeats 
        # gets and returns the list more DRY
        return_task_list = list_tasks(tasks)
        print(return_task_list)

        try:
            # Ask user which task they would like to mark as completed
            task_to_mark = int(input("Enter the number of the task to mark as completed: "))

            # error_handling check to validate
            # use of the len() function to review the list and range the range starting at index 0
            if 1 <= task_to_mark <= len(tasks):
                # validate -1 task since you know, we start at 0, but people think 1-100 not 0-99 
                tasks[task_to_mark - 1]['status'] = 'Completed'
                return f"Task '{task_to_mark}' has been marked as completed."
                #print(f"Task {task_to_mark} has been marked as completed.")
                #print("Task marked as completed successfully!")
            else:
                return "Invalid task number. No task marked as completed."
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
                return f"Task '{task_to_delete}' has been deleted: '{deleted_task}'"
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