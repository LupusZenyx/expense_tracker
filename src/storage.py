import csv
import os
from expense import Expense

# Define the file paths for storing expense data
EXPENSES_CSV_FILE = os.path.join("data", "expenses.csv")

def load_expenses():
    """
    Load expense data from the CSV file and return it as a list of Expense objects.

    Returns:
        list of Expense: List of expense objects.
    """
    expenses = []

    # Check if the CSV file exists
    if not os.path.exists(EXPENSES_CSV_FILE):
        return expenses

    # Read expense data from the CSV file
    with open(EXPENSES_CSV_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            amount, category, date, description = row
            expense = Expense(float(amount), category, date, description)
            expenses.append(expense)

    return expenses

def save_expenses(expenses):
    """
    Save a list of Expense objects to the CSV file.

    Args:
        expenses (list of Expense): List of expense objects to be saved.

    Returns:
        None
    """
    # Ensure the 'data' directory exists
    os.makedirs(os.path.dirname(EXPENSES_CSV_FILE), exist_ok=True)

    # Write expense data to the CSV file
    with open(EXPENSES_CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Date", "Description"])  # Write the header row
        for expense in expenses:
            writer.writerow([expense.amount, expense.category, expense.date, expense.description])
