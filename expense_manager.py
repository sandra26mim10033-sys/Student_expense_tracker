from data_manager import load_expenses, save_expenses
from validator import is_valid_amount, is_valid_name
from category_manager import get_category
from report_manager import category_totals  
def add_expense():
    """Add one new expense."""
    name = input("What did you spend money on? ")
    amount = input("How much did you spend? ")

    if not is_valid_name(name):
        print("Please enter a valid expense name.")
        return

    if not is_valid_amount(amount):
        print("Please enter a valid expense amount.")
        return
    amount = float(amount)

    expense = {
        "name": name,
        "amount": amount,
        "category": get_category(name)
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def show_expenses():
    """Show all the expenses."""
    expenses = load_expenses()

    if not expenses:
        print("You haven't added any expenses yet.")
        return

    print("\nYour Expenses")
    print("-" * 30)

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']} - ₹{expense['amount']:.2f - {expense.get('category', 'Other')}}")


def show_total():
    """Calculate and show the total spending."""
    expenses = load_expenses()
    totals = category_totals(expenses)
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal spending: ₹{total:.2f}")
    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")
def delete_expense():
    """Delete an expense."""

    expenses = load_expenses()

    if not expenses:
        print("You haven't added any expenses yet.")
        return

    print("\nYour Expenses")
    print("-" * 30)

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']} - ₹{expense['amount']:.2f}")

    try:
        choice = int(input("Which expense number would you like to delete? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice < 1 or choice > len(expenses):
        print("Please choose a valid expense number.")
        return

    deleted = expenses.pop(choice - 1)
    save_expenses(expenses)

    print(f"Deleted: {deleted['name']}")