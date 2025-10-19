import unittest
from core.board import Board
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    def test_board_initialization(self):
        """Verifica que el tablero se inicializa correctamente"""
        self.assertEqual(len(self.board.points), 24)
        self.assertEqual(self.board.bar["white"], 0)
        self.assertEqual(self.board.bar["black"], 0)
        self.assertEqual(self.board.off["white"], 0)
        self.assertEqual(self.board.off["black"], 0)
    def test_initial_position_white(self):
        """Verifica las posiciones iniciales de las fichas blancas"""
        point1 = self.board.get_point(1)
        self.assertEqual(point1[0], "white")
        self.assertEqual(point1[1], 2)
        point12 = self.board.get_point(12)
        self.assertEqual(point12[0], "white")
        self.assertEqual(point12[1], 5)
        point17 = self.board.get_point(17)
        self.assertEqual(point17[0], "white")
        self.assertEqual(point17[1], 3)
        point19 = self.board.get_point(19)
        self.assertEqual(point19[0], "white")
        self.assertEqual(point19[1], 5)
    def test_initial_position_black(self):
        """Verifica las posiciones iniciales de las fichas negras"""
        point24 = self.board.get_point(24)
        self.assertEqual(point24[0], "black")
        self.assertEqual(point24[1], 2)
        point13 = self.board.get_point(13)
        self.assertEqual(point13[0], "black")
        self.assertEqual(point13[1], 5)
        point8 = self.board.get_point(8)
        self.assertEqual(point8[0], "black")
        self.assertEqual(point8[1], 3)
        point6 = self.board.get_point(6)
        self.assertEqual(point6[0], "black")
        self.assertEqual(point6[1], 5)
    def test_empty_points(self):
        """Verifica que los puntos vacíos están correctos"""
        empty_points = [2, 3, 4, 5, 7, 9, 10, 11, 14, 15, 16, 18, 20, 21, 22, 23]
        for point_num in empty_points:
            point = self.board.get_point(point_num)
            self.assertEqual(point[0], "")
            self.assertEqual(point[1], 0)
    def test_get_point_valid(self):
        """Verifica que se pueden obtener puntos válidos"""
        point1 = self.board.get_point(1)
        self.assertIsNotNone(point1)
        self.assertIsInstance(point1, list)
        self.assertEqual(len(point1), 2)
        point24 = self.board.get_point(24)
        self.assertIsNotNone(point24)
        self.assertIsInstance(point24, list)
    def test_get_point_invalid(self):
        """Verifica el manejo de puntos inválidos"""
        self.assertIsNone(self.board.get_point(0))
        self.assertIsNone(self.board.get_point(25))
        self.assertIsNone(self.board.get_point(-1))
        self.assertIsNone(self.board.get_point(100))
    def test_move_checker_normal(self):
        """Verifica el movimiento normal de una ficha"""
        self.board.move_checker(1, 2, "white")
        point1 = self.board.get_point(1)
        self.assertEqual(point1[1], 1)
        point2 = self.board.get_point(2)
        self.assertEqual(point2[0], "white")
        self.assertEqual(point2[1], 1)
    def test_move_checker_to_occupied_same_color(self):
        """Verifica mover a un punto ocupado por el mismo color"""
        self.board.move_checker(1, 12, "white")
        point12 = self.board.get_point(12)
        self.assertEqual(point12[0], "white")
        self.assertEqual(point12[1], 6)
    def test_move_checker_capture(self):
        """Verifica la captura de una ficha enemiga"""
        self.board.points[1] = ["black", 1]
        self.board.move_checker(1, 2, "white")
        self.assertEqual(self.board.bar["black"], 1)
        point2 = self.board.get_point(2)
        self.assertEqual(point2[0], "white")
        self.assertEqual(point2[1], 1)
    def test_move_checker_from_bar(self):
        """Verifica el movimiento desde la barra"""
        self.board.bar["white"] = 1
        self.board.move_checker(25, 2, "white")
        self.assertEqual(self.board.bar["white"], 0)
        point2 = self.board.get_point(2)
        self.assertEqual(point2[0], "white")
        self.assertEqual(point2[1], 1)
    def test_move_checker_bear_off(self):
        """Verifica sacar una ficha del tablero"""
        self.board.move_checker(1, 0, "white")
        point1 = self.board.get_point(1)
        self.assertEqual(point1[1], 1)
        self.assertEqual(self.board.off["white"], 1)
    def test_move_checker_clear_point(self):
        """Verifica que se limpia un punto cuando queda vacío"""
        self.board.move_checker(1, 2, "white")
        self.board.move_checker(1, 3, "white")
        point1 = self.board.get_point(1)
        self.assertEqual(point1[0], "")
        self.assertEqual(point1[1], 0)
    def test_has_checkers_on_bar_initial(self):
        """Verifica el estado inicial de la barra"""
        self.assertFalse(self.board.has_checkers_on_bar("white"))
        self.assertFalse(self.board.has_checkers_on_bar("black"))
    def test_has_checkers_on_bar_with_checkers(self):
        """Verifica detectar fichas en la barra"""
        self.board.bar["white"] = 2
        self.board.bar["black"] = 1
        self.assertTrue(self.board.has_checkers_on_bar("white"))
        self.assertTrue(self.board.has_checkers_on_bar("black"))
    def test_has_checkers_on_bar_after_removal(self):
        """Verifica el estado después de quitar fichas de la barra"""
        self.board.bar["white"] = 1
        self.assertTrue(self.board.has_checkers_on_bar("white"))
        self.board.bar["white"] = 0
        self.assertFalse(self.board.has_checkers_on_bar("white"))
    def test_can_bear_off_initial_position(self):
        """Verifica que no se puede sacar fichas en posición inicial"""
        self.assertFalse(self.board.can_bear_off("white"))
        self.assertFalse(self.board.can_bear_off("black"))
    def test_can_bear_off_with_checkers_on_bar(self):
        """Verifica que no se puede sacar fichas con fichas en la barra"""
        self._setup_all_checkers_in_home("white")
        self.board.bar["white"] = 1
        self.assertFalse(self.board.can_bear_off("white"))
    def test_can_bear_off_all_in_home_white(self):
        """Verifica que se puede sacar fichas con todas en casa blanca"""
        self._setup_all_checkers_in_home("white")
        self.assertTrue(self.board.can_bear_off("white"))
    def test_can_bear_off_all_in_home_black(self):
        """Verifica que se puede sacar fichas con todas en casa negra"""
        self._setup_all_checkers_in_home("black")
        self.assertTrue(self.board.can_bear_off("black"))
    def test_can_bear_off_with_checkers_outside_home(self):
        """Verifica que no se puede sacar fichas con fichas fuera de casa"""
        self._setup_all_checkers_in_home("white")
        self.board.points[6] = ["white", 1]
        self.assertFalse(self.board.can_bear_off("white"))
    def test_is_winner_initial(self):
        """Verifica que no hay ganador en posición inicial"""
        self.assertIsNone(self.board.is_winner())
    def test_is_winner_white_wins(self):
        """Verifica la victoria de las blancas"""
        self.board.off["white"] = 15
        self.assertEqual(self.board.is_winner(), "white")
    def test_is_winner_black_wins(self):
        """Verifica la victoria de las negras"""
        self.board.off["black"] = 15
        self.assertEqual(self.board.is_winner(), "black")
    def test_is_winner_partial_off(self):
        """Verifica que no hay ganador con fichas parcialmente fuera"""
        self.board.off["white"] = 14
        self.board.off["black"] = 10
        self.assertIsNone(self.board.is_winner())
    def test_show_board_runs(self):
        """Verifica que show_board se ejecuta sin errores"""
        try:
            self.board.show_board()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
    def test_show_board_with_bar_checkers(self):
        """Verifica show_board con fichas en la barra"""
        self.board.bar["white"] = 2
        self.board.bar["black"] = 1
        try:
            self.board.show_board()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
    def test_show_board_empty_bar(self):
        """Verifica show_board con barra vacía"""
        try:
            self.board.show_board()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)
        self.assertTrue(success)
    def _setup_all_checkers_in_home(self, color):
        for i in range(24):
            self.board.points[i] = ["", 0]
        self.board.bar[color] = 0
        if color == "white":
            self.board.points[0] = ["white", 3]
            self.board.points[1] = ["white", 3]
            self.board.points[2] = ["white", 3]
            self.board.points[3] = ["white", 3]
            self.board.points[4] = ["white", 2]
            self.board.points[5] = ["white", 1]
        else:
            self.board.points[18] = ["black", 3]
            self.board.points[19] = ["black", 3]
            self.board.points[20] = ["black", 3]
            self.board.points[21] = ["black", 3]
            self.board.points[22] = ["black", 2]
            self.board.points[23] = ["black", 1]
if __name__ == '__main__':
    unittest.main()