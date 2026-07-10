# Expense Tracker (Python CLI Project)

A simple, beginner-friendly command-line Expense Tracker built entirely with
Python's built-in modules (`csv`, `os`, `datetime`). No database, no external
libraries — just clean, readable Python.

## Description

This project lets you track your daily expenses from the terminal. All data
is stored in a plain CSV file (`expenses.csv`), so it's easy to inspect,
back up, or even open in Excel/Google Sheets. It's a great example project
for learning file handling, CSV operations, input validation, and writing
modular Python code.

## Features

1. **Add Expense** – Enter a date (or press Enter for today), category,
   description, and amount. Input is validated before saving.
2. **View All Expenses** – See every expense in a neatly formatted table.
3. **Search Expense** – Search by category, exact date, or a description
   keyword (case-insensitive, partial match supported).
4. **Edit Expense** – Update any field of an existing expense by its ID.
   Leave a field blank to keep its current value.
5. **Delete Expense** – Remove an expense by ID, with a confirmation prompt.
6. **Monthly Summary** – Enter a month (YYYY-MM) to see:
   - Total expenses
   - Number of transactions
   - Highest expense
   - Lowest expense
   - Average expense
7. **Exit** – Cleanly exit the program.

### Error handling
- `expenses.csv` is created automatically if it doesn't exist.
- Invalid dates, amounts, and menu choices are caught and re-prompted
  instead of crashing the program.
- An empty expense file is handled gracefully (no errors, just a friendly
  "no expenses" message).

## Folder Structure

```
expense_tracker/
│
├── main.py             # Entry point - shows the menu and routes user choices
├── expense_manager.py  # Core logic: add/view/search/edit/delete/summary
├── utils.py             # Helper functions: validation, formatting, date handling
├── expenses.csv          # Auto-created CSV file that stores all expense data
├── .gitignore            # Excludes __pycache__/ and expenses.csv from git
└── README.md            # Project documentation (this file)
```

> **Note:** `expenses.csv` is listed in `.gitignore` so your personal expense
> data doesn't get pushed to a public GitHub repo. The file is created
> automatically the first time you run the program, so nothing extra needs
> to be set up.

## How to Run

1. Make sure you have **Python 3.7+** installed. Check with:
   ```
   python3 --version
   ```
2. Download / unzip this project folder.
3. Open a terminal inside the `expense_tracker` folder.
4. Run the program:
   ```
   python3 main.py
   ```
   (On Windows, you can usually just use `python main.py`)
5. Follow the on-screen menu to add, view, search, edit, or delete expenses.

No installation of extra packages is required — everything used is part of
the Python standard library.

## Example Output

```
===== EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Search Expense
4. Edit Expense
5. Delete Expense
6. Monthly Summary
7. Exit
============================
Choose an option (1-7): 1

--- Add New Expense ---
Date (YYYY-MM-DD) [Enter for today]:
Category: Food
Description: Lunch at cafe
Amount: 250
Expense added successfully! (ID: 1)

===== EXPENSE TRACKER =====
...
Choose an option (1-7): 2

--- All Expenses ---

ID   Date        Category       Description                  Amount
-------------------------------------------------------------------
1    2026-07-10  Food           Lunch at cafe                250.00

===== EXPENSE TRACKER =====
...
Choose an option (1-7): 6

--- Monthly Summary ---
Enter month to summarize (YYYY-MM): 2026-07

Summary for 2026-07
------------------------------
Total expenses:     250.00
Number of records:  1
Highest expense:    250.00
Lowest expense:     250.00
Average expense:    250.00
```

## Notes for Beginners

- The project is split into three files so each one stays small and focused:
  - `utils.py` handles small reusable helpers (validation, formatting).
  - `expense_manager.py` handles reading/writing the CSV and the actual
    features (add, edit, delete, search, summary).
  - `main.py` just displays the menu and calls the right function.
- Feel free to open `expenses.csv` in a spreadsheet app to see your data.
- Try adding a new feature yourself, like exporting a summary to a text file!