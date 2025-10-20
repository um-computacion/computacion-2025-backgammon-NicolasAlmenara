import unittest
from core.board import Board
from core.backgammon_game.move_validator import MoveValidator
class TestMoveValidator(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.board = Board()
        self.validator = MoveValidator(self.board)
    def test_validator_initialization(self):
        """Prueba la inicialización del validador"""
        validator = MoveValidator(self.board)
        self.assertIsNotNone(validator)
    def test_valid_move_from_starting_position(self):
        """Prueba movimientos válidos desde posiciones iniciales"""
        result = self.validator.is_valid_move(1, 2, "white")
        self.assertTrue(result)
    def test_invalid_move_empty_source(self):
        """Prueba movimiento inválido desde posición vacía"""
        result = self.validator.is_valid_move(3, 4, "white")
        self.assertFalse(result)
    def test_invalid_move_wrong_color(self):
        """Prueba movimiento inválido con color equivocado"""
        result = self.validator.is_valid_move(1, 2, "black")
        self.assertFalse(result)
    def test_invalid_source_position(self):
        """Prueba posiciones origen inválidas"""
        result = self.validator.is_valid_move(26, 1, "white")
        self.assertFalse(result)
        result = self.validator.is_valid_move(0, 1, "white")
        self.assertFalse(result)
    def test_invalid_destination_position(self):
        """Prueba posiciones destino inválidas"""
        result = self.validator.is_valid_move(1, 26, "white")
        self.assertFalse(result)
    def test_must_enter_from_bar_no_checkers(self):
        """Prueba must_enter_from_bar cuando no hay fichas en barra"""
        result = self.validator.must_enter_from_bar("white")
        self.assertFalse(result)
        result = self.validator.must_enter_from_bar("black")
        self.assertFalse(result)
    def test_must_enter_from_bar_with_checkers(self):
        """Prueba must_enter_from_bar cuando hay fichas en barra"""
        self.board.bar["white"] = 1
        result = self.validator.must_enter_from_bar("white")
        self.assertTrue(result)
    def test_move_from_bar_valid_position(self):
        """Prueba movimiento desde la barra"""
        self.board.bar["white"] = 1
        result = self.validator.is_valid_move(25, 1, "white")
        self.assertIsInstance(result, bool)
    def test_bearing_off_destination(self):
        """Prueba movimiento de bearing off (posición 0)"""
        result = self.validator.is_valid_move(1, 0, "white")
        self.assertIsInstance(result, bool)
    def test_destination_blocked_by_enemy(self):
        """Prueba destino bloqueado por fichas enemigas"""
        self.board.points[2] = ["black", 2]
        result = self.validator.is_valid_move(1, 3, "white")
        self.assertFalse(result)
    def test_destination_with_single_enemy(self):
        """Prueba destino con una sola ficha enemiga (captura válida)"""
        self.board.points[4] = ["black", 1]
        result = self.validator.is_valid_move(1, 5, "white")
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()