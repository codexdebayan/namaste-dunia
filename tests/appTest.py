import unittest
from app import NamasteDunia

class TestNamasteDunia(unittest.TestCase):
    def test_greet(self):
        expected_output = "Namaste Dunia"
        self.assertEqual(NamasteDunia.greet(), expected_output)

if __name__ == "__main__":
    unittest.main()
