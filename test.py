import unittest
from game import *


class TestVierGewinnt(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.ai_player = PlayerAI()

    def test_board_initialization(self):
        self.assertEqual(len(self.board.get_gameboard()), 7)  # 7 Spalten
        for col in self.board.get_gameboard():
            self.assertEqual(len(col), 0)  # Alle Spalten sind leer

    def test_player_move_valid(self):
        self.player1.current_move = 3  # Setzt eine gültige Spalte
        self.assertTrue(self.board.update_board(self.player1))  # Sollte True sein
        self.assertEqual(self.board.get_gameboard()[2][0], "X")  # "X" sollte in Spalte 3 sein

    def test_player_move_invalid(self):
        self.player1.current_move = 8  # Ungültige Spalte
        with self.assertRaises(IndexError):
            self.board.update_board(self.player1)

    def test_check_for_win_horizontal(self):
        for i in range(4):
            self.player1.current_move = i + 1
            self.board.update_board(self.player1)
        self.assertTrue(self.board.check_for_win("X"))

    def test_check_for_win_vertical(self):
        for _ in range(4):
            self.player1.current_move = 1
            self.board.update_board(self.player1)
        self.assertTrue(self.board.check_for_win("X"))

    def test_check_for_win_diagonal(self):
        moves = [(1, "X"), (2, "O"), (2, "X"), (3, "O"), (3, "O"), (3, "X"), (4, "O"), (4, "O"), (4, "O"), (4, "X")]
        for move in moves:
            self.player1.player_id = move[1]
            self.player1.current_move = move[0]
            self.board.update_board(self.player1)
        self.assertTrue(self.board.check_for_win("X"))

    def test_ai_move(self):
        self.ai_player.get_move()
        self.assertIn(self.ai_player.current_move, range(1, 8))  # AI sollte gültige Spalte wählen


if __name__ == "__main__":
    unittest.main()
