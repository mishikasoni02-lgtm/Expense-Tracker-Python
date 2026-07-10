"""
main.py
-------
Entry point for the Expense Tracker application.
Shows the main menu and calls functions from expense_manager.py
based on the user's choice.

Run this file to start the program:
    python main.py
"""

from expense_manager import (
    initialize_csv,
    add_expense,
    view_expenses,
    search_expenses,
    edit_expense,
    delete_expense,
    monthly_summary,
)


def print_menu():
    """Display the main menu options."""
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Monthly Summary")
    print("7. Exit")
    print("============================")


def main():
    """Main program loop. Keeps running until the user chooses to exit."""
    # Make sure the CSV file exists before doing anything else
    initialize_csv()

    while True:
        print_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            edit_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            monthly_summary()
        elif choice == "7":
            print("\nThanks for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
