import unittest
from core.board import Board
from core.backgammon_game.move_calculator import MoveCalculator
class TestMoveCalculator(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.calculator = MoveCalculator()
        self.board = Board()
    def test_calculator_initialization(self):
        """Prueba la inicialización del calculador"""
        calculator = MoveCalculator()
        self.assertIsNotNone(calculator)
    def test_calculate_white_normal_move(self):
        """Prueba cálculo de movimiento normal para fichas blancas"""
        result = self.calculator.calculate_destination(1, 3, "white")
        self.assertEqual(result, 4)
        result = self.calculator.calculate_destination(10, 5, "white")
        self.assertEqual(result, 15)
    def test_calculate_black_normal_move(self):
        """Prueba cálculo de movimiento normal para fichas negras"""
        result = self.calculator.calculate_destination(24, 3, "black")
        self.assertEqual(result, 21) 
        result = self.calculator.calculate_destination(15, 5, "black")
        self.assertEqual(result, 10)
    def test_calculate_white_bearing_off(self):
        """Prueba cálculo de bearing off para fichas blancas"""
        result = self.calculator.calculate_destination(23, 3, "white")
        self.assertEqual(result, 0)
        result = self.calculator.calculate_destination(20, 6, "white")
        self.assertEqual(result, 0)
    def test_calculate_black_bearing_off(self):
        """Prueba cálculo de bearing off para fichas negras"""
        result = self.calculator.calculate_destination(2, 3, "black")
        self.assertEqual(result, 0)
        result = self.calculator.calculate_destination(5, 6, "black")
        self.assertEqual(result, 0)
    def test_calculate_from_bar_white(self):
        """Prueba cálculo desde barra para fichas blancas"""
        result = self.calculator.calculate_destination(25, 3, "white")
        self.assertEqual(result, 3)
        result = self.calculator.calculate_destination(25, 6, "white")
        self.assertEqual(result, 6)
    def test_calculate_from_bar_black(self):
        """Prueba cálculo desde barra para fichas negras"""
        result = self.calculator.calculate_destination(25, 3, "black")
        self.assertEqual(result, 22)
        result = self.calculator.calculate_destination(25, 6, "black")
        self.assertEqual(result, 19)
    def test_can_bear_off_exact_white(self):
        """Prueba bearing off exacto para fichas blancas"""
        self.board.points[2] = ["white", 1]
        result = self.calculator.can_bear_off_exact_or_higher(3, 3, "white", self.board)
        self.assertTrue(result)
    def test_can_bear_off_exact_black(self):
        """Prueba bearing off exacto para fichas negras"""
        self.board.points[21] = ["black", 1]
        result = self.calculator.can_bear_off_exact_or_higher(22, 3, "black", self.board)
        self.assertTrue(result)
    def test_edge_cases(self):
        """Prueba casos límite"""
        result = self.calculator.calculate_destination(24, 1, "white")
        self.assertEqual(result, 0)
        result = self.calculator.calculate_destination(1, 1, "black")
        self.assertEqual(result, 0)
if __name__ == '__main__':
    unittest.main()
