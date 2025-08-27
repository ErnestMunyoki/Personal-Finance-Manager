from finance.transaction import Transaction
from finance.report import Report
from finance.budget import Budget
from finance.recurring import RecurringTransaction
from finance.file_handler import load_data, save_data, backup_data, restore_data

class FinanceManager:
    def __init__(self):
        self.transactions = load_data("data/transactions.json")
        self.budget = Budget(2000) 
        self.report = Report(self.transactions)

    def add_transaction(self):
        print("\n--- Add Transaction ---")
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport, Salary): ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        t_type = input("Enter type (income/expense): ")

        transaction = Transaction(amount, category, date, description, t_type)
        self.transactions.append(transaction.to_dict())
        save_data("data/transactions.json", self.transactions)
        print("Transaction added successfully!")

    def view_transactions(self):
        print("\n--- Transactions ---")
        if not self.transactions:
            print("No transactions found.")
        else:
            for t in self.transactions:
                print(f"{t['date']} | {t['category']} | {t['amount']} | {t['type']} | {t['description']}")

    def generate_reports(self):
        print("\n--- Reports & Summaries ---")
        self.report = Report(self.transactions)  
        summary = self.report.generate_summary()
        print(f"Total Income: {summary['income']}")
        print(f"Total Expenses: {summary['expenses']}")
        print(f"Balance: {summary['balance']}")

    def manage_budget(self):
        print("\n--- Manage Budget ---")
        new_limit = float(input("Enter new monthly budget limit: "))
        self.budget.set_limit(new_limit)
        print(f"Budget updated to {new_limit}")

        total_expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        status = self.budget.check_status(total_expenses)
        print(f"Budget Status: {status}")

    def search_transactions(self):
        print("\n--- Search Transactions ---")
        keyword = input("Enter keyword (category/description): ").lower()
        results = [t for t in self.transactions if keyword in t["category"].lower() or keyword in t["description"].lower()]

        if results:
            for t in results:
                print(f"{t['date']} | {t['category']} | {t['amount']} | {t['type']} | {t['description']}")
        else:
            print("No matching transactions found.")

    def backup_and_restore(self):
        print("\n--- Backup & Restore ---")
        choice = input("Enter 'b' for backup or 'r' for restore: ").lower()
        if choice == "b":
            backup_data()
            print("Backup completed successfully.")
        elif choice == "r":
            restore_data()
            print("Data restored successfully.")
        else:
            print("Invalid choice.")

