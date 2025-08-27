from finance.manager import FinanceManager

def main():
    print("=== Personal Finance Manager ===")
    print("\n--- Security Login ---")
    password = input("Enter password: ")
    if password != "1234":   
        print("Access Denied!")
        return

    manager = FinanceManager()

    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Reports & Summaries")
        print("4. Manage Budget")
        print("5. Search & Filter Transactions")
        print("6. Backup & Restore")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            manager.add_transaction()
        elif choice == "2":
            manager.view_transactions()
        elif choice == "3":
            manager.generate_reports()
        elif choice == "4":
            manager.manage_budget()
        elif choice == "5":
            manager.search_transactions()
        elif choice == "6":
            manager.backup_and_restore()  
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

        