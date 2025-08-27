import unittest
from utilities.security import Security 

class TestSecurity(unittest.TestCase):
    def test_login(self):
        sec = Security()
        self.assertEqual(sec.password, "1234")