import argparse
from expense import Expense
from storage import load_expenses, save_expenses
from reports import generate_report

def add_expense():
    """
    Function to add a new expense to the expense tracker.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Add Expense")
    parser.add_argument("amount", type=float, help="Expense amount")
    parser.add_argument("category", type=str, help="Expense category")
    parser.add_argument("date", type=str, help="Expense date (YYYY-MM-DD)")
    parser.add_argument("description", type=str, help="Expense description")
    args = parser.parse_args()

    # Create an Expense object
    expense = Expense(args.amount, args.category, args.date, args.description)

    # Load existing expenses and add the new expense
    expenses = load_expenses()
    expenses.append(expense)

    # Save updated expense data
    save_expenses(expenses)

    print("Expense added successfully.")

def main():
    # Parse command-line arguments using argparse
    parser = argparse.ArgumentParser(description="Personal Expense Tracker")
    parser.add_argument("--add", action="store_true", help="Add a new expense")
    parser.add_argument("--report", action="store_true", help="Generate a report")
    parser.add_argument("--report-type", type=str, choices=["monthly", "category"], help="Report type")

    args = parser.parse_args()

    if args.add:
        add_expense()
    elif args.report:
        if args.report_type == "monthly":
            # Generate a monthly expense report
            expenses = load_expenses()
            generate_report(expenses, "monthly")
        elif args.report_type == "category":
            # Generate a category-wise expense report
            expenses = load_expenses()
            generate_report(expenses, "category")

if __name__ == "__main__":
    main()
