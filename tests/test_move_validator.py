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