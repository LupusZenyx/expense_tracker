# Personal Expense Tracker 💰

## Introduction
Welcome to the Personal Expense Tracker, your financial companion for managing expenses. Keep your finances organized and never lose track of your spending again!

## Getting Started

### Prerequisites
Before you start using the Personal Expense Tracker, ensure you have Python 3.x installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

### Clone the Repository
To get started, clone this repository to your local machine:

```shell
git clone https://github.com/yourusername/personal-expense-tracker.git
```

### Navigate to the Project Directory
Navigate to the project directory after cloning:

```shell
cd personal-expense-tracker
```

## Usage

The Personal Expense Tracker supports the following commands:

### Add an Expense

To add a new expense, use the `--add` command followed by the expense details (amount, category, date, and description):

```shell
python main.py --add <amount> <category> <date> <description>
```

Example:

```shell
python main.py --add 45.50 Food 2023-09-15 "Lunch with friends"
```

### Generate Reports

You can generate two types of reports:

- Monthly Expense Report:

```shell
python main.py --report --report-type monthly
```

- Category-wise Expense Report:

```shell
python main.py --report --report-type category
```

### Customize Settings

You can customize settings such as currency and budget limits by editing the `settings.json` file in the `data` directory.

## Examples

Here are some example commands to help you get started:

- Add an expense:

```shell
python main.py --add 29.99 Shopping 2023-09-16 "New Shirt"
```

- Generate a monthly expense report:

```shell
python main.py --report --report-type monthly
```

- Generate a category-wise expense report:

```shell
python main.py --report --report-type category
```

Brought to you by the finance wizards of Big-Boy-Mr-Big. Keep track of your expenses like never before!
```

