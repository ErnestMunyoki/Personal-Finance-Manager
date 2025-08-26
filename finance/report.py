class Report:
    def __init__(self, transactions):
        self.transactions = transactions

    def generate_summary(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        balance = income - expenses

        return {
            "total_income": income,
            "total_expenses": expenses,
            "balance": balance
        }

    def category_breakdown(self):
        breakdown = {}
        for t in self.transactions:
            breakdown[t.category] = breakdown.get(t.category, 0) + t.amount
        return breakdown
