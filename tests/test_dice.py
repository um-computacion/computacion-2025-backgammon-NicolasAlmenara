import unittest
from core.dice import Dice
class TestDice(unittest.TestCase):
    def test_dice_initialization(self):
        """Verifica que los dados se inicializan correctamente"""
        d = Dice()
        self.assertEqual(d.value1, 1)
        self.assertEqual(d.value2, 1) 
    def test_roll_returns_values(self):
        """Verifica que roll() devuelve una lista de dos valores"""
        d = Dice()
        result = d.roll()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
    def test_roll_values_in_range(self):
        """Verifica que los valores están entre 1 y 6"""
        d = Dice()
        for _ in range(100):  
            values = d.roll()
            self.assertTrue(1 <= values[0] <= 6)
            self.assertTrue(1 <= values[1] <= 6)
    def test_roll_updates_properties(self):
        """Verifica que roll() actualiza value1 y value2"""
        d = Dice()
        values = d.roll()
        self.assertEqual(d.value1, values[0])
        self.assertEqual(d.value2, values[1])   
    def test_is_double_detection(self):
        """Verifica que is_double() funciona correctamente"""
        d = Dice()
        found_double = False
        found_non_double = False
        for _ in range(100):
            values = d.roll()
            if values[0] == values[1]:
                self.assertTrue(d.is_double())
                found_double = True
            else:
                self.assertFalse(d.is_double())
                found_non_double = True
            if found_double and found_non_double:
                break
        self.assertTrue(found_double or found_non_double, "Debería encontrar al menos algún resultado")
    def test_multiple_rolls_change_values(self):
        """Verifica que múltiples lanzamientos pueden cambiar los valores"""
        d = Dice()
        first_roll = d.roll()
        values_changed = False
        for _ in range(50):
            new_roll = d.roll()
            if new_roll != first_roll:
                values_changed = True
                break
        self.assertTrue(values_changed, "Los dados deberían cambiar de valor en múltiples lanzamientos")