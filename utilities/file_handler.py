import json
import os

DATA_FILE = "data/transactions.json"

def save_data(transactions):
    """Save transactions list to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump([t.__dict__ for t in transactions], f, indent= 4)

def load_data():
    """Load transactions from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return data