class Report:
    def __init__(self, transactions=None):
        self.transactions = transactions if transactions is not None else []

    def generate_summary(self):
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = total_income - total_expense

        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
        }

    def breakdown_by_category(self):
        categories = {}
        for t in self.transactions:
            cat = t["category"]
            categories[cat] = categories.get(cat, 0) + t["amount"]
        return categories
