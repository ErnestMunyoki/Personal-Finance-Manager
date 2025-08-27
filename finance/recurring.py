class RecurringTransaction:
    def __init__(self, amount, category, description, frequency="monthly", t_type="expense"):
        self.amount = amount
        self.category = category
        self.description = description
        self.frequency = frequency  
        self.type = t_type

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "frequency": self.frequency,
            "type": self.type,
        }
