import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        p = Player("Juan", "white")
        self.assertEqual(p.name, "Juan")
        self.assertEqual(p.color, "white")

    def test_str(self):
        p = Player("Ana", "black")
        self.assertEqual(str(p), "Ana (black)")

    def test_different_players(self):
        p1 = Player("Juan", "white")
        p2 = Player("Ana", "black")
        self.assertNotEqual(p1.name, p2.name)
        self.assertNotEqual(p1.color, p2.color)

    def test_change_name(self):
        p = Player("Juan", "white")
        p.name = "Pedro"
        self.assertEqual(p.name, "Pedro")

    def test_change_color(self):
        p = Player("Ana", "black")
        p.color = "white"
        self.assertEqual(p.color, "white")

if __name__ == "__main__":
    unittest.main()