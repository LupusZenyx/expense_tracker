import argparse
from user_interface import add_expense, generate_monthly_report, generate_category_report
from storage import load_expenses

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
        expenses = load_expenses()
        if args.report_type == "monthly":
            generate_monthly_report(expenses)
        elif args.report_type == "category":
            generate_category_report(expenses)

if __name__ == "__main__":
    main()
