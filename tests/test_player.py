import unittest
from core.player import Player
class TestPlayer(unittest.TestCase):
    def test_player_initialization(self):
        """Prueba la inicialización correcta del jugador"""
        player = Player("Juan", "white")
        self.assertEqual(player.get_name(), "Juan")
        self.assertEqual(player.get_color(), "white")
    def test_player_with_different_colors(self):
        """Prueba jugadores con diferentes colores"""
        player_white = Player("Player1", "white")
        player_black = Player("Player2", "black")
        self.assertEqual(player_white.get_color(), "white")
        self.assertEqual(player_black.get_color(), "black")
    def test_player_names(self):
        """Prueba diferentes tipos de nombres"""
        player1 = Player("Alice", "white")
        self.assertEqual(player1.get_name(), "Alice")
        player2 = Player("Bob Smith", "black")
        self.assertEqual(player2.get_name(), "Bob Smith")
        player3 = Player("", "white")
        self.assertEqual(player3.get_name(), "")
    def test_player_get_methods(self):
        """Prueba que los métodos get devuelven los valores correctos"""
        name = "TestPlayer"
        color = "red"
        player = Player(name, color)
        self.assertEqual(player.get_name(), name)
        self.assertEqual(player.get_color(), color)
    def test_multiple_players(self):
        """Prueba crear múltiples jugadores independientes"""
        player1 = Player("Player1", "white")
        player2 = Player("Player2", "black")
        self.assertNotEqual(player1.get_name(), player2.get_name())
        self.assertNotEqual(player1.get_color(), player2.get_color())
    def test_player_immutability(self):
        """Prueba que los valores no cambian después de la creación"""
        original_name = "OriginalPlayer"
        original_color = "blue"
        player = Player(original_name, original_color)
        self.assertEqual(player.get_name(), original_name)
        self.assertEqual(player.get_color(), original_color)
        self.assertEqual(player.get_name(), player.get_name())
        self.assertEqual(player.get_color(), player.get_color())
if __name__ == '__main__':
    unittest.main()