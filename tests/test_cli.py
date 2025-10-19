import unittest
from CLI.cli import CLI
from core.backgammon_game.backgammongame import BackgammonGame
class TestCLI(unittest.TestCase):
    def test_cli_initialization(self):
        """Prueba que el CLI se inicializa correctamente"""
        cli = CLI()
        self.assertIsNotNone(cli)
    def test_cli_can_create_game(self):
        """Prueba que CLI puede crear y mantener un juego"""
        cli = CLI()
        game = BackgammonGame("TestPlayer1", "TestPlayer2")
        self.assertIsNotNone(game)
    def test_cli_game_integration(self):
        """Prueba integración básica CLI-Game"""
        cli = CLI()
        game = BackgammonGame("Alice", "Bob")
        current_player = game.get_current_player()
        self.assertIn(current_player.get_name(), ["Alice", "Bob"])
    def test_cli_exists(self):
        """Prueba que la clase CLI existe y es instanciable"""
        cli = CLI()
        self.assertIsInstance(cli, CLI)
if __name__ == '__main__':
    unittest.main()