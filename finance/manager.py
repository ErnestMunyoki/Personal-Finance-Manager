from finance.transaction import Transaction
from finance.file_handler import load_data, save_data
from finance.report import Report
from finance.budget import Budget
from finance.recurring import RecurringTransaction

class FinanceManager:
    def __init__(self):
        self.transactions = [Transaction.from_dict(t) for t in load_data("data/transactions.json")]
        self.report = Report(self.transactions)
        self.budget = Budget()
        self.recurring_transactions = []

    def add_transaction(self):
        print("\n--- Add Transaction ---")
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport, Salary): ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        t_type = input("Enter type (income/expense): ")

        transaction = Transaction(amount, category, date, description, t_type)
        self.transactions.append(transaction)
        save_data("data/transactions.json", [t.to_dict() for t in self.transactions])
        print("Transaction added successfully!")

    def view_transactions(self):
        print("\n--- Transactions ---")
        if not self.transactions:
            print("No transactions found.")
            return
        for i, t in enumerate(self.transactions, start=1):
            print(f"{i}. {t.date} | {t.category} | {t.type} | {t.amount} | {t.description}")


