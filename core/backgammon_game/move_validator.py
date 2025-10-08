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