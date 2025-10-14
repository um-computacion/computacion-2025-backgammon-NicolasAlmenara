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
    def test_set_moves_from_dice_double(self):
        """Prueba establecer movimientos desde dados dobles"""
        self.turn_manager.set_moves_from_dice([4, 4], True)
        moves = self.turn_manager.get_remaining_moves()
        self.assertEqual(len(moves), 4)
        self.assertEqual(moves, [4, 4, 4, 4])
    def test_use_move_valid(self):
        """Prueba usar un movimiento válido"""
        self.turn_manager.set_moves_from_dice([2, 6], False)
        result = self.turn_manager.use_move(6)
        self.assertTrue(result)
        moves = self.turn_manager.get_remaining_moves()
        self.assertEqual(len(moves), 1)
        self.assertIn(2, moves)
        self.assertNotIn(6, moves)
    def test_use_move_invalid(self):
        """Prueba usar un movimiento no disponible"""
        self.turn_manager.set_moves_from_dice([2, 6], False)
        result = self.turn_manager.use_move(5)
        self.assertFalse(result)
        moves = self.turn_manager.get_remaining_moves()
        self.assertEqual(len(moves), 2)
    def test_has_move(self):
        """Prueba verificación de movimientos disponibles"""
        self.turn_manager.set_moves_from_dice([1, 4], False)
        self.assertTrue(self.turn_manager.has_move(1))
        self.assertTrue(self.turn_manager.has_move(4))
        self.assertFalse(self.turn_manager.has_move(3))
        self.assertFalse(self.turn_manager.has_move(6))
    def test_switch_player(self):
        """Prueba cambio de jugador"""
        initial_player = self.turn_manager.get_current_player()
        self.assertEqual(initial_player, self.player1)
        self.turn_manager.switch_player()
        new_player = self.turn_manager.get_current_player()
        self.assertEqual(new_player, self.player2)
        self.turn_manager.switch_player()
        back_to_first = self.turn_manager.get_current_player()
        self.assertEqual(back_to_first, self.player1)
    def test_switch_player_clears_moves(self):
        """Prueba que cambiar jugador limpia los movimientos"""
        self.turn_manager.set_moves_from_dice([3, 6], False)
        self.assertFalse(self.turn_manager.is_turn_complete())
        self.turn_manager.switch_player()
        self.assertTrue(self.turn_manager.is_turn_complete())
        self.assertEqual(len(self.turn_manager.get_remaining_moves()), 0)
    def test_is_turn_complete(self):
        """Prueba verificación de turno completo"""
        self.assertTrue(self.turn_manager.is_turn_complete())
        self.turn_manager.set_moves_from_dice([2, 5], False)
        self.assertFalse(self.turn_manager.is_turn_complete())
        self.turn_manager.use_move(2)
        self.assertFalse(self.turn_manager.is_turn_complete())
        self.turn_manager.use_move(5)
        self.assertTrue(self.turn_manager.is_turn_complete())
    def test_get_forced_moves_no_moves(self):
        """Prueba movimientos forzados sin dados"""
        forced = self.turn_manager.get_forced_moves(self.validator, self.board, "white")
        self.assertEqual(len(forced), 0)
    def test_get_forced_moves_with_moves(self):
        """Prueba movimientos forzados con dados disponibles"""
        self.turn_manager.set_moves_from_dice([3, 5], False)
        forced = self.turn_manager.get_forced_moves(self.validator, self.board, "white")
        self.assertIsInstance(forced, list)
        self.assertGreaterEqual(len(forced), 0)
    def test_multiple_use_moves(self):
        """Prueba usar múltiples movimientos"""
        self.turn_manager.set_moves_from_dice([1, 2, 3], False)  # Simulando dados personalizados
        self.assertTrue(self.turn_manager.use_move(2))
        self.assertTrue(self.turn_manager.use_move(1))
        self.assertFalse(self.turn_manager.use_move(1))  # Ya usado
        self.assertTrue(self.turn_manager.use_move(3))
        self.assertTrue(self.turn_manager.is_turn_complete())
    def test_remaining_moves_copy(self):
        """Prueba que get_remaining_moves devuelve una copia"""
        self.turn_manager.set_moves_from_dice([4, 6], False)
        moves1 = self.turn_manager.get_remaining_moves()
        moves2 = self.turn_manager.get_remaining_moves()
        moves1.append(99) 
        self.assertNotEqual(moves1, moves2)
        self.assertNotIn(99, moves2)
if __name__ == '__main__':
    unittest.main()