class MoveValidator:
    """Valida movimientos del backgammon"""
    def __init__(self, board):
        """Crea el validador con una referencia al tablero"""
        self.__board__ = board
    def is_valid_move(self, from_pos, to_pos, color):
        """Valida si un movimiento es legal"""
        if not self._is_valid_source(from_pos, color):
            return False
        if not self._is_valid_destination(to_pos, color):
            return False
        return True
    def _is_valid_source(self, from_pos, color):
        """Valida la posición origen"""
        if from_pos == 25:
            return self.__board__.has_checkers_on_bar(color)
        if from_pos < 1 or from_pos > 24:
            return False
        point = self.__board__.get_point(from_pos)
        return point and point[0] == color and point[1] > 0
    def _is_valid_destination(self, to_pos, color):
        """Valida la posición destino"""
        if to_pos == 0:
            return self.__board__.can_bear_off(color)
        if to_pos < 1 or to_pos > 24:
            return False
        point = self.__board__.get_point(to_pos)
        if point[0] != "" and point[0] != color and point[1] >= 2:
            return False
        return True
    def must_enter_from_bar(self, color):
        """Dice si debe mover desde la barra primero"""
        return self.__board__.has_checkers_on_bar(color)