
# Python Expense Tracker (CLI)

A beginner-friendly command-line Expense Tracker built using Python. This project helps users manage daily expenses through a simple terminal-based interface.

Expense records are stored in a CSV file using Python's built-in CSV and file-handling functionality.

## Project Overview

The Expense Tracker allows users to add, view, search, edit, and delete expenses. It also provides a monthly summary with category-wise expense analysis.

This project demonstrates basic Python programming concepts, file handling, CSV operations, input validation, and modular code organization.

## Features

1. **Add Expense** – Add an expense with date, category, description, and amount.
2. **View Expenses** – Display all recorded expenses in a formatted table.
3. **Search Expenses** – Search by category, date, or description keyword.
4. **Edit Expense** – Update an existing expense using its ID.
5. **Delete Expense** – Delete an expense after confirmation.
6. **Monthly Summary** – View monthly expense statistics, including:
   - Total expenses
   - Number of transactions
   - Highest expense
   - Lowest expense
   - Average expense
7. **Category-wise Breakdown** – View the total amount spent in each category for a selected month.
8. **CSV Storage** – Automatically create and manage expense records in a CSV file.

## Technologies Used

- Python
- CSV Module
- OS Module
- File Handling
- Git and GitHub

## Project Structure

```text
expense-tracker-cli/
│
├── main.py
├── expense_manager.py
├── utils.py
├── .gitignore
└── README.md
```

The `expenses.csv` file is generated automatically when the program runs and is excluded from Git tracking.

## How to Run

### 1. Install Python

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the Project Folder

```bash
cd expense-tracker-cli
```

### 4. Run the Application

```bash
python main.py
```

### 5. Use the Menu

Follow the instructions displayed in the terminal to manage your expenses.

## Example Output

```text
===== EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Search Expense
4. Edit Expense
5. Delete Expense
6. Monthly Summary
7. Exit

Choose an option (1-7): 6

--- Monthly Summary ---
Enter month to summarize (YYYY-MM): 2026-11

Summary for 2026-11
------------------------------
Total expenses:     1500.00
Number of records:  3
Highest expense:    800.00
Lowest expense:     200.00
Average expense:    500.00

Category-wise Breakdown:
Food: 800.00
Travel: 500.00
Shopping: 200.00
```

*Example output is illustrative.*

## Learning Objectives

Through this project, I have practiced:

- Python functions and modules
- Lists and dictionaries
- Loops and conditional statements
- Reading and writing CSV files
- Basic CRUD operations
- Input validation and error handling
- Organizing code into separate modules
- Using Git and GitHub for version control

## Future Improvements

- Export monthly reports to a text or CSV file.
- Add date-range filtering.
- Improve the terminal interface.
- Add graphical data visualization.

## Note

This repository is based on a forked beginner project and has been used for learning, testing, and customization. Original project attribution is retained.
