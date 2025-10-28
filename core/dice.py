import random
class Dice:
    """Los dados del juego"""
    def __init__(self):
        """Crea los dados"""
        self.__values__ = [1, 1]
    def roll(self):
        """Lanza los dados"""
        self.__values__ = [random.randint(1, 6), random.randint(1, 6)]
        return self.__values__
    def is_double(self):
        """Dice si es un doble"""
        return self.__values__[0] == self.__values__[1]
    @property
    def value1(self):
        """Acceso al primer dado"""
        return self.__values__[0]
    @property
    def value2(self):
        """Acceso al segundo dado"""
        return self.__values__[1]