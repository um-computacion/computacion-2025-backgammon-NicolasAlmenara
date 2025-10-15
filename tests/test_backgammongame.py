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
if __name__ == "__main__":
    unittest.main()