class Transaction: 
    def __init__(self, amount, category, date, description, t_type="expense"):
        """
        t_type: "income" or "expense"
        """
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.type = t_type

    def __str__(self):
        return f"{self.date} | {self.type.upper()} | {self.category} | {self.amount} | {self.description}"
