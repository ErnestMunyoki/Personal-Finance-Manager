class Report:
    def __init__(self, transactions):
        self.transactions = transactions

    def generate_summary(self):
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = income - expenses
        return {
            "income": income,
            "expenses": expenses,
            "balance": balance
        }

    def category_report(self):
        category_totals = {}
        for t in self.transactions:
            cat = t["category"]
            category_totals[cat] = category_totals.get(cat, 0) + t["amount"]
        return category_totals
