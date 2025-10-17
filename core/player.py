class Player:
    """Un jugador del juego"""
    def __init__(self, name, color):
        """Crea un jugador con nombre y color"""
        self.__name__ = name
        self.__color__ = color
    def get_name(self):
        """Obtiene el nombre del jugador"""
        return self.__name__
    def get_color(self):
        """Obtiene el color del jugador"""
        return self.__color__