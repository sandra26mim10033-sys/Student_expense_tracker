from expense_manager import add_expense, show_expenses, show_total, delete_expense

def show_menu():
    print("\n===== Student Expense Tracker =====")
    print("1. Add an expense")
    print("2. View my expenses")
    print("3. See total spending")
    print("4. Delete an expense")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("What would you like to do? ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("Thanks for using Student Expense Tracker!")
            break

        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
