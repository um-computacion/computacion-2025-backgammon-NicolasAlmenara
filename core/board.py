class Board:
    """El tablero del juego"""
    def __init__(self):
        """Crea el tablero en posición inicial"""
        self.points = [["", 0] for _ in range(24)]
        self.bar = {"white": 0, "black": 0}
        self.off = {"white": 0, "black": 0}
        self._setup_initial_position()
    def _setup_initial_position(self):
        """Configura la posición inicial del backgammon"""
        self.points[0] = ["white", 2]
        self.points[11] = ["white", 5]
        self.points[16] = ["white", 3]
        self.points[18] = ["white", 5]
        self.points[23] = ["black", 2]
        self.points[12] = ["black", 5]
        self.points[7] = ["black", 3]
        self.points[5] = ["black", 5]
    def get_point(self, position):
        """Obtiene la información de un punto"""
        if 1 <= position <= 24:
            return self.points[position - 1]
        return None
    def move_checker(self, from_pos, to_pos, color):
        """Mueve una ficha (sin validar)"""
        if from_pos == 25:
            self.bar[color] -= 1
        else:
            point = self.points[from_pos - 1]
            point[1] -= 1
            if point[1] == 0:
                point[0] = ""
        if to_pos == 0:
            self.off[color] += 1
        else:
            point = self.points[to_pos - 1]
            if point[1] == 1 and point[0] != color and point[0] != "":
                enemy_color = "white" if color == "black" else "black"
                self.bar[enemy_color] += 1
                point[1] = 0
                point[0] = ""
            point[0] = color
            point[1] += 1
    def has_checkers_on_bar(self, color):
        """Dice si hay fichas en la barra"""
        return self.bar[color] > 0
    def can_bear_off(self, color):
        """Dice si el jugador puede sacar fichas"""
        if self.has_checkers_on_bar(color):
            return False
        home_range = range(1, 7) if color == "white" else range(19, 25)
        for i in range(24):
            point = self.points[i]
            if point[0] == color and point[1] > 0:
                if (i + 1) not in home_range:
                    return False
        return True
    
    def show_board(self):
        """Muestra el tablero"""
        print("\n" + "="*70)
        print("                    TABLERO DE BACKGAMMON")
        print("="*70)
        top_nums = "   "
        for i in range(13, 25):
            top_nums += f"{i:>3} "
        print(top_nums)
        top_line = "   "
        for i in range(12, 24):
            point = self.points[i]
            if point[1] > 0:
                letter = "W" if point[0] == "white" else "B"
                top_line += f"{letter}{point[1]:>2} "
            else:
                top_line += " .  "
        print(top_line)
        
        print("   " + "-" * 48)
        bar_info = ""
        if self.bar["white"] > 0:
            bar_info += f"W{self.bar['white']} "
        if self.bar["black"] > 0:
            bar_info += f"B{self.bar['black']} "
        if not bar_info:
            bar_info = "vacía"
        print(f"BARRA: {bar_info:^42}")
        
        print("   " + "-" * 48)
        bottom_line = "   "
        for i in range(11, -1, -1):
            point = self.points[i]
            if point[1] > 0:
                letter = "W" if point[0] == "white" else "B"
                bottom_line += f"{letter}{point[1]:>2} "
            else:
                bottom_line += " .  "
        print(bottom_line)
        bottom_nums = "   "
        for i in range(12, 0, -1):
            bottom_nums += f"{i:>3} "
        print(bottom_nums)
        print()
        off_info = f"FUERA - Blancas: {self.off['white']}  |  Negras: {self.off['black']}"
        print(f"{off_info:^70}")
        print("="*70)
    def is_winner(self):
        """Dice si hay un ganador"""
        if self.off["white"] == 15:
            return "white"
        elif self.off["black"] == 15:
            return "black"
        return None
        