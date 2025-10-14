from ..board import Board
from ..dice import Dice
from ..player import Player
from .move_validator import MoveValidator
from .move_calculator import MoveCalculator
from .turn_manager import TurnManager
from .game_state_manager import GameStateManager
class BackgammonGame:
    """Coordinador del juego de backgammon"""
    def __init__(self, player1_name="Player 1", player2_name="Player 2"):
        """Inicializa el juego coordinando todas las clases especializadas"""
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__player1__ = Player(player1_name, "white")
        self.__player2__ = Player(player2_name, "black")
        self.__validator__ = MoveValidator(self.__board__)
        self.__calculator__ = MoveCalculator()
        self.__turn_manager__ = TurnManager(self.__player1__, self.__player2__)
        self.__state_manager__ = GameStateManager()
    def roll_dice(self):
        """Coordina el lanzamiento de dados"""
        values = self.__dice__.roll()
        self.__turn_manager__.set_moves_from_dice(values, self.__dice__.is_double())
        return values
    def make_move(self, from_pos, die_value):
        """Coordina la ejecución de un movimiento simple"""
        current_player = self.__turn_manager__.get_current_player()
        color = current_player.get_color()
        if not self.__turn_manager__.has_move(die_value):
            return False
        forced_moves = self.__turn_manager__.get_forced_moves(self.__validator__, self.__board__, color)
        if die_value not in forced_moves:
            return False
        to_pos = self.__calculator__.calculate_destination(from_pos, die_value, color)
        if to_pos == 0:
            if not self.__calculator__.can_bear_off_exact_or_higher(from_pos, die_value, color, self.__board__):
                return False
        if not self._is_legal_move(from_pos, to_pos, color):
            return False
        self.__board__.move_checker(from_pos, to_pos, color)
        self.__turn_manager__.use_move(die_value)
        self.__state_manager__.check_winner(self.__board__, self.__player1__, self.__player2__)
        return True