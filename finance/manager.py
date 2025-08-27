from finance.transaction import Transaction
from finance.budget import Budget
from finance.recurring import RecurringTransaction
from finance.report import Report
from finance.file_handler import load_data, save_data, backup_data, restore_data


class FinanceManager:
    def __init__(self):
        print("Finance Manager initialized.")
        self.transactions = load_data("data/transactions.json")
        self.recurring_transactions = []  
        self.budget = Budget()
        self.report = Report(self.transactions)

    def add_transaction(self):
        print("\n--- Add Transaction ---")
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Transport, Salary): ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            t_type = input("Enter type (income/expense): ").lower()

            transaction = Transaction(amount, category, date, description, t_type)
            self.transactions.append(transaction.to_dict())
            save_data("data/transactions.json", self.transactions)
            print("Transaction added successfully!")

        except ValueError:
            print("Invalid input. Amount must be a number.")

    def add_recurring_transaction(self):
        print("\n--- Add Recurring Transaction ---")
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Rent, Subscription): ")
            description = input("Enter description: ")
            frequency = input("Enter frequency (daily/weekly/monthly): ").lower()
            t_type = input("Enter type (income/expense): ").lower()

            rt = RecurringTransaction(amount, category, description, frequency, t_type)
            self.recurring_transactions.append(rt.to_dict())
            print("Recurring transaction added successfully!")

        except ValueError:
            print("Invalid input. Amount must be a number.")

