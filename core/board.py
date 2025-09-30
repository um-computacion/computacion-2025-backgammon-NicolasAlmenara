class Board:
    def __init__(self):
        """Inicializa un tablero vacío y coloca las fichas en posición inicial."""
        self.__positions__ = [{"color": None, "count": 0} for _ in range(24)]
        self.setup_initial_position()

    def setup_initial_position(self):
        """Configura las posiciones iniciales de las fichas según las reglas del backgammon."""
        self.__positions__[23] = {"color": "white", "count": 2}
        self.__positions__[12] = {"color": "white", "count": 5}
        self.__positions__[7]  = {"color": "white", "count": 3}
        self.__positions__[5]  = {"color": "white", "count": 5}
        self.__positions__[0]  = {"color": "black", "count": 2}
        self.__positions__[11] = {"color": "black", "count": 5}
        self.__positions__[16] = {"color": "black", "count": 3}
        self.__positions__[18] = {"color": "black", "count": 5}
        
    def move_checker(self, from_pos, to_pos, color):
        """Mueve una ficha del color especificado desde from_pos hacia to_pos."""
        if from_pos == 25:
            return self.move_from_bar(to_pos, color)
            
        if self.__positions__[from_pos]["color"] != color or self.__positions__[from_pos]["count"] == 0:
            return False
        if self.__positions__[to_pos]["color"] and self.__positions__[to_pos]["color"] != color and self.__positions__[to_pos]["count"] == 1:
            self.__positions__[to_pos] = {"color": color, "count": 1}
        else:
            if self.__positions__[to_pos]["color"] in [None, color]:
                self.__positions__[to_pos]["color"] = color
                self.__positions__[to_pos]["count"] += 1
            else:
                return False
        self.__positions__[from_pos]["count"] -= 1
        if self.__positions__[from_pos]["count"] == 0:
            self.__positions__[from_pos]["color"] = None
        return True

    def move_from_bar(self, to_pos, color):
        """Mueve una ficha desde la barra al tablero"""
        if self.__positions__[to_pos]["color"] and self.__positions__[to_pos]["color"] != color and self.__positions__[to_pos]["count"] == 1:
            self.__positions__[to_pos] = {"color": color, "count": 1}
        elif self.__positions__[to_pos]["color"] in [None, color]:
            self.__positions__[to_pos]["color"] = color
            self.__positions__[to_pos]["count"] += 1
        else:
            return False
        return True

    def bear_off_checker(self, from_pos, color):
        """Saca una ficha del color especificado desde from_pos del tablero."""
        if self.__positions__[from_pos]["color"] == color and self.__positions__[from_pos]["count"] > 0:
            self.__positions__[from_pos]["count"] -= 1
            if self.__positions__[from_pos]["count"] == 0:
                self.__positions__[from_pos]["color"] = None
            return True
        return False

    def get_position(self, pos):
        """Retorna la información de la posición especificada del tablero."""
        return self.__positions__[pos]

    def is_move_valid(self, from_pos, to_pos, color):
        """Verifica si un movimiento del color dado es válido según las reglas."""
        if from_pos == 25:
            if to_pos < 0 or to_pos > 23:
                return False
            if self.__positions__[to_pos]["color"] not in [None, color] and self.__positions__[to_pos]["count"] > 1:
                return False
            return True
            
        if from_pos < 0 or from_pos > 23 or to_pos < 0 or to_pos > 23:
            return False
        if self.__positions__[from_pos]["color"] != color or self.__positions__[from_pos]["count"] == 0:
            return False
        if self.__positions__[to_pos]["color"] not in [None, color] and self.__positions__[to_pos]["count"] > 1:
            return False
        return True

    def show_board(self):
        """Imprime el tablero con formato visual mostrando las fichas y posiciones."""
        def format_point(pos):
            if not self.__positions__[pos]["color"] or self.__positions__[pos]["count"] == 0:
                return "  . "
            
            count = self.__positions__[pos]["count"]
            color = self.__positions__[pos]["color"][0].upper()  # B o W
            
            if count <= 9:
                return f" {color}{count} "
            else:
                return f"{color}{count:2}"
        
        print("\n" + "="*65)
        print("TABLERO DE BACKGAMMON")
        print("="*65)
        
        print(" 13   14   15   16   17   18  |BAR|  19   20   21   22   23   24 |OFF|")
        
        print(f"{format_point(12)} {format_point(13)} {format_point(14)} {format_point(15)} {format_point(16)} {format_point(17)} |", end="")
        
        from core.checker import Checker
        white_bar = Checker.get_bar_count("white")
        black_bar = Checker.get_bar_count("black")
        if white_bar > 0:
            print(f" W{white_bar} ", end="")
        elif black_bar > 0:
            print(f" B{black_bar} ", end="")
        else:
            print("  . ", end="")
        
        print(f"| {format_point(18)} {format_point(19)} {format_point(20)} {format_point(21)} {format_point(22)} {format_point(23)} |   |")
    
        print(" " * 65)
        print(" " * 65)
        
        print(f"{format_point(11)} {format_point(10)} {format_point(9)} {format_point(8)} {format_point(7)} {format_point(6)} | . | {format_point(5)} {format_point(4)} {format_point(3)} {format_point(2)} {format_point(1)} {format_point(0)} |   |")
        
        print(" 12   11   10    9    8    7  |   |   6    5    4    3    2    1 |   |")
        
        print("="*65)
        print("B = Negro, W = Blanco, Número = cantidad de fichas")
        print("="*65 + "\n")