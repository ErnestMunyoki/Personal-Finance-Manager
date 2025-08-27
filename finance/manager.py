from finance.transaction import Transaction
from utilities.file_handler import load_data, save_data

class FinanceManager:
    def __init__(self):
        print("Finance Manager initialized.")

    def menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Generate Reports & Summaries")
            print("4. Manage Budget")
            print("5. Search & Filter Transactions")
            print("6. Backup & Restore")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.view_transactions()
            elif choice == "3":
                print("[TODO] Generate Reports & Summaries")
            elif choice == "4":
                print("[TODO] Manage Budget")
            elif choice == "5":
                print("[TODO] Search & Filter Transactions")
            elif choice == "6":
                print("[TODO] Backup & Restore")
            elif choice == "7":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

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
        print("\n--- View Transactions ---")
        transactions = load_data()

        if not transactions:
            print("No transactions found.")
            return

        for i, t in enumerate(transactions, start=1):
            print(f"{i}. {t['date']} | {t['type'].capitalize()} | {t['category']} | {t['amount']} | {t['description']}")
