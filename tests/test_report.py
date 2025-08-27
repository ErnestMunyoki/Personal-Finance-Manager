import unittest
from finance.transaction import Transaction 
from finance.report import Report

class TestReport(unittest.TestCase):
    def test_summary(self):
        transactions = [
            Transaction(1000, "Salary", "2025-08-01", "Monthly salary", "Income"),
            Transaction(200, "Foodd", "2025-08-02", "Groceries", "Expense")
        ]
        report = Report(transactions)
        summary = report.generate_summary()
        self.assertEqual(summary["total_income"], 1000)
        self.assertEqual(summary["total_expense"], 200)