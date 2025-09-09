import unittest
from core.board import Board
class Test_Board(unittest.TestCase):
    def test_board_inicial(self):
        b = Board()
        b.board_inicial()
        self.assertEqual(b.positions[23]["color"], "white")
        self.assertEqual(b.positions[23]["count"], 2)
        self.assertEqual(b.positions[0]["color"], "black")
        self.assertEqual(b.positions[0]["count"], 2)
        self.assertEqual(b.positions[1]["color"], None)
        self.assertEqual(b.positions[1]["count"], 0)
        self.assertEqual(b.positions[12]["color"], "white")
        self.assertEqual(b.positions[12]["count"], 5) 
        self.assertEqual(b.positions[11]["color"], "black")
        self.assertEqual(b.positions[11]["count"], 5)
        self.assertEqual(b.positions[5]["color"], "white")
        self.assertEqual(b.positions[5]["count"], 5)
        self.assertEqual(b.positions[18]["color"], "black")
        self.assertEqual(b.positions[18]["count"], 5)
        
if __name__ == "__main__":
    unittest.main()