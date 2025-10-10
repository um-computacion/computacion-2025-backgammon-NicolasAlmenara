class MoveCalculator:
    """Calcula destinos de movimientos"""
    def calculate_destination(self, from_pos, die_value, color):
        """Calcula la posición destino de un movimiento"""
        if from_pos == 25:
            return self._calculate_from_bar(die_value, color)
        return self._calculate_normal_move(from_pos, die_value, color)
    def _calculate_from_bar(self, die_value, color):
        """Calcula destino desde la barra"""
        if color == "white":
            return die_value
        else:
            return 25 - die_value
    def _calculate_normal_move(self, from_pos, die_value, color):
        """Calcula destino de movimiento normal"""
        if color == "white":
            to_pos = from_pos + die_value
            return 0 if to_pos > 24 else to_pos
        else:
            to_pos = from_pos - die_value
            return 0 if to_pos < 1 else to_pos