class Transaction:
    def __init__(self, amount, category, date, description, t_type="expense"):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.type = t_type 

    def to_dict(self):
        """Convert transaction object into dictionary for saving."""
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
            "type": self.type
        }

    @staticmethod
    def from_dict(data):
        """Create Transaction object from dictionary."""
        return Transaction(
            amount=data.get("amount"),
            category=data.get("category"),
            date=data.get("date"),
            description=data.get("description"),
            t_type=data.get("type", "expense")
        )

