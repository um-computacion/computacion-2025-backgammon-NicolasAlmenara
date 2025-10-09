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