import unittest
from unittest.mock import Mock, patch
from cli.cli import CLI
from core.backgammon_game.backgammongame import BackgammonGame
class TestCLI(unittest.TestCase):
    def test_cli_initialization(self):
        """Verifica que el CLI se inicializa correctamente"""
        cli = CLI()
        self.assertIsNotNone(cli)
    @patch('cli.cli.BackgammonGame')
    @patch.object(CLI, 'play_game')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Alice', 'Bob'])
    def test_start_with_names(self, input_mock, print_mock, play_game_mock, game_mock):
        """Verifica que start() crea el juego con nombres personalizados"""
        cli = CLI()
        cli.start()
        game_mock.assert_called_once_with('Alice', 'Bob')
        play_game_mock.assert_called_once()
    @patch('cli.cli.BackgammonGame')
    @patch.object(CLI, 'play_game')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['', ''])
    def test_start_default_names(self, input_mock, print_mock, play_game_mock, game_mock):
        """Verifica que start() usa nombres por defecto cuando no se ingresa nada"""
        cli = CLI()
        cli.start()
        game_mock.assert_called_once_with('Player 1', 'Player 2')
        play_game_mock.assert_called_once()
    @patch.object(CLI, 'play_turn', return_value=None)
    @patch('builtins.print')
    def test_play_game_until_over(self, print_mock, play_turn_mock):
        """Verifica que play_game() ejecuta turnos hasta que el juego termina"""
        cli = CLI()
        mock_game = Mock(spec=BackgammonGame)
        cli.__game__ = mock_game
        mock_game.is_game_over.side_effect = [False, False, True]
        winner_mock = Mock()
        winner_mock.get_name.return_value = 'Alice'
        mock_game.get_winner.return_value = winner_mock
        cli.play_game()
        self.assertEqual(play_turn_mock.call_count, 2)
    @patch.object(CLI, 'play_turn', return_value='exit')
    @patch('builtins.print')
    def test_play_game_exit(self, print_mock, play_turn_mock):
        """Verifica que play_game() se detiene cuando play_turn() retorna 'exit'"""
        cli = CLI()
        mock_game = Mock(spec=BackgammonGame)
        cli.__game__ = mock_game
        mock_game.is_game_over.return_value = False
        cli.play_game()
        play_turn_mock.assert_called_once()
    @patch('builtins.print')
    @patch('builtins.input')
    def test_play_turn_no_valid_moves(self, input_mock, print_mock):
        """Verifica que se cambia de turno cuando no hay movimientos válidos"""
        cli = CLI()
        mock_game = Mock(spec=BackgammonGame)
        cli.__game__ = mock_game
        player_mock = Mock()
        player_mock.get_name.return_value = 'Alice'
        player_mock.get_color.return_value = 'white'
        mock_game.get_current_player.return_value = player_mock
        mock_game.roll_dice.return_value = [3, 5]
        mock_game.has_valid_moves.return_value = False
        mock_game.get_remaining_moves.return_value = [3, 5]
        result = cli.play_turn()
        mock_game.switch_turn.assert_called_once()
        self.assertIsNone(result)
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2'])
    def test_play_turn_exit_option(self, input_mock, print_mock):
        """Verifica que play_turn() retorna 'exit' cuando el usuario elige salir"""
        cli = CLI()
        mock_game = Mock(spec=BackgammonGame)
        cli.__game__ = mock_game
        player_mock = Mock()
        player_mock.get_name.return_value = 'Alice'
        player_mock.get_color.return_value = 'white'
        mock_game.get_current_player.return_value = player_mock
        mock_game.roll_dice.return_value = [3, 5]
        mock_game.get_remaining_moves.return_value = [3, 5]
        mock_game.has_valid_moves.return_value = True
        mock_game.get_available_moves.return_value = [3, 5]
        mock_game.get_forced_move_message.return_value = None
        mock_game.count_checkers_on_bar.return_value = 0
        mock_game.is_game_over.return_value = False
        result = cli.play_turn()
        self.assertEqual(result, 'exit')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', 'abc', '1', '12', '3'])
    def test_play_turn_invalid_input(self, input_mock, print_mock):
        """Verifica que play_turn() maneja correctamente input no numérico"""
        cli = CLI()
        mock_game = Mock(spec=BackgammonGame)
        cli.__game__ = mock_game
        player_mock = Mock()
        player_mock.get_name.return_value = 'Alice'
        player_mock.get_color.return_value = 'white'
        mock_game.get_current_player.return_value = player_mock
        mock_game.roll_dice.return_value = [3, 5]
        mock_game.get_remaining_moves.side_effect = [[3, 5], [5], []]
        mock_game.has_valid_moves.side_effect = [True, True, False]
        mock_game.get_available_moves.return_value = [3, 5]
        mock_game.get_forced_move_message.return_value = None
        mock_game.count_checkers_on_bar.return_value = 0
        mock_game.make_move.return_value = True
        mock_game.is_game_over.return_value = False
        result = cli.play_turn()
        self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()
