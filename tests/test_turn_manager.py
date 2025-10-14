import unittest
from core.player import Player
from core.board import Board
from core.backgammon_game.turn_manager import TurnManager
from core.backgammon_game.move_validator import MoveValidator
class TestTurnManager(unittest.TestCase): 
    def setUp(self):
        """Configuración inicial para cada test"""
        self.player1 = Player("Player1", "white")
        self.player2 = Player("Player2", "black")
        self.turn_manager = TurnManager(self.player1, self.player2)
        self.board = Board()
        self.validator = MoveValidator(self.board)
    def test_turn_manager_initialization(self):
        """Prueba la inicialización del gestor de turnos"""
        manager = TurnManager(self.player1, self.player2)
        self.assertIsNotNone(manager)
        self.assertEqual(manager.get_current_player(), self.player1)
        self.assertTrue(manager.is_turn_complete())
    def test_initial_current_player(self):
        """Prueba que el jugador inicial es el primero"""
        current = self.turn_manager.get_current_player()
        self.assertEqual(current, self.player1)
        self.assertEqual(current.get_name(), "Player1")
        self.assertEqual(current.get_color(), "white")
    def test_initial_remaining_moves(self):
        """Prueba que inicialmente no hay movimientos"""
        moves = self.turn_manager.get_remaining_moves()
        self.assertEqual(len(moves), 0)
        self.assertTrue(self.turn_manager.is_turn_complete())
    def test_set_moves_from_dice_normal(self):
        """Prueba establecer movimientos desde dados normales"""
        self.turn_manager.set_moves_from_dice([3, 5], False)
        moves = self.turn_manager.get_remaining_moves()
        self.assertEqual(len(moves), 2)
        self.assertIn(3, moves)
        self.assertIn(5, moves)
        self.assertEqual(moves, [5, 3])
if __name__ == '__main__':
    unittest.main()