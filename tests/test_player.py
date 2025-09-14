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