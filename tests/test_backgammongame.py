import unittest
from core.backgammon_game.backgammongame import BackgammonGame
class TestBackgammonGame(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.game = BackgammonGame("TestPlayer1", "TestPlayer2")
    def test_game_initialization(self):
        """Prueba la inicialización del juego"""
        game = BackgammonGame("Player1", "Player2")
        self.assertIsNotNone(game)
        self.assertFalse(game.is_game_over())
        self.assertIsNone(game.get_winner())
    def test_default_player_names(self):
        """Prueba nombres de jugadores por defecto"""
        game = BackgammonGame()
        current_player = game.get_current_player()
        self.assertIn(current_player.get_name(), ["Player 1", "Player 2"])
    def test_custom_player_names(self):
        """Prueba nombres de jugadores personalizados"""
        current_player = self.game.get_current_player()
        self.assertIn(current_player.get_name(), ["TestPlayer1", "TestPlayer2"])
    def test_roll_dice(self):
        """Prueba lanzamiento de dados"""
        values = self.game.roll_dice()
        self.assertEqual(len(values), 2)
        for value in values:
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)
    def test_initial_turn_state(self):
        """Prueba estado inicial del turno"""
        self.assertTrue(self.game.is_turn_complete())
        remaining_moves = self.game.get_remaining_moves()
        self.assertEqual(len(remaining_moves), 0)
    def test_dice_roll_sets_moves(self):
        """Prueba que lanzar dados establece movimientos"""
        values = self.game.roll_dice()
        remaining_moves = self.game.get_remaining_moves()
        self.assertGreater(len(remaining_moves), 0)
        self.assertFalse(self.game.is_turn_complete())
    def test_switch_turn(self):
        """Prueba cambio de turno"""
        initial_player = self.game.get_current_player()
        self.game.switch_turn()
        new_player = self.game.get_current_player()
        self.assertNotEqual(initial_player.get_name(), new_player.get_name())
    def test_make_move_without_dice(self):
        """Prueba movimiento sin haber lanzado dados"""
        result = self.game.make_move(1, 3)
        self.assertFalse(result)
    def test_make_move_with_dice(self):
        """Prueba movimiento después de lanzar dados"""
        self.game.roll_dice()
        remaining_moves = self.game.get_remaining_moves()
        if remaining_moves:
            die_value = remaining_moves[0]
            result = self.game.make_move(1, die_value)
            self.assertIsInstance(result, bool)
    def test_has_valid_moves_initial_position(self):
        """Prueba verificación de movimientos válidos"""
        self.game.roll_dice()
        has_moves = self.game.has_valid_moves()
        self.assertIsInstance(has_moves, bool)
    def test_get_available_moves(self):
        """Prueba obtener movimientos disponibles"""
        self.game.roll_dice()
        available_moves = self.game.get_available_moves()
        self.assertIsInstance(available_moves, list)
    def test_count_checkers_on_bar_initial(self):
        """Prueba contar fichas en barra al inicio"""
        white_count = self.game.count_checkers_on_bar("white")
        black_count = self.game.count_checkers_on_bar("black")
        self.assertEqual(white_count, 0)
        self.assertEqual(black_count, 0)
    def test_get_forced_move_message_initial(self):
        """Prueba mensaje de movimientos forzados"""
        self.game.roll_dice()
        message = self.game.get_forced_move_message()
        self.assertTrue(message is None or isinstance(message, str))
    def test_reset_game(self):
        """Prueba reinicio del juego"""
        self.game.roll_dice()
        self.assertFalse(self.game.is_turn_complete())
        self.game.reset_game()
        self.assertFalse(self.game.is_game_over())
        self.assertIsNone(self.game.get_winner())
        self.assertTrue(self.game.is_turn_complete())
    def test_make_compound_move_without_dice(self):
        """Prueba movimiento compuesto sin dados"""
        result = self.game.make_compound_move(1, [2, 3])
        self.assertFalse(result)
    def test_game_state_consistency(self):
        """Prueba consistencia del estado del juego"""
        self.assertFalse(self.game.is_game_over())
        player = self.game.get_current_player()
        self.assertIsNotNone(player)
        self.assertIn(player.get_color(), ["white", "black"])
if __name__ == "__main__":
    unittest.main()