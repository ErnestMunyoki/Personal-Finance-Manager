import json
import os
import shutil

def load_data(filepath="data/transactions.json"):
    """Load transaction data from JSON file."""
    if not os.path.exists(filepath):
        return []  
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []  

def save_data(filepath="data/transactions.json", data=None):
    """Save transaction data to JSON file."""
    if data is None:
        data = []
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def backup_data(src="data/transactions.json", dest="backup/transactions_backup.json"):
    """Backup transaction data file."""
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(src):
        shutil.copy(src, dest)
        print("Backup successful.")
    else:
        print("No data file found to backup.")

def restore_data(src="backup/transactions_backup.json", dest="data/transactions.json"):
    """Restore transaction data from backup file."""
    if os.path.exists(src):
        shutil.copy(src, dest)
        print("Restore successful.")
    else:
        print("No backup file found to restore.")


