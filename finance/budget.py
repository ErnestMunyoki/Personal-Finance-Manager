import json
import os

BUDGET_FILE = "data/budget.json"

class Budget:
    def __init__(self):
        self.monthly_limit = self.load_budget()

    def load_budget(self):
        if os.path.exists(BUDGET_FILE):
            with open(BUDGET_FILE, "r") as f:
                return json.load(f).get("monthly_limit", 0)
        return 0

    def save_budget(self):
        with open(BUDGET_FILE, "w") as f:
            json.dump({"monthly_limit": self.monthly_limit}, f)

    def set_budget(self, amount):
        self.monthly_limit = amount
        self.save_budget()
        print(f"Budget set to {amount}")

    def check_budget(self, transactions):
        expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
        print(f"Spent {expenses} / {self.monthly_limit}")
        if expenses > self.monthly_limit:
            print("Budget exceeded!")
        else:
            print("Within budget")
