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