# Project Statement

## Project Title

Student Expense Tracker

## Problem Statement

As a student, I spend money on different things like food, travelling, books and other daily expenses. It is easy to forget small expenses and lose track of how much money I have spent.

Because of this, I wanted to make a simple program that could help me keep track of my expenses without making the process complicated.

So I decided to create a Student Expense Tracker using Python.

The program allows me to add an expense, view my saved expenses, check my total spending and delete an expense when I make a mistake. I also added an automatic category system so that expenses can be grouped into categories such as Food, Travel, Education and Other.

## Scope of the Project

The main purpose of this project is to provide a simple way for students to record and check their daily expenses.

The project is currently a terminal-based Python application. It does not need a complicated setup or a database. The expenses are stored in a JSON file so that the saved data can be used again when the program is run.

The current version focuses on the basic expense tracking features. In the future, more features such as charts, monthly tracking, searching and a graphical interface can be added.

## Target Users

This project is mainly intended for:

- Students who want to track their daily spending
- People who want a simple expense tracking program
- Beginners who want to understand how a small Python project can be organized

## Objectives

The main objectives of this project are:

- To create a simple expense tracking application
- To allow users to add and view their expenses
- To calculate total spending
- To allow incorrect expenses to be deleted
- To organize expenses into categories
- To validate user input and handle incorrect entries
- To store expense data so that it is not lost when the program is closed
- To practice Python programming concepts such as functions, modules, file handling and testing

## High-Level Features

The main features of my project are:

- Add a new expense
- View all saved expenses
- Calculate total spending
- Delete an expense
- Automatically assign a category to an expense
- Show category-wise spending
- Validate expense names and amounts
- Save expenses in a JSON file
- Load previously saved expenses
- Run tests for important parts of the program

## Functional Requirements

The system should allow the user to:

1. Add an expense by entering its name and amount.
2. Check whether the entered expense information is valid.
3. Automatically assign a category based on the expense name.
4. Save the expense in the JSON file.
5. View the expenses that have already been saved.
6. Calculate and display the total amount spent.
7. Display spending based on categories.
8. Delete an expense selected by the user.
9. Exit the program using the menu.

## Non-Functional Requirements

I also considered some basic non-functional requirements while making the project.

### Usability

The program uses a simple menu so that a user can understand the available options easily.

### Error Handling

The program checks for invalid expense amounts, empty names and invalid menu or delete selections instead of allowing the program to crash.

### Reliability

The expense data is stored in a JSON file so that the data can be loaded again when the program is started.

### Maintainability

I divided the project into different Python files. For example, validation, data storage, categories and reports are handled separately instead of putting everything in one file.

### Performance

The project is designed for normal student-level expense records and uses simple operations to add, view, calculate and delete expenses.

### Resource Efficiency

The project uses a JSON file for storage and does not require a separate database or large external software.

## Project Structure

I divided the project into different modules so that each file has a specific responsibility.

- `main.py` - handles the main menu and program flow
- `expense_manager.py` - handles adding, viewing and deleting expenses
- `data_manager.py` - handles saving and loading JSON data
- `validator.py` - validates user input
- `category_manager.py` - assigns categories to expenses
- `report_manager.py` - calculates category-wise spending
- `test_tracker.py` - contains tests for important functions
- `expenses.json` - stores the expense data
- `README.md` - contains information about the project
- `statement.md` - contains the project statement

## Technologies Used

The project was made using:

- Python
- JSON
- Python `unittest`
- VS Code
- Git
- GitHub

## Testing

I created a separate test file called `test_tracker.py` using Python's `unittest`.

I tested some important parts of the project, including:

- Valid expense amounts
- Invalid expense amounts
- Valid expense names
- Empty expense names
- Expense category assignment

The tests can be run using:

`python -m unittest test_tracker.py`

## Expected Outcome

The expected outcome of this project is a working and simple expense tracker that can be used from the terminal.

A user should be able to enter expenses, view saved expenses, see the total spending, check category-wise spending and delete an expense when required.

The project should also handle common incorrect inputs without crashing.

## Future Improvements

If I continue working on this project, I would like to add:

- Monthly expense tracking
- Charts for showing spending
- Search and filter options
- More expense categories
- A graphical user interface
- Exporting expenses to Excel or CSV
- Better reports for comparing spending over time

## Conclusion

I started this project with the simple idea of making something that could be useful for students.

While building it, I learned how to divide a Python program into different modules, work with JSON files, validate user input, handle errors and write basic tests.

The current project covers the main expense tracking features, and I can improve it further by adding more advanced reporting and a graphical interface in the future.