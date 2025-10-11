class GameStateManager:
    """Maneja el estado y fin del juego"""
    def __init__(self):
        """Inicializa el estado del juego"""
        self.__game_over__ = False
        self.__winner__ = None
    def check_winner(self, board, player1, player2):
        """Verifica si hay ganador"""
        winner_color = board.is_winner()
        if winner_color:
            self.__game_over__ = True
            self.__winner__ = player1 if winner_color == player1.get_color() else player2
            return True
        return False