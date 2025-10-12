import unittest
from core.player import Player
from core.board import Board
from core.backgammon_game.game_state_manager import GameStateManager
class TestGameStateManager(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.manager = GameStateManager()
        self.board = Board()
        self.player1 = Player("Player1", "white")
        self.player2 = Player("Player2", "black")
    def test_manager_initialization(self):
        """Prueba la inicialización del gestor de estado"""
        manager = GameStateManager()
        self.assertFalse(manager.is_game_over())
        self.assertIsNone(manager.get_winner())
    def test_initial_state(self):
        """Prueba el estado inicial del juego"""
        self.assertFalse(self.manager.is_game_over())
        self.assertIsNone(self.manager.get_winner())
    def test_check_winner_no_winner(self):
        """Prueba verificación cuando no hay ganador"""
        result = self.manager.check_winner(self.board, self.player1, self.player2)
        self.assertFalse(result)
        self.assertFalse(self.manager.is_game_over())
        self.assertIsNone(self.manager.get_winner())