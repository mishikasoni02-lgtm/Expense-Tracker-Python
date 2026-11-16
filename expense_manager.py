
"""
expense_manager.py
-------------------
Handles all the logic for reading and writing expenses to the CSV file.
This is the "engine" of the project - main.py just calls these functions.
"""

import csv
import os

from utils import (
    get_valid_date_input,
    get_valid_amount_input,
    get_non_empty_input,
    print_table,
)

CSV_FILE = "expenses.csv"

FIELDNAMES = ["id", "date", "category", "description", "amount"]


def initialize_csv():
    """Create expenses.csv with headers if it doesn't already exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_all_expenses():
    """Read all expenses from the CSV file and return them as a list."""
    initialize_csv()

    expenses = []
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("id"):
                expenses.append(row)

    return expenses


def write_all_expenses(expenses):
    """Overwrite the CSV file with the given list of expenses."""
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def get_next_id(expenses):
    """Return the next available expense ID."""
    if not expenses:
        return 1

    existing_ids = [int(expense["id"]) for expense in expenses]
    return max(existing_ids) + 1


def add_expense():
    """Ask the user for expense details and add a new expense."""
    print("\n--- Add New Expense ---")

    date = get_valid_date_input()
    category = get_non_empty_input("Category: ")
    description = get_non_empty_input("Description: ")
    amount = get_valid_amount_input()

    expenses = read_all_expenses()
    new_id = get_next_id(expenses)

    new_expense = {
        "id": new_id,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }

    initialize_csv()
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(new_expense)

    print(f"Expense added successfully! (ID: {new_id})")


def view_expenses():
    """Display all expenses sorted by ID."""
    print("\n--- All Expenses ---")

    expenses = read_all_expenses()
    expenses.sort(key=lambda e: int(e["id"]))

    print_table(expenses)


def search_expenses():
    """Search expenses by category, date, or description."""
    print("\n--- Search Expenses ---")
    print("1. Search by Category")
    print("2. Search by Date")
    print("3. Search by Description keyword")

    choice = input("Choose an option (1-3): ").strip()

    expenses = read_all_expenses()
    results = []

    if choice == "1":
        keyword = input("Enter category: ").strip().lower()
        results = [
            e for e in expenses
            if keyword in e["category"].lower()
        ]

    elif choice == "2":
        keyword = input("Enter date (YYYY-MM-DD): ").strip()
        results = [
            e for e in expenses
            if keyword == e["date"]
        ]

    elif choice == "3":
        keyword = input("Enter description keyword: ").strip().lower()
        results = [
            e for e in expenses
            if keyword in e["description"].lower()
        ]

    else:
        print("Invalid option.")
        return

    print(f"\nFound {len(results)} matching expense(s).")
    print_table(results)


def find_expense_by_id(expenses, expense_id):
    """Find an expense using its ID."""
    for expense in expenses:
        if int(expense["id"]) == expense_id:
            return expense

    return None


def edit_expense():
    """Edit an existing expense."""
    print("\n--- Edit Expense ---")

    expenses = read_all_expenses()

    if not expenses:
        print("No expenses available to edit.")
        return

    print_table(expenses)

    try:
        expense_id = int(input("Enter the ID of the expense to edit: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    expense = find_expense_by_id(expenses, expense_id)

    if expense is None:
        print(f"No expense found with ID {expense_id}.")
        return

    print("\nLeave a field blank to keep its current value.")

    # Date
    new_date = input(f"Date [{expense['date']}]: ").strip()

    if new_date != "":
        from utils import is_valid_date

        if is_valid_date(new_date):
            expense["date"] = new_date
        else:
            print("Invalid date format, keeping the old date.")

    # Category
    new_category = input(f"Category [{expense['category']}]: ").strip()

    if new_category != "":
        expense["category"] = new_category

    # Description
    new_description = input(
        f"Description [{expense['description']}]: "
    ).strip()

    if new_description != "":
        expense["description"] = new_description

    # Amount
    new_amount = input(f"Amount [{expense['amount']}]: ").strip()

    if new_amount != "":
        from utils import is_valid_amount

        if is_valid_amount(new_amount):
            expense["amount"] = round(float(new_amount), 2)
        else:
            print("Invalid amount, keeping the old amount.")

    write_all_expenses(expenses)

    print("Expense updated successfully!")


def delete_expense():
    """Delete an expense after user confirmation."""
    print("\n--- Delete Expense ---")

    expenses = read_all_expenses()

    if not expenses:
        print("No expenses available to delete.")
        return

    print_table(expenses)

    try:
        expense_id = int(input("Enter the ID of the expense to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    expense = find_expense_by_id(expenses, expense_id)

    if expense is None:
        print(f"No expense found with ID {expense_id}.")
        return

    confirm = input(
        f"Are you sure you want to delete expense {expense_id} "
        f"({expense['category']} - {expense['amount']})? (y/n): "
    ).strip().lower()

    if confirm == "y":
        expenses.remove(expense)
        write_all_expenses(expenses)
        print("Expense deleted successfully!")
    else:
        print("Delete cancelled.")


def monthly_summary():
    """Show monthly expense summary with category-wise breakdown."""

    print("\n--- Monthly Summary ---")
    month = input("Enter month to summarize (YYYY-MM): ").strip()

    expenses = read_all_expenses()

    monthly_expenses = [
        e for e in expenses
        if e["date"].startswith(month)
    ]

    if not monthly_expenses:
        print(f"No expenses found for {month}.")
        return

    amounts = [
        float(e["amount"])
        for e in monthly_expenses
    ]

    total = sum(amounts)
    count = len(amounts)
    highest = max(amounts)
    lowest = min(amounts)
    average = total / count

    category_totals = {}

    for expense in monthly_expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print(f"\nSummary for {month}")
    print("-" * 30)
    print(f"Total expenses:     {total:.2f}")
    print(f"Number of records:  {count}")
    print(f"Highest expense:    {highest:.2f}")
    print(f"Lowest expense:     {lowest:.2f}")
    print(f"Average expense:    {average:.2f}")

    print("\nCategory-wise Breakdown:")

    for category, amount in category_totals.items():
        print(f"{category}: {amount:.2f}")

    print()
