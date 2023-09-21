class Expense:
    """
    Class to represent an expense.

    Attributes:
        amount (float): The expense amount.
        category (str): The category of the expense.
        date (str): The date of the expense in "YYYY-MM-DD" format.
        description (str): A description of the expense.
    """

    def __init__(self, amount, category, date, description):
        """
        Initialize a new Expense object.

        Args:
            amount (float): The expense amount.
            category (str): The category of the expense.
            date (str): The date of the expense in "YYYY-MM-DD" format.
            description (str): A description of the expense.
        """
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        """
        Return a string representation of the Expense object.

        Returns:
            str: String representation of the expense.
        """
        return f"Amount: ${self.amount:.2f}, Category: {self.category}, Date: {self.date}, Description: {self.description}"
