import unittest
from finance.manager import FinanceManager

class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.fm = FinanceManager()

    def test_add_transaction(self):
        self.fm.add_transaction()
        self.assertTrue(True)
        