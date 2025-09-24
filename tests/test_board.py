import unittest
from core.board import Board
class Test_Board(unittest.TestCase):
    
    def setUp(self):
        self.b = Board()
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

    def test_move_checker_valid(self):
        self.b.positions[22] = {"color": None, "count": 0}
        result = self.b.move_checker(23, 22, "white")
        self.assertTrue(result)
        self.assertEqual(self.b.positions[22]["color"], "white")
        self.assertEqual(self.b.positions[22]["count"], 1)
        self.assertEqual(self.b.positions[23]["count"], 1)
    
    def test_move_checker_invalid(self):
        result = self.b.move_checker(1, 2, "white")
        self.assertFalse(result)

    def test_bear_off_checker(self):
        result = self.b.bear_off_checker(23, "white")
        self.assertTrue(result)
        self.assertEqual(self.b.positions[23]["count"], 1)
        result = self.b.bear_off_checker(23, "white")
        self.assertTrue(result)
        self.assertEqual(self.b.positions[23]["count"], 0)
        self.assertIsNone(self.b.positions[23]["color"])
    
    def test_get_position(self):
        pos = self.b.get_position(23)
        self.assertEqual(pos["color"], "white")
        self.assertEqual(pos["count"], 2)

    def test_is_move_valid(self):
        self.b.positions[22] = {"color": None, "count": 0}
        self.assertTrue(self.b.is_move_valid(23, 22, "white"))
        self.assertFalse(self.b.is_move_valid(1, 2, "white"))
        self.b.positions[11] = {"color": "black", "count": 2}
        self.assertFalse(self.b.is_move_valid(23, 11, "white"))

    def test_move_checker_invalid_color(self):
        self.b.positions[23] = {"color": "black", "count": 2}
        result = self.b.move_checker(23, 22, "white")
        self.assertFalse(result)

    def test_move_checker_to_pos_ocupado(self):
        self.b.positions[23] = {"color": "white", "count": 2}
        self.b.positions[22] = {"color": "black", "count": 2}
        result = self.b.move_checker(23, 22, "white")
        self.assertFalse(result)

    def test_bear_off_checker_success(self):
        self.b.positions[5] = {"color": "white", "count": 1}
        result = self.b.bear_off_checker(5, "white")
        self.assertTrue(result)
        self.assertEqual(self.b.positions[5]["count"], 0)
        self.assertIsNone(self.b.positions[5]["color"])
        
if __name__ == "__main__":
    unittest.main()