# To-Do List Application

This is a command-line to-do list application written in Python. It allows users to manage their daily tasks right from the terminal. The project is a practical exercise in learning fundamental programming concepts and Python development.

## Core Features Implemented

The application currently supports full in-memory CRUD (Create, Read, Update, Delete) operations for managing tasks.

* **Create**: Add a new task to the list.
* **Read**: View all the tasks currently on the list.
* **Update**: Modify an existing task.
* **Delete**: Remove a task from the list.

The program runs in a continuous loop, allowing the user to perform multiple actions in a single session. All application logic is neatly organized into functions within the `choices.py` module.

## Next Objective: File Persistence

The current list of tasks is stored in memory, which means all tasks are lost when the program closes. The next major goal is to implement **persistence**. This will involve:

1.  **Saving Tasks**: Writing the current list of tasks to a text file (`tasks.txt`).
2.  **Loading Tasks**: Reading from `tasks.txt` when the application starts up, so the user's session can be restored.

This will be the first step in making the application a truly useful, long-term task manager.

### git update guide:
-----------------------------------
Common types include:
    feat: (a new feature)
    fix: (a bug fix)
    refactor: (changing code structure without changing its behavior)
    docs: (updating comments or documentation)

Examples:
    feat: Add dynamic skill level selection
    fix: Prevent crash on non-numeric user input
    refactor: Move game logic functions into separate modules
    docs: Add comments explaining main game loop