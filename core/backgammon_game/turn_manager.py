class TurnManager:
    """Maneja turnos y movimientos restantes"""
    def __init__(self, player1, player2):
        """Inicializa con los dos jugadores"""
        self.__player1__ = player1
        self.__player2__ = player2
        self.__current_player__ = player1
        self.__remaining_moves__ = []
    def set_moves_from_dice(self, dice_values, is_double):
        """Establece movimientos basado en dados"""
        if is_double:
            self.__remaining_moves__ = [dice_values[0]] * 4
        else:
            self.__remaining_moves__ = sorted(dice_values, reverse=True)
    def use_move(self, die_value):
        """Usa un movimiento si está disponible"""
        if die_value in self.__remaining_moves__:
            self.__remaining_moves__.remove(die_value)
            return True
        return False
    def get_forced_moves(self, game_validator, board, color):
        """Obtiene movimientos forzados según las reglas"""
        moves = self.__remaining_moves__.copy()
        if not moves:
            return []
        if game_validator.must_enter_from_bar(color):
            forced = []
            for die in moves:
                if color == "white":
                    to_pos = die
                else:
                    to_pos = 25 - die
                if game_validator.is_valid_move(25, to_pos, color):
                    forced.append(die)
            return forced if forced else moves
        return moves  
    def switch_player(self):
        """Cambia al siguiente jugador"""
        self.__current_player__ = self.__player2__ if self.__current_player__ == self.__player1__ else self.__player1__
        self.__remaining_moves__ = []
    def get_current_player(self):
        """Obtiene el jugador actual"""
        return self.__current_player__
    def get_remaining_moves(self):
        """Obtiene movimientos restantes"""
        return self.__remaining_moves__.copy()
    def is_turn_complete(self):
        """Dice si el turno está completo"""
        return len(self.__remaining_moves__) == 0
    def has_move(self, die_value):
        """Verifica si tiene un movimiento disponible"""
        return die_value in self.__remaining_moves__