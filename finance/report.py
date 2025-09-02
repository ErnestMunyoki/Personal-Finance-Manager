class Report:
    def __init__(self, transactions=None):
        self.transactions = transactions if transactions else []

    def generate_summary(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        return {"income": income, "expenses": expenses, "balance": income - expenses}

    def category_report(self):
        breakdown = {}
        for t in self.transactions:
            breakdown[t.category] = breakdown.get(t.category, 0) + t.amount
        return breakdown
