class Checker:
    bar_counts = {"white": 0, "black": 0}
    off_counts = {"white": 0, "black": 0}
    def __init__(self, color, estado="tablero"):
        self.color = color                  
        self.estado = "tablero"             
        if estado == "barra":
            Checker.bar_counts[self.color] += 1
            self.estado = "barra"
        elif estado == "fuera":
            Checker.off_counts[self.color] += 1
            self.estado = "fuera"
    
    def to_bar(self):
        if self.estado == "tablero":
            Checker.bar_counts[self.color] += 1
            self.estado = "barra"

    def to_board(self):
        if self.estado == "barra":
            Checker.bar_counts[self.color] -= 1
            self.estado = "tablero"

    def to_off(self):
        if self.estado == "tablero":
            Checker.off_counts[self.color] += 1
            self.estado = "fuera"
    @classmethod
    def get_bar_count(cls, color):
        return cls.bar_counts[color]

    @classmethod
    def get_off_count(cls, color):
        return cls.off_counts[color]