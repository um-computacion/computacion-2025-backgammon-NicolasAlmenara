import unittest
from core.dice import Dice
class Test_Dice(unittest.TestCase):
    def test_roll(self):
        d = Dice()
        value1, value2 = d.roll()
        self.assertTrue(1 <= value1 <= 6)
        self.assertTrue(1 <= value2 <= 6)
        if value1 == value2:
            self.assertTrue(d.doubles)
        else:
            self.assertFalse(d.doubles)
    def test_get_values(self):
        d = Dice()
        d.roll()
        v1, v2 = d.get_values()
        self.assertEqual((d.value1, d.value2), (v1, v2))
    def test_is_double(self):
        d = Dice()
        d.roll()
        if d.value1 == d.value2:
            self.assertTrue(d.is_double())
        else:
            self.assertFalse(d.is_double())