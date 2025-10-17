from core.backgammon_game.backgammongame import BackgammonGame
class CLI:
    """Interfaz para el juego"""
    def __init__(self):
        """Crea la interfaz"""
        self.__game__ = None
    def start(self):
        """Inicia el juego"""
        print("=== BACKGAMMON ===")
        name1 = input("Nombre jugador 1 (blancas): ") or "Player 1"
        name2 = input("Nombre jugador 2 (negras): ") or "Player 2"
        self.__game__ = BackgammonGame(name1, name2)
        self.play_game()
    def play_game(self):
        """Ciclo principal del juego"""
        while not self.__game__.is_game_over():
            self.play_turn()
        winner = self.__game__.get_winner()
        print(f"\n¡{winner.get_name()} GANÓ!")