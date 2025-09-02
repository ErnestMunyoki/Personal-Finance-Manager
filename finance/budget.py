class Budget:
    def __init__(self, limit=0):
        self.limit = limit

    def set_limit(self, new_limit):
        self.limit = new_limit

    def check_status(self, total_expenses):
        if total_expenses > self.limit:
            return f"Over budget by {total_expenses - self.limit}"
        else:
            return f"Within budget. Remaining: {self.limit - total_expenses}"
