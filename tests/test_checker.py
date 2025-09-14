import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    def setUp(self):
        Checker.reset_counts()

    def test_init_bar(self):
        c = Checker("white", "barra")
        self.assertEqual(Checker.get_bar_count("white"), 1)
        self.assertEqual(Checker.get_bar_count("black"), 0)
        
    def test_init_off(self):
        c = Checker("black", "fuera")
        self.assertEqual(Checker.get_off_count("black"), 1)
        self.assertEqual(Checker.get_off_count("white"), 0)

    def test_to_bar_and_to_board(self):
        c = Checker("white")
        c.to_bar()
        self.assertEqual(Checker.get_bar_count("white"), 1)
        c.to_board()
        self.assertEqual(Checker.get_bar_count("white"), 0)
    def test_to_off(self):
        c = Checker("black")
        c.to_off()
        self.assertEqual(Checker.get_off_count("black"), 1)

    def test_reset_counts(self):
        c1 = Checker("white", "barra")
        c2 = Checker("black", "fuera")
        Checker.reset_counts()
        self.assertEqual(Checker.get_bar_count("white"), 0)
        self.assertEqual(Checker.get_off_count("black"), 0)

if __name__ == "__main__":
    unittest.main()