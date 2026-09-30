import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    """Load saved expenses from the file."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """Save expenses so they are available next time."""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)