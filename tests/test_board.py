import unittest
from core.board import Board
import unittest
from core.board import Board
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    def test_board_initialization(self):
        """Verifica que el tablero se inicializa correctamente"""
        self.assertEqual(len(self.board.points), 24)
        self.assertEqual(self.board.bar["white"], 0)
        self.assertEqual(self.board.bar["black"], 0)
        self.assertEqual(self.board.off["white"], 0)
        self.assertEqual(self.board.off["black"], 0)
    def test_initial_position_white(self):
        """Verifica las posiciones iniciales de las fichas blancas"""
        point1 = self.board.get_point(1)
        self.assertEqual(point1[0], "white")
        self.assertEqual(point1[1], 2)
        point12 = self.board.get_point(12)
        self.assertEqual(point12[0], "white")
        self.assertEqual(point12[1], 5)
        point17 = self.board.get_point(17)
        self.assertEqual(point17[0], "white")
        self.assertEqual(point17[1], 3)
        point19 = self.board.get_point(19)
        self.assertEqual(point19[0], "white")
        self.assertEqual(point19[1], 5)
    def test_initial_position_black(self):
        """Verifica las posiciones iniciales de las fichas negras"""
        point24 = self.board.get_point(24)
        self.assertEqual(point24[0], "black")
        self.assertEqual(point24[1], 2)
        point13 = self.board.get_point(13)
        self.assertEqual(point13[0], "black")
        self.assertEqual(point13[1], 5)
        point8 = self.board.get_point(8)
        self.assertEqual(point8[0], "black")
        self.assertEqual(point8[1], 3)
        point6 = self.board.get_point(6)
        self.assertEqual(point6[0], "black")
        self.assertEqual(point6[1], 5)
    def test_empty_points(self):
        """Verifica que los puntos vacíos están correctos"""
        empty_points = [2, 3, 4, 5, 7, 9, 10, 11, 14, 15, 16, 18, 20, 21, 22, 23]
        for point_num in empty_points:
            point = self.board.get_point(point_num)
            self.assertEqual(point[0], "")
            self.assertEqual(point[1], 0)
if __name__ == "__main__":
    unittest.main()