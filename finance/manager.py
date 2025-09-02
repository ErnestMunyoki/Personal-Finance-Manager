from finance.database import SessionLocal
from finance.models import Transaction
from finance.report import Report
from finance.budget import Budget
from datetime import datetime

class FinanceManager:
    def __init__(self):
        self.db = SessionLocal()
        self.budget = Budget(2000)
        self.report = Report()

    def add_transaction(self):
        print("\n--- Add Transaction ---")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        t_type = input("Enter type (income/expense): ")

        transaction = Transaction(
            amount=amount,
            category=category,
            date=datetime.strptime(date, "%Y-%m-%d").date(),
            description=description,
            type=t_type
        )

        self.db.add(transaction)
        self.db.commit()
        print("✅ Transaction added successfully!")

    def view_transactions(self):
        print("\n--- Transactions ---")
        transactions = self.db.query(Transaction).all()
        if not transactions:
            print("No transactions found.")
        else:
            for t in transactions:
                print(f"{t.date} | {t.category} | {t.amount} | {t.type} | {t.description}")

    def generate_reports(self):
        print("\n--- Reports ---")
        transactions = self.db.query(Transaction).all()
        self.report = Report(transactions)
        summary = self.report.generate_summary()
        print(f"Total Income: {summary['income']}")
        print(f"Total Expenses: {summary['expenses']}")
        print(f"Balance: {summary['balance']}")

    def manage_budget(self):
        print("\n--- Budget Management ---")
        new_limit = float(input("Set new budget limit: "))
        self.budget.set_limit(new_limit)
        transactions = self.db.query(Transaction).filter(Transaction.type == "expense").all()
        total_expenses = sum(t.amount for t in transactions)
        print(self.budget.check_status(total_expenses))

    def search_transactions(self):
        print("\n--- Search Transactions ---")
        keyword = input("Enter keyword to search in description: ").lower()
        results = self.db.query(Transaction).filter(Transaction.description.ilike(f"%{keyword}%")).all()
        if results:
            for t in results:
                print(f"{t.date} | {t.category} | {t.amount} | {t.type} | {t.description}")
        else:
            print("No matching transactions found.")

    def backup_and_restore(self):
        print("[TODO] Backup & Restore feature not yet implemented.")
