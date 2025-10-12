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
    def test_check_winner_white_wins(self):
        """Prueba verificación cuando ganan las blancas"""
        self.board.off["white"] = 15
        result = self.manager.check_winner(self.board, self.player1, self.player2)
        self.assertTrue(result)
        self.assertTrue(self.manager.is_game_over())
        self.assertEqual(self.manager.get_winner(), self.player1)
    def test_check_winner_black_wins(self):
        """Prueba verificación cuando ganan las negras"""
        self.board.off["black"] = 15
        result = self.manager.check_winner(self.board, self.player1, self.player2)
        self.assertTrue(result)
        self.assertTrue(self.manager.is_game_over())
        self.assertEqual(self.manager.get_winner(), self.player2)
    def test_reset_game(self):
        """Prueba reinicio del juego"""
        self.board.off["white"] = 15
        self.manager.check_winner(self.board, self.player1, self.player2)
        self.assertTrue(self.manager.is_game_over())
        self.assertIsNotNone(self.manager.get_winner())
        self.manager.reset_game()
        self.assertFalse(self.manager.is_game_over())
        self.assertIsNone(self.manager.get_winner())