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