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
    def _is_legal_move(self, from_pos, to_pos, color):
        """Coordina la validación de movimientos"""
        if self.__validator__.must_enter_from_bar(color) and from_pos != 25:
            return False
        return self.__validator__.is_valid_move(from_pos, to_pos, color)
    def switch_turn(self):
        """Coordina el cambio de turno"""
        self.__turn_manager__.switch_player()
    def get_current_player(self):
        """Obtiene el jugador actual"""
        return self.__turn_manager__.get_current_player()
    def get_remaining_moves(self):
        """Obtiene movimientos restantes"""
        return self.__turn_manager__.get_remaining_moves()
    def is_turn_complete(self):
        """Verifica si el turno está completo"""
        return self.__turn_manager__.is_turn_complete()
    def is_game_over(self):
        """Verifica si el juego terminó"""
        return self.__state_manager__.is_game_over()
    def get_winner(self):
        """Obtiene el ganador"""
        return self.__state_manager__.get_winner()
    def show_board(self):
        """Muestra el tablero"""
        self.__board__.show_board()
    def has_valid_moves(self):
        """Verifica si el jugador actual tiene movimientos válidos"""
        current_player = self.__turn_manager__.get_current_player()
        color = current_player.get_color()
        remaining_moves = self.__turn_manager__.get_remaining_moves()
        for die_value in remaining_moves:
            if self.__validator__.must_enter_from_bar(color):
                if color == "white":
                    to_pos = die_value
                else:
                    to_pos = 25 - die_value
                if self.__validator__.is_valid_move(25, to_pos, color):
                    return True
            else:
                for pos in range(1, 25):
                    point = self.__board__.get_point(pos)
                    if point and point[0] == color and point[1] > 0:
                        to_pos = self.__calculator__.calculate_destination(pos, die_value, color)
                        if to_pos == 0:
                            if self.__calculator__.can_bear_off_exact_or_higher(pos, die_value, color, self.__board__):
                                return True
                        elif self.__validator__.is_valid_move(pos, to_pos, color):
                            return True
        return False
    def get_forced_move_message(self):
        """Obtiene mensaje sobre movimientos forzados"""
        current_player = self.__turn_manager__.get_current_player()
        color = current_player.get_color()
        forced_moves = self.__turn_manager__.get_forced_moves(self.__validator__, self.__board__, color)
        all_moves = self.__turn_manager__.get_remaining_moves()
        if self.__validator__.must_enter_from_bar(color):
            return "¡DEBES entrar TODAS las fichas desde la barra primero!"
        if len(forced_moves) < len(all_moves):
            return f"¡DEBES usar dado(s): {forced_moves}!"
        return None
    def get_available_moves(self):
        """Obtiene movimientos disponibles según reglas"""
        current_player = self.__turn_manager__.get_current_player()
        color = current_player.get_color()
        return self.__turn_manager__.get_forced_moves(self.__validator__, self.__board__, color)
    def count_checkers_on_bar(self, color):
        """Cuenta fichas en la barra"""
        return self.__board__.get_bar_count(color)
    def reset_game(self):
        """Coordina el reinicio del juego"""
        self.__board__ = Board()
        self.__turn_manager__ = TurnManager(self.__player1__, self.__player2__)
        self.__state_manager__.reset_game()