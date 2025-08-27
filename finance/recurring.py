class RecurringTransaction:
    def __init__(self, amount, category, description, frequency="monthly", t_type="expense"):
        self.amount = amount
        self.category = category
        self.description = description
        self.frequency = frequency  # daily / weekly / monthly
        self.type = t_type          # income or expense

    def to_dict(self):
        """Convert to dictionary for saving in JSON."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "frequency": self.frequency,
            "type": self.type,
        }

