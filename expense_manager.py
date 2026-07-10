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

# Name of the CSV file where all expenses are stored
CSV_FILE = "expenses.csv"

# Column names used in the CSV file
FIELDNAMES = ["id", "date", "category", "description", "amount"]


def initialize_csv():
    """
    Create expenses.csv with headers if it doesn't already exist.
    This makes sure the program never crashes because the file is missing.
    """
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_all_expenses():
    """
    Read all expenses from the CSV file and return them as a list of dicts.
    Handles the case where the file is empty or only has a header.
    """
    initialize_csv()  # safety net in case the file got deleted mid-run

    expenses = []
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Skip any completely blank rows
            if row.get("id"):
                expenses.append(row)
    return expenses


def write_all_expenses(expenses):
    """
    Overwrite the CSV file with the given list of expense dicts.
    Used after editing or deleting an expense.
    """
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def get_next_id(expenses):
    """
    Work out the next available ID by looking at existing expenses.
    Keeps IDs unique even after deletions.
    """
    if not expenses:
        return 1
    existing_ids = [int(expense["id"]) for expense in expenses]
    return max(existing_ids) + 1


def add_expense():
    """Ask the user for expense details and append a new row to the CSV."""
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

    # Append the new expense without rewriting the whole file
    initialize_csv()
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(new_expense)

    print(f"Expense added successfully! (ID: {new_id})")


def view_expenses():
    """Display every expense currently stored, sorted by ID."""
    print("\n--- All Expenses ---")
    expenses = read_all_expenses()
    expenses.sort(key=lambda e: int(e["id"]))
    print_table(expenses)


def search_expenses():
    """
    Let the user search expenses by category, date, or a description keyword.
    The search is case-insensitive and matches partial text.
    """
    print("\n--- Search Expenses ---")
    print("1. Search by Category")
    print("2. Search by Date")
    print("3. Search by Description keyword")
    choice = input("Choose an option (1-3): ").strip()

    expenses = read_all_expenses()
    results = []

    if choice == "1":
        keyword = input("Enter category: ").strip().lower()
        results = [e for e in expenses if keyword in e["category"].lower()]
    elif choice == "2":
        keyword = input("Enter date (YYYY-MM-DD): ").strip()
        results = [e for e in expenses if keyword == e["date"]]
    elif choice == "3":
        keyword = input("Enter description keyword: ").strip().lower()
        results = [e for e in expenses if keyword in e["description"].lower()]
    else:
        print("Invalid option.")
        return

    print(f"\nFound {len(results)} matching expense(s).")
    print_table(results)


def find_expense_by_id(expenses, expense_id):
    """Return the expense dict matching the given ID, or None if not found."""
    for expense in expenses:
        if int(expense["id"]) == expense_id:
            return expense
    return None


def edit_expense():
    """Let the user edit an existing expense by its ID."""
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
    new_description = input(f"Description [{expense['description']}]: ").strip()
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
    """Let the user delete an expense by its ID, after confirmation."""
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
    """
    Show a summary of expenses for a month chosen by the user.
    Includes total, count, highest, lowest, and average expense.
    """
    print("\n--- Monthly Summary ---")
    month = input("Enter month to summarize (YYYY-MM): ").strip()

    expenses = read_all_expenses()
    # Match expenses whose date starts with the given YYYY-MM
    monthly_expenses = [e for e in expenses if e["date"].startswith(month)]

    if not monthly_expenses:
        print(f"No expenses found for {month}.")
        return

    amounts = [float(e["amount"]) for e in monthly_expenses]

    total = sum(amounts)
    count = len(amounts)
    highest = max(amounts)
    lowest = min(amounts)
    average = total / count

    print(f"\nSummary for {month}")
    print("-" * 30)
    print(f"Total expenses:     {total:.2f}")
    print(f"Number of records:  {count}")
    print(f"Highest expense:    {highest:.2f}")
    print(f"Lowest expense:     {lowest:.2f}")
    print(f"Average expense:    {average:.2f}")
    print()
