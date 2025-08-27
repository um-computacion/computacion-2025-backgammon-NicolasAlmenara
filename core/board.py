class Board:
    def __init__(self):
        self.positions = [{"color": None, "count": 0} for _ in range(24)]
        self.board_inicial()

    def board_inicial(self):
        self.positions[23] = {"color": "white", "count": 2}
        self.positions[12] = {"color": "white", "count": 5}
        self.positions[7]  = {"color": "white", "count": 3}
        self.positions[5]  = {"color": "white", "count": 5}
        self.positions[0]  = {"color": "black", "count": 2}
        self.positions[11] = {"color": "black", "count": 5}
        self.positions[16] = {"color": "black", "count": 3}
        self.positions[18] = {"color": "black", "count": 5}
