# To-Do List Application

This is a command-line to-do list application written in Python. It allows users to manage their daily tasks right from the terminal. The project is a practical exercise in learning fundamental programming concepts, data persistence, and refactoring.

## Core Features

The application supports full CRUD (Create, Read, Update, Delete) operations for managing tasks. Each task is stored with a **title**, **priority** (High, Medium, Low), and a **due date**.

* **Create**: Add a new, detailed task to the list.
* **Read**: View all the tasks with their priority and due date.
* **Update**: Modify an existing task's details.
* **Delete**: Remove a task from the list.
* **Persistence**: Tasks are saved to a `tasks.csv` file, so they are not lost when the application closes.

## Project Evolution & Concepts Learned

This project evolved through several key stages, each introducing a new core programming concept.

### 1. In-Memory CRUD
The application started as a simple in-memory list of strings. This established the foundational Create, Read, Update, and Delete logic. At this stage, all data was lost when the program exited.

### 2. Simple File Persistence (`.txt`)
The first major feature was persistence. The list of tasks (as strings) was saved to a `tasks.txt` file. This involved learning fundamental file I/O operations in Python: `open()`, `file.write()`, and `file.readlines()`.

### 3. Refactoring to Structured Data (Dictionaries)
To support more detailed tasks, the data structure was refactored from a simple list of strings to a **list of dictionaries**. Each dictionary holds multiple pieces of information (`title`, `priority`, `due_date`), making the application more powerful.

### 4. Robust Persistence with the `csv` Module
Saving dictionaries to a plain text file manually was brittle and could break if a task title contained a comma. The project was refactored a second time to use Python's built-in `csv` module. This introduced a more robust, professional method for handling structured data and taught the importance of using standard libraries to handle common edge cases.

## Next Objective: Task Completion
The next feature to be implemented is the ability to mark tasks as "complete." This will involve:
1.  Adding a `status` field to the task data structure.
2.  Creating a new function to update a task's status.
3.  Updating the display to visually distinguish between complete and incomplete tasks.

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