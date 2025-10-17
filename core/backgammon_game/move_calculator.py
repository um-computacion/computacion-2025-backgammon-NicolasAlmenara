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
    def can_bear_off_exact_or_higher(self, from_pos, die_value, color, board):
        """Verifica si puede sacar ficha exacta o con dado mayor"""
        if color == "white":
            home_pos = from_pos
            if home_pos == die_value:
                return True
            if home_pos < die_value and home_pos <= 6:
                for i in range(home_pos + 1, 7):
                    point = board.get_point(i)
                    if point and point[0] == color and point[1] > 0:
                        return False
                return True
        else:
            home_pos = 25 - from_pos
            if home_pos == die_value:
                return True
            if home_pos < die_value and from_pos >= 19:
                for i in range(home_pos + 1, 7):
                    check_pos = 25 - i
                    point = board.get_point(check_pos)
                    if point and point[0] == color and point[1] > 0:
                        return False
                return True
        return False