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
        if len(set(moves)) == 2 and len(moves) == 2:
            larger_die = max(moves)
            smaller_die = min(moves)
            can_use_both = self._can_use_both_dice(larger_die, smaller_die, game_validator, board, color)
            if can_use_both:
                return moves 
            can_use_larger = self._can_use_any_move_with_die(larger_die, game_validator, board, color)
            can_use_smaller = self._can_use_any_move_with_die(smaller_die, game_validator, board, color)
            if can_use_larger and not can_use_smaller:
                return [larger_die]
            elif can_use_smaller and not can_use_larger:
                return [smaller_die]
            elif can_use_larger: 
                return [larger_die]
        return moves  