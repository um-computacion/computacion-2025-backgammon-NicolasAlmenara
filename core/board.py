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
        
    def move_checker(self, from_pos, to_pos, color):
        if self.positions[from_pos]["color"] != color or self.positions[from_pos]["count"] == 0:
            return False
        if self.positions[to_pos]["color"] and self.positions[to_pos]["color"] != color and self.positions[to_pos]["count"] == 1:
            self.positions[to_pos] = {"color": color, "count": 1}
        else:
            if self.positions[to_pos]["color"] in [None, color]:
                self.positions[to_pos]["color"] = color
                self.positions[to_pos]["count"] += 1
            else:
                return False
        self.positions[from_pos]["count"] -= 1
        if self.positions[from_pos]["count"] == 0:
            self.positions[from_pos]["color"] = None
        return True
    
    def bear_off_checker(self, from_pos, color):
        if self.positions[from_pos]["color"] == color and self.positions[from_pos]["count"] > 0:
            self.positions[from_pos]["count"] -= 1
            if self.positions[from_pos]["count"] == 0:
                self.positions[from_pos]["color"] = None
            return True
        return False

    def get_position(self, pos):
        return self.positions[pos]
        
    def is_move_valid(self, from_pos, to_pos, color):
        if from_pos < 0 or from_pos > 23 or to_pos < 0 or to_pos > 23:
            return False
        if self.positions[from_pos]["color"] != color or self.positions[from_pos]["count"] == 0:
            return False
        if self.positions[to_pos]["color"] not in [None, color] and self.positions[to_pos]["count"] > 1:
            return False
        return True

    def show_board(self):
        for i, pos in enumerate(self.positions):
            color = pos["color"] if pos["color"] else "vacío"
            print(f"{i:2}: {color} x{pos['count']}", end=" | ")
            if (i + 1) % 6 == 0:
                print()