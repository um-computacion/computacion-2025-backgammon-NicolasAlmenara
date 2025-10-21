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
        """Verifica si puede sacar ficha según reglas de backgammon
        Reglas:
        - Blancas: punto 24 más cerca de salir (dado 1), punto 19 más lejos (dado 6)
        - Negras: punto 1 más cerca de salir (dado 1), punto 6 más lejos (dado 6)
        - Regla 3: No puedes sacar desde punto bajo si hay fichas en puntos más altos
        - Regla 4: Si no hay ficha exacta del dado, DEBES usar desde el punto MÁS ALTO disponible
        """
        if color == "white":
            home_pos = 25 - from_pos
            highest_point = None
            for i in range(19, 25):
                point = board.get_point(i)
                if point and point[0] == color and point[1] > 0:
                    highest_point = i
                    break
            if home_pos == die_value:
                if from_pos == highest_point:
                    return True
                return False
            if home_pos < die_value and from_pos >= 19:
                exact_pos = 25 - die_value
                exact_point = board.get_point(exact_pos)
                if exact_point and exact_point[0] == color and exact_point[1] > 0:
                    return False
                if from_pos == highest_point:
                    return True
                else:
                    return False
        else:
            home_pos = from_pos
            highest_point = None
            for i in range(6, 0, -1):
                point = board.get_point(i)
                if point and point[0] == color and point[1] > 0:
                    highest_point = i
                    break
            if home_pos == die_value:
                if from_pos == highest_point:
                    return True
                return False
            if home_pos < die_value and home_pos <= 6:
                exact_pos = die_value
                if exact_pos <= 6:
                    exact_point = board.get_point(exact_pos)
                    if exact_point and exact_point[0] == color and exact_point[1] > 0:
                        return False
                if from_pos == highest_point:
                    return True
                else:
                    return False
        return False