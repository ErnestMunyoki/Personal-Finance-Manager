from finance.transaction import Transaction
from finance.file_handler import load_data, save_data, backup_data, restore_data
from finance.budget import Budget
from finance.report import Report
from finance.recurring import RecurringTransaction


class FinanceManager:
    def __init__(self):
        print("Finance Manager initialized.")
        self.budget = Budget()
        self.report = Report()
        self.recurring = RecurringTransaction()

    def add_transaction(self):
        print("\n--- Add Transaction ---")

        amount_input = input("Enter amount: ").strip()
        if not amount_input.replace(".", "", 1).isdigit():
            print("Invalid input. Amount must be a number.")
            return

        amount = float(amount_input)
        category = input("Enter category (e.g., Food, Transport, Salary): ").strip()
        date = input("Enter date (YYYY-MM-DD): ").strip()
        description = input("Enter description: ").strip()
        t_type = input("Enter type (income/expense): ").lower().strip()

        if t_type not in ["income", "expense"]:
            print("Invalid type. Must be 'income' or 'expense'.")
            return

        new_transaction = Transaction(amount, category, date, description, t_type)

        transactions = load_data()
        transactions.append(new_transaction.__dict__)
        save_data(transactions)

        print("Transaction added successfully!")

    def view_transactions(self):
        print("\n--- All Transactions ---")
        transactions = load_data()
        if not transactions:
            print("No transactions found.")
            return

        for i, t in enumerate(transactions, 1):
            print(
                f"{i}. {t['date']} | {t['type']} | {t['category']} | {t['amount']} | {t['description']}"
            )

    def generate_reports(self):
        self.report.generate()

    def manage_budget(self):
        self.budget.manage()

    def search_filter_transactions(self):
        print("\n--- Search Transactions ---")
        keyword = input("Enter keyword (category/date/description): ").strip().lower()

        transactions = load_data()
        filtered = [
            t
            for t in transactions
            if keyword in t["category"].lower()
            or keyword in t["date"].lower()
            or keyword in t["description"].lower()
        ]

        if not filtered:
            print("No matching transactions found.")
            return

        for i, t in enumerate(filtered, 1):
            print(
                f"{i}. {t['date']} | {t['type']} | {t['category']} | {t['amount']} | {t['description']}"
            )

    def backup_restore(self):
        print("\n--- Backup & Restore ---")
        choice = input("Enter 'b' to backup or 'r' to restore: ").lower().strip()
        if choice == "b":
            backup_data()
        elif choice == "r":
            restore_data()
        else:
            print("Invalid choice.")

    def handle_recurring(self):
        self.recurring.manage()
