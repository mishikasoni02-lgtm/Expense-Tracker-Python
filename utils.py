"""
utils.py
--------
Small helper functions used across the expense tracker project.
Keeping these separate keeps expense_manager.py and main.py clean.
"""

from datetime import datetime

# The date format used everywhere in this project (e.g. 2026-07-10)
DATE_FORMAT = "%Y-%m-%d"


def get_today_date():
    """Return today's date as a string in YYYY-MM-DD format."""
    return datetime.now().strftime(DATE_FORMAT)


def is_valid_date(date_text):
    """
    Check whether a string is a valid date in YYYY-MM-DD format.
    Returns True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_text, DATE_FORMAT)
        return True
    except ValueError:
        return False


def is_valid_amount(amount_text):
    """
    Check whether a string can be converted into a positive number.
    Returns True if valid, False otherwise.
    """
    try:
        amount = float(amount_text)
        return amount > 0
    except ValueError:
        return False


def get_valid_date_input(prompt="Date (YYYY-MM-DD) [Enter for today]: "):
    """
    Ask the user for a date until a valid one is given.
    Pressing Enter without typing anything uses today's date.
    """
    while True:
        date_text = input(prompt).strip()

        # Empty input means "use today's date"
        if date_text == "":
            return get_today_date()

        if is_valid_date(date_text):
            return date_text

        print("Invalid date format. Please use YYYY-MM-DD (e.g. 2026-07-10).")


def get_valid_amount_input(prompt="Amount: "):
    """
    Ask the user for an amount until a valid positive number is given.
    """
    while True:
        amount_text = input(prompt).strip()

        if is_valid_amount(amount_text):
            return round(float(amount_text), 2)

        print("Invalid amount. Please enter a positive number (e.g. 250 or 99.50).")


def get_non_empty_input(prompt):
    """
    Ask the user for text input until something other than blank is given.
    Used for fields like Category and Description that shouldn't be empty.
    """
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("This field cannot be empty. Please try again.")


def print_table(expenses):
    """
    Print a list of expense dictionaries as a neat table.
    Each expense dict is expected to have: id, date, category, description, amount
    """
    if not expenses:
        print("\nNo expenses to display.\n")
        return

    # Column widths chosen to comfortably fit typical data
    header = f"{'ID':<5}{'Date':<12}{'Category':<15}{'Description':<25}{'Amount':>10}"
    print("\n" + header)
    print("-" * len(header))

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<12}"
            f"{expense['category']:<15}"
            f"{expense['description'][:24]:<25}"
            f"{float(expense['amount']):>10.2f}"
        )
    print()
