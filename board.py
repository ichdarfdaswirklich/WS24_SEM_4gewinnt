
import numpy as np


class Board:

    """Board Klasse zur Initialisierung und Anzeige des Spielfelds

    TODO: Public Attribute hier Dokumentieren

    Attribute
    ----------
    rows = statischer Wert 6
        initialisiert Reihenwert mit 6.
    columns = statischer Wert 7
        initialisiert Reihenwert mit 7.
   TODO: falls irrelevant (aufgrund anderer noch zu implementierenden Methoden) anpassen

    """

    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns



    @staticmethod
    def display_board():
        """Statische Methode um Board mittels Numpy "Zeros" Methode darzustellen
        Source/Initiale Idee: https://github.com/GabrielWongAu/connect-four-terminal-application
            Erstellung des initialen Board
            Returns
            -------
            Leere 6 x 7 Matrix, Felder gefüllt mit 0
            Mittels print Befehlen wird Darstellung "verschönert"
        """
        board = np.zeros((6, 7), dtype=np.uint8)
        cells = [" ", "#", "OO"]
        print("  1   2   3   4   5   6   7 ")
        for row in reversed(board):
            print("+---" * 6 + "+---+")
            print("| " + " | ".join([cells[u] for u in row]) + " |")
        print("+---" * 6 + "+---+")
        print("")
        print("")
        print("")


    @staticmethod
    def welcome_message():
        """Statische Methode für Willkommenstext in Terminal
        """
        creators = "Vici + Angie haben ihr bestes gegeben"
        print("---------------------------------------")
        print("---------------------------------------")
        print("---------------------------------------")
        print("---------------------------------------")

        print("---------------------------------------")
        print("Willkommen zu unserem verzweifelten Versuch 4 gewinnt zu programmieren")
        print("---------------------------------------")
        print("---------------------------------------")
        print(creators)
        print("---------------------------------------")
        print("---------------------------------------")
        return print("-------<3------")



    def iterate_over_board(self):
        pass


    def create_initial_board(self):
        pass







    def token_placed(self):
        pass



if __name__ == "__main__":
    board_test = Board()

    print(board_test.welcome_message())
    print(board_test.display_board())



