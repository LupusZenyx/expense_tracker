import datetime
import matplotlib.pyplot as plt

def generate_monthly_report(expenses):
    """
    Generate a monthly expense report.

    Args:
        expenses (list of Expense): List of expense objects.

    Returns:
        None
    """
    # Group expenses by month and calculate total expenses for each month
    monthly_totals = {}
    for expense in expenses:
        date = datetime.datetime.strptime(expense.date, "%Y-%m-%d")
        month_key = date.strftime("%Y-%m")
        if month_key in monthly_totals:
            monthly_totals[month_key] += expense.amount
        else:
            monthly_totals[month_key] = expense.amount

    # Sort months chronologically
    sorted_months = sorted(monthly_totals.keys())

    # Generate the monthly expense report
    print("Monthly Expense Report")
    for month in sorted_months:
        total = monthly_totals[month]
        print(f"{month}: ${total:.2f}")

    # Plot monthly expenses
    plot_monthly_expenses(sorted_months, [monthly_totals[month] for month in sorted_months])

def generate_category_report(expenses):
    """
    Generate a category-wise expense report.

    Args:
        expenses (list of Expense): List of expense objects.

    Returns:
        None
    """
    # Group expenses by category and calculate total expenses for each category
    category_totals = {}
    for expense in expenses:
        category = expense.category
        if category in category_totals:
            category_totals[category] += expense.amount
        else:
            category_totals[category] = expense.amount

    # Generate the category-wise expense report
    print("Category-wise Expense Report")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

    # Plot category-wise expenses
    plot_category_expenses(category_totals)

def plot_monthly_expenses(months, totals):
    """
    Plot a bar chart of monthly expenses.

    Args:
        months (list of str): List of month-year strings (e.g., "YYYY-MM").
        totals (list of float): List of total expenses for each month.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.bar(months, totals)
    plt.xlabel("Month")
    plt.ylabel("Total Expenses ($)")
    plt.title("Monthly Expense Summary")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_category_expenses(category_totals):
    """
    Plot a pie chart of category-wise expenses.

    Args:
        category_totals (dict): Dictionary mapping expense categories to total expenses.

    Returns:
        None
    """
    categories = list(category_totals.keys())
    totals = [category_totals[category] for category in categories]

    plt.figure(figsize=(8, 8))
    plt.pie(totals, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Category-wise Expense Breakdown")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
