import json
import os

DATA_FILE = "data/transactions.json"
BUDGET_FILE = "data/budget.json"
RECURRING_FILE = "data/recurring.json"
BACKUP_FILE = "data/transactions_backup.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_data(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)


def backup_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as original, open(BACKUP_FILE, "w") as backup:
            backup.write(original.read())
        print("Backup created successfully.")
    else:
        print("No data to backup.")


def restore_data():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "r") as backup, open(DATA_FILE, "w") as original:
            original.write(backup.read())
        print("Data restored from backup.")
    else:
        print("No backup found.")

