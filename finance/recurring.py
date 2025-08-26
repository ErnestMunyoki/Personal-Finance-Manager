class RecurringTransaction:
     def__init__(self, amount, category, description, frequency="monthly", t_type="expense"):
        """
        frequency: daily, weekly, monthly, yearly
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.frequency = frequency
        self.type = t_type
    
    def __str__(self):
        return f"[Recurring] {self.frequency} | {self.type.upper()} | {self.category} | {self.amount} | {self.description}