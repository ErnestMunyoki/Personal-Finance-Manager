import unittest
from finance.budget import Budget

class TestBudget(unittest.TestCase):
    def test_budget_alerts(self):
        budget = Budget(1000)
        result = budget.check_budget(1200)
        self.assertIn("exceeded", result)