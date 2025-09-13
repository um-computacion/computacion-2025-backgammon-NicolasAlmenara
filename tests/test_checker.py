import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    def setUp(self):
        Checker.reset_counts()

    def test_init_bar(self):
        c = Checker("white", "barra")
        self.assertEqual(Checker.get_bar_count("white"), 1)
        self.assertEqual(Checker.get_bar_count("black"), 0)

if __name__ == "__main__":
    unittest.main()