
"""
utils.py
--------
Small helper functions used across the expense tracker project.
Handles date validation, amount validation, and table formatting.
"""

from datetime import datetime
import math

DATE_FORMAT = "%Y-%m-%d"


def get_today_date():
    """Return today's date in YYYY-MM-DD format."""
    return datetime.now().strftime(DATE_FORMAT)


def is_valid_date(date_text):
    """Check whether the given date is valid."""
    try:
        datetime.strptime(date_text, DATE_FORMAT)
        return True
    except ValueError:
        return False


def is_valid_amount(amount_text):
    """Check whether the amount is a valid positive number."""
    try:
        amount = float(amount_text)

        if not math.isfinite(amount):
            return False

        return amount > 0

    except (ValueError, TypeError):
        return False


def get_valid_date_input(prompt="Date (YYYY-MM-DD) [Enter for today]: "):
    """Ask for a valid date. Enter uses today's date."""

    while True:
        date_text = input(prompt).strip()

        if date_text == "":
            return get_today_date()

        if is_valid_date(date_text):
            return date_text

        print("Invalid date. Please use YYYY-MM-DD (e.g. 2026-07-10).")


def get_valid_amount_input(prompt="Amount: "):
    """Ask for a valid positive expense amount."""

    while True:
        amount_text = input(prompt).strip()

        if is_valid_amount(amount_text):
            return round(float(amount_text), 2)

        print("Invalid amount. Please enter a positive number (e.g. 250 or 99.50).")


def get_non_empty_input(prompt):
    """Ask for input until the user enters non-empty text."""

    while True:
        text = input(prompt).strip()

        if text:
            return text

        print("This field cannot be empty. Please try again.")


def print_table(expenses):
    """Display expenses in a formatted table."""

    if not expenses:
        print("\nNo expenses to display.\n")
        return

    id_width = 5
    date_width = 12
    category_width = 18
    description_width = 25
    amount_width = 12

    header = (
        f"{'ID':<{id_width}}"
        f"{'Date':<{date_width}}"
        f"{'Category':<{category_width}}"
        f"{'Description':<{description_width}}"
        f"{'Amount':>{amount_width}}"
    )

    print("\n" + header)
    print("-" * len(header))

    for expense in expenses:
        print(
            f"{str(expense['id']):<{id_width}}"
            f"{expense['date']:<{date_width}}"
            f"{expense['category'][:category_width - 1]:<{category_width}}"
            f"{expense['description'][:description_width - 1]:<{description_width}}"
            f"{float(expense['amount']):>{amount_width}.2f}"
        )

    print()
