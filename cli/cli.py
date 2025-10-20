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
            result = self.play_turn()
            if result == "exit":
                return
        winner = self.__game__.get_winner()
        print(f"\n¡{winner.get_name()} GANÓ!")
    def play_turn(self):
        """Juega un turno completo"""
        player = self.__game__.get_current_player()
        print(f"\nTurno de {player.get_name()} ({player.get_color()})")
        self.__game__.show_board()
        dice = self.__game__.roll_dice()
        print(f"Dados: {dice}")
        moves = self.__game__.get_remaining_moves()
        if not self.__game__.has_valid_moves():
            print("No hay movimientos válidos. Turno perdido.")
            self.__game__.switch_turn()
            return
        while moves and not self.__game__.is_game_over():
            available_moves = self.__game__.get_available_moves()
            print(f"Dados lanzados: {moves}")
            print(f"Puedes usar: {available_moves}")
            forced_message = self.__game__.get_forced_move_message()
            if forced_message:
                print(f" {forced_message}")
            current_player = self.__game__.get_current_player()
            bar_count = self.__game__.count_checkers_on_bar(current_player.get_color())
            if bar_count > 0:
                print(f"Tienes {bar_count} fichas en la barra")
            if not self.__game__.has_valid_moves():
                print("No quedan movimientos válidos.")
                break
            try:
                print(f"\n Tienes {len(moves)} movimiento(s) restante(s)")
                print("Opciones:")
                print("1. Usar UN dado en UNA ficha")
                print("2. Usar VARIOS dados en LA MISMA ficha")
                print("3. SALIR del juego")
                option = input("¿Qué quieres hacer? (1/2/3): ").strip()
                if option == "1":
                    from_pos = int(input("¿Desde qué posición? (1-24, 25=barra): "))
                    print(f"Dados disponibles: {available_moves}")
                    die_value = int(input("¿Qué dado usar?: "))
                    if self.__game__.make_move(from_pos, die_value):
                        print(f"Moviste ficha desde {from_pos} usando dado {die_value}")
                    else:
                        print("Movimiento no válido")
                elif option == "2":
                    from_pos = int(input("¿Desde qué posición? (1-24, 25=barra): "))
                    print(f"Dados disponibles: {available_moves}")
                    dice_input = input("¿Qué dados usar en esta ficha? (ej: 6,4 o 6): ")
                    dice_list = [int(x.strip()) for x in dice_input.split(",")]
                    if self.__game__.make_compound_move(from_pos, dice_list):
                        print(f"Moviste ficha desde {from_pos} usando dados {dice_list}")
                    else:
                        print("Movimiento compuesto no válido")
                elif option == "3":
                    print("\n¡Gracias por jugar!")
                    print("Juego terminado.")
                    return "exit"
                else:
                    print("Opción inválida")
                    continue
                moves = self.__game__.get_remaining_moves()
            except (ValueError, KeyboardInterrupt):
                print("Entrada inválida")
                break
        if not self.__game__.get_remaining_moves():
            self.__game__.switch_turn()
if __name__ == "__main__":
    cli = CLI()
    cli.start()
