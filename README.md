# Student Expense Tracker

## About

This is a simple Student Expense Tracker project that I made using Python.

I made this project because I wanted to create something useful for keeping track of daily expenses. As a student, we spend money on different things like food, travelling, books and other small expenses, and sometimes it is difficult to keep track of all of them.

This program lets me add my expenses, view them, check how much I have spent, and delete an expense if I don't need it anymore.

I also added categories so that expenses can be grouped into things like Food, Travel and Education.

## Features

The main things my project can do are:

- Add an expense
- View all expenses
- Calculate total spending
- Delete an expense
- Automatically add a category to an expense
- Show spending category-wise
- Check if the entered expense amount is valid
- Save expenses in a JSON file
- Run tests for some parts of the program

## How It Works

When I run the program, it shows a simple menu in the terminal.

The user can select an option from the menu, for example adding an expense or viewing the expenses.

When adding an expense, the program asks for the name and amount. It then checks if the input is valid and saves the expense.

The category is decided based on the expense name. For example, if I enter "lunch", it is added to the Food category.

The expenses are stored in `expenses.json`, so the data does not disappear when the program is closed.

## Technologies I Used

- Python
- JSON
- unittest
- VS Code
- Git and GitHub

## Project Files

I divided the project into different files so that the code is easier to understand and manage.

- `main.py` - contains the main menu
- `expense_manager.py` - handles the main expense operations
- `data_manager.py` - saves and loads expense data
- `validator.py` - checks user input
- `category_manager.py` - decides the expense category
- `report_manager.py` - creates the category-wise spending report
- `test_tracker.py` - contains the tests
- `expenses.json` - stores the expense data

## Running the Project

To run the project, I open the project folder in VS Code and open the terminal.

Then I run:

```text
python main.pys