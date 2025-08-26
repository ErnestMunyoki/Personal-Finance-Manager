class Budget:
    def __init__(self, monthly_limit=0):
        self.monthly_limit = monthly_limit

    def set_budget(self,limit):
        self.monthly_limit = limit
        print(f"Budget set to {limit}")

    def check_budget(self, total_expenses):
        if self.monthly_limit == 0:
            return "No budget set."
        if total_expenses > self.monthly_limit:
            return "Alert: You have exceeded your budget!"
            elif total_expenses > 0.9 * self.monthly_limit:
                return "Warning: You are close to exceeding your budget."
            else:
                return "You are within your budget."
                